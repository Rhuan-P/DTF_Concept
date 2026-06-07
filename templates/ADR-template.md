# ADR — Architecture Decision Record (EXEMPLO)

---

## 1. Decisão Arquitetural: [Nome da Decisão]

**ID**: DEC-002  
**Data**: 2024-01-20  
**Autor**: Rhuan-P, Lead Architect  
**Status**: ✅ **PROPOSED** (proposta para decisão) | ✅ **APPROVED** (aprovado) | ✅ **DEPRECATED** (obsoleto)

---

## 2. Contexto

### 2.1 Problema Identificado
Precisamos validar inputs de API endpoints para prevenir injection attacks e garantir data consistency antes de processamento.

**Exemplo real:**
```bash
# Request malicioso sem validação:
curl -X POST https://api.example.com/products \
  -H "Content-Type: application/json" \
  -d '{"name": "<script>alert(1)</script>", "price": "-5"}'

# Impacto: SQL injection, negative price manipulation
```

### 2.2 Restrições e Requisitos
- **Security**: Todos inputs devem ser validados antes de acesso a banco de dados
- **Performance**: Validação não pode adicionar >5ms latência
- **Developer Experience**: Erros claros para frontend developers

**Documentação de referência:** [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheats/Input_Validation/)

---

## 3. Opções Consideradas

### Option A: Pydantic Models (✅ SELECIONADA)
```python
from pydantic import BaseModel, Field, validator

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(..., gt=0)  # >0 validation
    
    @validator('name')
    def sanitize_name(cls, v):
        if '<' in v or '>' in v:
            raise ValueError("Invalid characters in product name")
```

**Pros:**
- ✅ Auto-generated OpenAPI spec (`{"type": "string", "maxLength": 200}`)
- ✅ Type hints em IDE → autocomplete + intellisense
- ✅ Fast validation (<1ms overhead benchmarked)
- ✅ Erros estruturados: `{"error": "invalid_price", "code": "PRODUCT_PRICE_500"}`

**Cons:**
- ⚠️ More boilerplate (um arquivo por model)

---

### Option B: Flask-WTF Forms (❌ REJEITADA)
```python
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange

class ProductCreateForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), 
        Length(min=1, max=200),
        wtforms.validators.Regexp(r'^[a-zA-Z0-9\s\-_.]+$')  # regex validation
    ])
    price = DecimalField(decimal_places=2, validators=[
        NumberRange(min=0.0)
    ])
```

**Pros:**
- ✅ Integrated with Flask template system

**Cons:**
- ❌ No type hints → worse IDE support
- ❌ Regex in Python 3.7+ slow (compared to Pydantic compiled C extensions)
- ❌ No auto-generated OpenAPI spec

---

### Option C: Manual Dict Validation (❌ REJEITADA)
```python
def validate_product(data):
    errors = {}
    
    if 'name' not in data or len(data['name']) < 1:
        errors['name'] = ['Name is required']
    elif '>' in data['name']:
        errors['name'] = ['Invalid characters']
        
    if 'price' not in data or float(data['price']) <= 0:
        errors['price'] = ['Price must be positive']
    
    return errors, None  # errors dict or validated data
```

**Pros:**
- ✅ Zero boilerplate
- ✅ Flexible validation logic

**Cons:**
- ❌ No type hints → worse IDE support
- ❌ Manual OpenAPI generation (error-prone)
- ❌ Slower validation (pure Python, no C optimizations)

---

### Option D: SQLAlchemy ORM Only (❌ REJEITADA)
```python
from sqlalchemy import Column, String, Numeric

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200))  # length check at DB level only
    price = Column(Numeric(10, 2), nullable=False)  # no validation in Python
```

**Pros:**
- ✅ Validation moved to database level

**Cons:**
- ❌ No client-side validation (always hit DB first → slower)
- ❌ Error messages cryptic (SQL errors instead of user-friendly)
- ❌ Security risk: SQL injection before ORM layer

---

| Criteria | Pydantic A | Flask-WTF B | Manual C | SQLAlchemy D |
|----------|------------|-------------|----------|---------------|
| Type Safety | ✅ Strong | ⚠️ Weak | ❌ None | ✅ Schema-level |
| Performance | ✅ <1ms | ⚠️ 2-5ms | ⚠️ 3-8ms | ❌ Hit DB first |
| Developer Exp | ✅ Excellent | ⚠️ Good | ❌ Poor | ⚠️ Moderate |
| Security | ✅ Fast validation | ⚠️ OK | ⚠️ Slow | ❌ Risky |
| OpenAPI Auto | ✅ Yes | ❌ Manual | ❌ Manual | ✅ Auto (OpenAPI plugin) |

---

## 4. Decisão Tomada

**Option A: Pydantic Models é a escolha recomendada** por oferecer o melhor equilíbrio entre type safety, performance e developer experience.

### Justificativa Detalhada
1. **Type Safety**: Pydantic compila validações em C extensions → <1ms overhead vs Flask-WTF ~2-5ms
2. **Security First**: Validação ocorre antes de qualquer acesso a banco de dados
3. **Auto-generated OpenAPI**: IDE intellisense + API documentation automaticamente mantida
4. **Developer Velocity**: Type hints reduz erros em 70% (baseado em benchmarks internos)

**Trade-off Aceito:**
> *"Menos boilerplate inicial (Option C/D), mas ganho de velocidade a longo prazo via type safety e auto-generated docs"*

---

## 5. Consequências

