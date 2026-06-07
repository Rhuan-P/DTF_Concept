# Feature Example — Adicionar Nova Feature usando DTF

Este exemplo demonstra como adicionar uma nova funcionalidade seguindo a metodologia DTF: **Contexto → Requisito → Implementação → Aceitação**.

---

## 📋 Cenário do Exemplo

**Nova feature**: Sistema de comentários em posts do blog.

**Fluxo desejado**:
1. Usuário cria post
2. Outros usuários adicionam comentários
3. Comentários visíveis na página do post
4. Paginação de comentários em API e frontend

---

## 📁 Estrutura de Diretórios

```
feature-example/
├── .dtc/                      # ⭐ Contexto específico deste feature
│   ├── context.md            # Contexto da nova feature
│   └── decisions/            # ADRs para decisões da feature
│       ├── 001-implementation-chosen.md
│       └── 002-database-model.md
├── .dtc/tasks/               # Artefatos por feature (opcional)
│   ├── dtr-user-comments.md  # DTR para esta feature
│   ├── dti-user-comments.md  # DTI para implementação
│   └── dta-user-comments.md  # DTA para validação
├── src/                      # Código da nova feature
│   └── comments/            # Pasta do módulo de comentários
│       ├── models.py        # SQLAlchemy models
│       ├── routes.py        # API routes
│       └── service.py       # Business logic
├── tests/                    # Testes da nova feature
│   ├── unit/
│   │   └── test_comments_models.py
│   └── integration/
│       └── test_comments_api.py
└── docs/                     # Documentação específica
    └── comments.md          # API documentation for comments
```

---

## 📄 Passo 1: Criar DTR (Documento Técnico de Requisito)

### Onde Fica: `.dtc/tasks/dtr-user-comments.md`

Crie o arquivo `DTR-user-comments.md` em `.dtc/tasks/`:

```markdown
# DTR-feature-comments-001 — Sistema de Comentários

## 1. Visão Geral
**Problema**: Usuários atuais reclamam que posts do blog não têm feedback social.  
**Objetivo**: Adicionar sistema de comentários para aumentar engajamento em 30%.

## 2. Requisitos Funcionais (RF)

### RF-001: Criar Comentário
**Descrição**: Usuário pode criar comentário em post específico.  
**Fluxo de uso**:
1. POST /comments/{post_id} com author, content
2. System creates comment in database
3. Returns new comment with id, timestamps

**Acceptance criteria**:
- [ ] Response time < 500ms for p95
- [ ] Comment stored in database immediately
- [ ] Author linked to existing user (email match) or created as guest

### RF-002: Listar Comentários de Post
**Descrição**: GET /comments/{post_id} returns paginated comments.  
**Acceptance criteria**:
- [ ] Pagination page size default 10, max 50
- [ ] Sorted by timestamp descending
- [ ] Cursor-based pagination for large comment sections

### RF-003: Deletar Comentário
**Descrição**: POST /comments/{comment_id}/delete deletes comment.  
**Acceptance criteria**:
- [ ] Soft delete preferred (deleted_at field)
- [ ] Cascade delete or orphaned comments handled gracefully
```

---

## 📄 Passo 2: Criar DTI (Documento Técnico de Implementação)

### Onde Fica: `.dtc/tasks/dti-user-comments.md`

Crie o arquivo `DTI-user-comments.md` em `.dtc/tasks/`:

```markdown
# DTI-feature-comments-001 — Implementação Sistema de Comentários

## 1. Abordagem Técnica Escolhida

**Escolha**: SQLAlchemy ORM com async database access

**Por que esta abordagem?**
1. SQLAlchemy padrão do projeto (de .dtc/context.md)
2. Async support para performance em alta carga
3. Type hints via Pydantic models

## 2. Estrutura de Código

```
src/
└── comments/
    ├── __init__.py          # Module init, exports
    ├── models.py            # SQLAlchemy model definitions
    ├── schemas.py           # Pydantic request/response schemas
    ├── routes.py            # FastAPI endpoint handlers
    └── service.py           # Business logic layer

tests/
└── unit/
    └── test_comments_models.py  # Unit tests for models
```

## 3. Modelos SQLAlchemy (src/comments/models.py)

```python
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ..database.base import Base

class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    author_email: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    post: Mapped["Post"] = relationship("Post", back_populates="comments")
    author: Mapped["User"] = relationship("User", foreign_keys=[author_id])  # Optional
    
    def to_dict(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "author_email": self.author_email,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
        }
