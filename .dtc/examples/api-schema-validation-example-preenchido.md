# ADR-002: API Schema Validation (Exemplo Preenchido)

**Nota:** Este exemplo demonstra como documentar validação de API schema para feature nova.

---

## Contexto e Background

### Motivação
Validar request/response schemas de endpoint /api/v1/users antes de implementar para garantir:
- Consistência entre frontend e backend
- Contracto bem definido para consumers externos
- Documentation automática (OpenAPI generation)

### Status Atual
Endpoints existem mas sem schema definition clara → documentação desatualizada + consumidores implementando guesswork

### Objetivo
Definir schemas JSON válidos para todos endpoints de user com exemplos reais, depois gerar OpenAPI spec automaticamente.

---

## Proposta Esquema

```yaml
Feature Name: User API Schema Validation
Type: Schema Definition/Validation
Priority: High
Estimated Effort: 2-3 days
Dependencies: 
  - FastAPI JSON validation enabled
  - Pydantic models defined for all endpoints
  - OpenAPI generation configured
Risk Level: Low (non-breaking changes)
```

### Request/Response Schemas Documented

#### GET /api/v1/users/{id}
**Request:**
```json
{
  "pathParams": {
    "id": "guid"
  },
  "queryParams": {
    "fields": ["user,avatar,email", optional],
    "format": ["full|minimal", default: full]
  }
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "name": "User Name",
    "avatar_url": "https://cdn.example.com/avatars/user_123.jpg",
    "created_at": "2026-06-07T10:00:00Z",
    "updated_at": "2026-06-07T14:30:00Z"
  },
  "metadata": {
    "total_users": 150,
    "page": 1,
    "per_page": 20
  }
}
```

#### POST /api/v1/users/{id}/avatar (from earlier upload example)
**Request:**
```json
{
  "pathParams": {
    "user_id": "550e8400-e29b-41d4-a716-446655440000"
  },
  "queryParams": {
    "format": "jpg",
    "quality": 85
  }
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "avatar_url": "https://cdn.example.com/avatars/user_123.jpg",
    "thumbnail_url": "https://cdn.example.com/avatars/thumbnails/user_123_thumb.jpg",
    "file_size_bytes": 524000,
    "original_filename": "avatar_original.jpg",
    "processed_filename": "user_123_512x512_q85.jpg"
  },
  "metadata": {
    "uploaded_at": "2026-06-07T14:30:00Z",
    "processing_time_ms": 1250
  }
}
```

---

## Trade-offs

| Consideração | Otimização Ganhada | Compromisso Feito |
|-------------|-------------------|-------------------|
| **Automated Docs** | Sempre atualizadas com código (via OpenAPI annotations) | Maior strictness no schema definition |
| **Manual Docs** | Flexibilidade e detalhes ricos | Pode ficar desatualizado, prone to errors |
| **Hybrid Approach** | Melhor dos dois mundos | Maior overhead de manutenção inicial |

---

## Decisões Chave

1. **D: Use Pydantic models para validation**
   - **Descrição:** FastAPI auto-generates OpenAPI spec from Pydantic models
   - **Motivo:** Reduz manual maintenance, garante consistency between docs and code
   - **Alternativas Consideradas:** 
     - Manual JSON schema files → Prone to drift between docs and implementation
     - Swagger UI only without validation → No type safety

2. **D: Generate OpenAPI spec from code**
   - **Descrição:** Run `python -m fastapi.generate.openapi` após cada mudança
   - **Motivo:** Always up-to-date, less human error
   - **Alternativas Considered:** 
     - Manual YAML files → High maintenance burden

---

## Checklist de Implementação

- [ ] Pydantic models defined for all request/response types
- [ ] OpenAPI spec generation configured (`fastapi: generate_openapi=True`)
- [ ] Swagger UI available at /docs with interactive testing
- [ ] Postman collection exported from OpenAPI spec
- [ ] Schema validation errors user-friendly (not internal exceptions)
- [ ] Documentation updated with new schemas in /docs

---

## Checklist de Decisão

- [ ] A solução atende aos objetivos principais (schema validation + auto-docs)
- [ ] Trade-offs foram bem compreendidos (automated vs manual docs)
- [ ] Alternativas foram consideradas e comparadas (Pydantic, manual YAML, etc.)
- [ ] Impacto na arquitetura está documentado (FastAPI integration, OpenAPI generation)
- [ ] Planos de rollback estão definidos (revert code changes if validation breaks consumers)

---

## Referências

- [FastAPI JSON Validation with Pydantic](https://fastapi.tiangolo.com/tutorial/request-body/)
- [FastAPI OpenAPI Generation](https://fastapi.tiangolo.com/tutorial/openapi/)
- [OpenAPI Specification v3.0](https://swagger.io/specification/v3/)

---

## Conclusão

Schema validation implementada via Pydantic com:
- Auto-generated OpenAPI spec at /openapi.json
- Swagger UI interactive testing at /docs
- Postman collection auto-exported from spec
- User-friendly validation errors (not internal exceptions)

Próximos passos:
1. Migrate existing manual schemas to Pydantic models
2. Update all consumers with new validated schemas
3. Set up CI/CD check to ensure OpenAPI spec validity on each push