### 5.1 Benefícios Tangíveis
- ✅ Redução de bugs em 60% (type hints catching errors at runtime)
- ✅ Auto-generated OpenAPI docs → menos erros por frontend developers
- ✅ Faster IDE autocomplete → reduced typing errors by 40%

### 5.2 Custos Operacionais
- ⚠️ Additional dependency (`pydantic>=2.0`) → ~1KB package size increase
- ⚠️ Learning curve for team unfamiliar with Pydantic v2 (v1→v2 breaking changes)

### 5.3 Impacto em Time-to-Market
- **Short-term**: +2h setup (model definitions para endpoints existentes)
- **Long-term**: -40% review time (fewer merge conflicts, clearer code ownership)

---

## 6. Implementação

### 6.1 Código Final (Após Decisão)

```python
# src/product/models.py
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from datetime import date

class ProductCreate(BaseModel):
    """Product creation request model with validation."""
    
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Product display name (no special characters)"
    )
    
    price: float = Field(
        ...,
        gt=0,
        le=999_999_999.99,
        description="Product price in local currency"
    )
    
    sku: Optional[str] = Field(
        None,
        max_length=50,
        description="Unique stock keeping unit code"
    )
    
    category_id: int = Field(..., ge=1, le=1000)  # Assumes 1000 categories max
    
    tags: Optional[List[str]] = Field(
        None,
        min_length=0,
        max_length=50,
        description="Product tags for filtering"
    )
    
    @validator('name')
    def sanitize_name(cls, v):
        """Remove any HTML/script injection attempts."""
        if '<' in v or '>' in v:
            raise ValueError("HTML tags not allowed in product names")
        
        if '\n' in v:
            raise ValueError("Line breaks not allowed in product names")
        
        return v.rstrip()  # Trim trailing whitespace
    
    @validator('category_id')
    def validate_category(cls, v):
        """Ensure category exists before database query."""
        from src.product.repositories import CategoryRepository
        
        if v < 1 or v > 1000:
            raise ValueError(f"Invalid category ID (must be 1-1000)")
        
        category_repo = CategoryRepository()
        existing_category_id = category_repo.get_by_id(v)
        
        if not existing_category_id:
            raise ValueError(f"Category {v} does not exist")
        
        return v

class ProductResponse(BaseModel):
    """Product response model with OpenAPI description."""
    
    id: int = Field(..., description="Unique product identifier")
    name: str = Field(..., description="Product display name")
    price: float = Field(..., description="Product price in local currency")
    sku: Optional[str] = Field(None, description="Stock keeping unit code")
    category_id: int = Field(..., description="Parent category reference")
    created_at: date = Field(..., description="Creation timestamp")

# Usage example with auto-generated OpenAPI spec:
from src.product.api import router

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,  # ← Auto-validated by Pydantic
    db: Session
):
    """Create a new product with validation."""
    
    # Validation happens automatically BEFORE this line!
    # OpenAPI auto-generated doc includes Pydantic Field descriptions
    
    product_repo = ProductRepository(db)
    existing_product = product_repo.get_by_sku(product.sku)
    
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"error": "duplicate_sku", "code": "PRODUCT_SKU_409"}
        )
    
    new_product = ProductCreate.model_validate(product.dict())
    created_product = product_repo.create(new_product)
    
    return ProductResponse.model_validate(created_product.to_dict())
```

### 6.2 Migrations Necessárias
- ✅ Add Pydantic dependency to `requirements.txt` / `pyproject.toml`
- ✅ Update existing endpoints with model definitions (one file per bounded context)
- ⚠️ Consider v2→v3 upgrade path if using older Pydantic

### 6.3 Rollback Plan
Se decisão falhar:
```python
# Fallback to manual validation if needed
def validate_product_fallback(data):
    errors = {}
    
    # Manual checks (slower but works)
    if 'name' not in data or not isinstance(data['name'], str):
        errors['name'] = ['Name is required']
    elif len(data['name']) < 1:
        errors['name'] = ['Name too short']
        
    return errors, data
```

---

## 7. Verificação de Decisão

### 7.1 Success Metrics
| Metric | Target | Actual (3 months post-deploy) | Status |
|--------|--------|-------------------------------|--------|
| Error Rate Reduction | -50% | -62% ✅ | Exceeded |
| Code Review Time | -30% | -41% ✅ | Exceeded |
| Frontend Integration Errors | -80% | -73% ✅ | Met |

### 7.2 Feedback do Team
- **Lead Dev**: "Pydantic validation catching 95% of errors que seriam SQL injection attacks"
- **Frontend Lead**: "OpenAPI auto-generated docs saved us 20h de manual API spec writing"
- **DevOps**: "Type hints reduced deployment failures by 60%"

---

## 8. Decisões Relacionadas

| ADR ID | Title | Relation |
|--------|-------|----------|
| DEC-001 | Database Choice (PostgreSQL + Alembic) | Foundation |
| DEC-003 | Caching Strategy (Redis TTL-based) | Performance impact |

**See `.dtc/decisions/` for full decision history.**

---

## 9. Referências

- [Pydantic Official Docs](https://docs.pydantic.dev/)
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheats/Input_Validation/)
- [FastAPI Pydantic Integration](https://fastapi.tiangolo.com/tutorial/pydantic/#pydantic-models-for-request-validation)

---

> **\"This document captures the architectural decision for API input validation in the Product Service bounded context.\"**  
> Last reviewed: 2024-02-15 | Next review: 2024-08-15 (6-month cycle)

🔗 **Link direto ao arquivo**: `.dtc/decisions/002-api-validation-choice.md`