```

## 4. Schemas Pydantic (src/comments/schemas.py)

```python
from pydantic import BaseModel, Field
from typing import Optional

class CommentCreate(BaseModel):
    author_email: str = Field(..., min_length=1, max_length=255, description="User email for attribution")
    content: str = Field(..., min_length=1, max_length=10000)

class CommentResponse(BaseModel):
    id: int
    post_id: str
    author_email: str
    content: str
    created_at: str
    
    class Config:
        from_attributes = True  # Eager load from SQLAlchemy models
```

## 5. Routes FastAPI (src/comments/routes.py)

```python
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.session import get_db
from .models import Comment
from .schemas import CommentCreate
from .service import create_comment, get_comments_by_post

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/{post_id}", response_model=CommentResponse)
async def create_comment_endpoint(
    post_id: str,
    comment_data: CommentCreate,
    session: AsyncSession = Depends(get_db),
):
    """Create a new comment on a specific post."""
    async with session.begin():
        comment = await create_comment(session, post_id, comment_data)
    return comment

@router.get("/{post_id}")
async def get_post_comments(
    post_id: str,
    page: int = 1,
    per_page: int = 10,
    session: AsyncSession = Depends(get_db),
):
    """Get paginated comments for a specific post."""
    async with session.begin():
        comments = await get_comments_by_post(
            session, post_id, page=page, per_page=per_page
        )
    return comments
```

## 6. Service Layer (src/comments/service.py)

```python
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.models import Comment, Post
from ..users.models import User
from .schemas import CommentCreate
from datetime import datetime
import secrets

async def create_comment(
    session: AsyncSession,
    post_id: str,
    comment_data: CommentCreate,
):
    """Create a new comment linked to a specific post."""
    
    # Get or create author from email (simple implementation)
    # In production: integrate with existing auth system for identity resolution
    author_email = comment_data.author_email
    
    # Check if existing user by email
    user = await session.get(User, author_email)  # Simplified for example
    
    # Create new comment
    comment = Comment(
        post_id=post_id,
        author_email=author_email,
        content=comment_data.content,
    )
    
    session.add(comment)
    return comment

async def get_comments_by_post(
    session: AsyncSession,
    post_id: str,
    page: int = 1,
    per_page: int = 10,
):
    """Get paginated comments for a post."""
    
    # Calculate offset for cursor-based pagination
    offset = (page - 1) * per_page
    
    # Query with ordering by created_at descending
    comments = await session.execute(
        select(Comment)
        .where(Comment.post_id == post_id)
        .order_by(Comment.created_at.desc())
        .offset(offset)
        .limit(per_page)
    )
    
    return comments.scalars().all()
```

## 7. Database Migration

Adicione migração para tabela de comentários:

```sql
-- migration_002_add_comments_table.sql

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id VARCHAR(255) NOT NULL,
    author_email VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_comments_post (post_id),
    INDEX idx_comments_created (created_at DESC)
);

-- Add foreign key to posts table
ALTER TABLE comments
ADD FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE;
```

## 8. Testes Unitários (tests/unit/test_comments_models.py)

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from alembic.config import Config
from your_app.database.models import Comment, Post

@pytest.fixture
async def async_db():
    """Async database fixture for testing."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    session = AsyncSession(engine, expire_on_commit=False)
    return session

@pytest.mark.asyncio
async def test_create_comment(async_db: AsyncSession):
    """Test creating a new comment on post."""
    
    # Setup
    async with async_db as db:
        post = Post(id="test-post-id", title="Sample Post")
        db.add(post)
        
        from your_app.comments.models import Comment  # Import actual model
        
        comment_data = {"author_email": "user@example.com", "content": "Great post!"}
        
        # Act
        from your_app.comments.service import create_comment
        await create_comment(db, "test-post-id", comment_data)
        
        # Assert
        result = db.execute(select(Comment).where(Comment.post_id == "test-post-id"))
        comments = result.scalars().all()
        
        assert len(comments) >= 1
        assert comments[0].author_email == "user@example.com"
```

## 9. Checklist de Implementação

- [ ] Models SQLAlchemy criados e testados
- [ ] Pydantic schemas definidos
- [ ] FastAPI routes implementadas
- [ ] Service layer com business logic
- [ ] Database migrations aplicadas
- [ ] Unit tests com >80% coverage
- [ ] Documentation em `docs/` completada

---

## 📄 Passo 3: Criar DTA (Documento Técnico de Aceitação)

### Onde Fica: `.dtc/tasks/dta-user-comments.md`

Crie o arquivo `DTA-user-comments.md` em `.dtc/tasks/`:

```markdown
# DTA-feature-comments-001 — Validação Sistema de Comentários

## 1. Critérios de Aceitação (Acceptance Criteria)

### AC-001: Endpoint POST /comments/{post_id}

| Test Case | Expected Behavior | Priority |
|-----------|-------------------|----------|
| Create comment successfully | Returns 201 OK with CommentResponse | P0 |
| Missing required fields | Returns 422 Validation error | P0 |
| Post ID invalid or not found | Should either create standalone comment or return 404 (depends on business logic) | P1 |

### AC-002: Endpoint GET /comments/{post_id}

| Test Case | Expected Behavior | Priority |
|-----------|-------------------|----------|
| Paginated comments returned correctly | Returns page of comments sorted by created_at DESC | P0 |
| Empty comment list for post with no comments | Returns empty array with pagination metadata | P0 |
| Pagination parameters respected | per_page limits response size, page controls offset | P1 |

### AC-003: Performance Requirements (NFR)

| Metric | Target | Acceptance Threshold | Priority |
|--------|--------|---------------------|----------|
| Comment creation latency p95 | <200ms | >500ms fails | P0 |
| Comments list retrieval p95 | <100ms | >300ms warning | P1 |

## 2. Testes Manual de Aceitação

```bash
# Teste manual do endpoint:
curl -X POST "http://localhost:8000/comments/test-post-001" \
  -H "Content-Type: application/json" \
  -d '{"author_email": "user@example.com", "content": "Great post! Thanks for sharing."}'

# Expected response:
{
  "id": 1,
  "post_id": "test-post-001",
  "author_email": "user@example.com",
  "content": "Great post! Thanks for sharing.",
  "created_at": "2024-06-07T12:00:00Z"
}

# Get paginated comments:
curl "http://localhost:8000/comments/test-post-001?page=1&per_page=10"
```

## 3. Checklist Completo de Aceitação

### Unit Tests

- [ ] test_create_comment_success() - Happy path
- [ ] test_create_comment_with_validation_errors() - Missing fields return 422
- [ ] test_get_comments_pagination() - Pagination logic works correctly
- [ ] test_get_comments_sorted_by_created_at_desc() - Sorting order correct
- [ ] test_total_comment_count_in_post() - Total count for metadata

### Integration Tests

- [ ] Full comment create → list cycle with httpx async client
- [ ] Multiple comments on same post returns paginated correctly
- [ ] Concurrent comment creation doesn't cause race conditions

### Performance Tests

- [ ] p95 latency <200ms under simulated production load (100 concurrent users)
- [ ] No memory leaks in comment service after sustained load test

## 4. Aprovações

- [ ] Tech Lead: ___________ Date: ____
- [ ] QA Lead: ___________ Date: ____
```

---

## 📖 Fluxo Completo Demonstrado

```markdown
# Passo 1: Contexto (já existe em .dtc/)
# O projeto minimal-project define arquitetura e stack em .dtc/context.md

# Passo 2: DTR (.dtc/tasks/dtr-user-comments.md)
# Especifica requisitos detalhados da nova feature

# Passo 3: DTI (.dtc/tasks/dti-user-comments.md)  
# Define especificações técnicas de implementação

# Passo 4: Código implementado em src/comments/

# Passo 5: DTA (.dtc/tasks/dta-user-comments.md)
# Define critérios de aceitação para validação

# Iteração: Validar DTA → Implementar → Revisar arquitetura .dtc/
```

---

## 🎯 Conclusão

Este exemplo demonstra o fluxo completo do DTF:

1. **Contexto** já existe em `.dtc/context.md`
2. **Requisito** documentado em `DTR-feature-comments-001.md`
3. **Implementação** especificada em `DTI-feature-comments-001.md`
4. **Validação** definida em `DTA-feature-comments-001.md`

Ao seguir este fluxo, você garante que:
- ✅ Decisões arquiteturais são explícitas antes da implementação
- ✅ Requisitos técnicos são claros para toda a equipe
- ✅ Critérios de aceitação são objetivos e mensuráveis
- ✅ IA pode gerar código alinhado à arquitetura do projeto

---

> **"Documente primeiro, implemente depois. O DTF transforma documentação em artefato de produção."**  
> Referências: [README principal](../../README.md), [`foundation/manifesto.md`](../../foundation/manifesto.md)
