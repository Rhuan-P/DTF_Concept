# ADR-001: Upload Avatar API Route (Exemplo Preenchido)

**Nota:** Este é um exemplo preenchido para referência rápida. Use como base quando criar nova API route de upload.

---

## Contexto e Background

### Motivação
Implementar endpoint específico para upload de avatar de usuários, suportando:
- File picker (mobile legacy fallback)
- Drag-and-drop (desktop otimizado)
- Compressão automática (512x512px, quality 85%)

### Status Atual
Upload atual é manual sem compressão, leva tempo e não suporta cancelamento.

### Objetivo
Definir endpoint /api/v1/users/{id}/avatar/upload com validação completa de arquivo + preview em tempo real.

---

## Proposta Esquema

```yaml
Route Name: Upload Avatar API
Path: /api/v1/users/{user_id}/avatar/upload
Method: POST
Authentication: JWT Bearer Token
Authorization Scope: User Profile Write
Priority: High
Estimated Effort: 3-5 days
Risk Level: Medium (requires file handling + compression)
```

### Request Schema
```json
{
  "pathParams": {
    "user_id": "uuid v4",
    "description": "Identifier of the user uploading avatar"
  },
  "queryParams": {
    "format": ["png|jpg|webp"],
    "quality": [1-100, default: 85]
  },
  "body": {} // FormData/Multipart upload - file in 'avatar' field
}
```

### Response Schema (Success)
```json
{
  "success": true,
  "data": {
    "avatar_url": "https://cdn.example.com/avatars/user123.jpg",
    "thumbnail_url": "https://cdn.example.com/avatars/thumbnails/user123_thumb.jpg",
    "file_size_bytes": 524000,
    "original_filename": "avatar_original.jpg",
    "processed_filename": "user123_512x512_q85.jpg"
  },
  "metadata": {
    "uploaded_at": "2026-06-07T14:30:00Z",
    "processing_time_ms": 1250
  }
}
```

### Response Schema (Error)
```json
{
  "success": false,
  "error": {
    "code": "INVALID_FILE_SIZE",
    "message": "Avatar file too large. Maximum allowed is 5MB.",
    "details": [
      {"field": "avatar", "message": "File size exceeds 5MB limit"}
    ]
  }
}
```

### Error Handling Matrix
| Status | Quando Ocorre | Response Body |
|--------|---------------|---------------|
| 201 | Upload bem-sucedido | See success schema above |
| 400 | File size/type invalid | `{"error": "INVALID_FILE", "details": [...]}` |
| 401 | Unauthorized (bad/bad token) | `{"error": "Unauthorized"}` |
| 403 | Insufficient permissions | `{"error": "Forbidden"}` |
| 404 | User not found | `{"error": "Not Found", "user_id": "..."} |
| 500 | Server error (storage full, etc.) | `{"error": "Internal Error", "code": "..."}` |

---

## Trade-offs

| Consideração | Otimização Ganhada | Compromisso Feito |
|-------------|-------------------|-------------------|
| **Performance** | Compressão no upload → menor uso CDN | Maior CPU durante upload |
| **Simplicidade** | Single endpoint com query params | Menos granularidade no routing |
| **Flexibilidade** | Suporte múltiplos formatos (png/jpg/webp) | Maior complexity na validation |

---

## Decisões Chave

1. **D: Compressão automática no upload**
   - **Descrição:** File processado no servidor antes de armazenamento CDN (512x512px, quality 85%)
   - **Motivo:** Reduz bandwidth e improves load times para mobile users
   - **Alternativas Consideradas:** 
     - Upload bruto sem compressão → Pior performance, mais storage
     - Client-side compression only → Inconsistent results across browsers

2. **D: Rate limiting de 10 uploads/min por user**
   - **Descrição:** Throttling prevent upload storms ou brute force
   - **Motivo:** Protect against storage exhaustion and abuse
   - **Alternativas Considered:**
     - No rate limiting → Risk of storage exhaustion
     - Strict 1 upload/hour → User experience suffers

---

## Checklist de Implementação

- [ ] File size validation (< 5MB) antes de processamento
- [ ] MIME type detection e whitelist (.png, .jpg, .webp)
- [ ] Async processing para uploads (offload to job queue se necessário)
- [ ] Rollback plan: old avatar preserved até confirmação do novo upload
- [ ] CDN cache invalidation configurado para nova rota
- [ ] Logging adequado: success errors com user_id file info
- [ ] Response schemas consistentes com especificação acima

---

## Checklist de Decisão

- [ ] A solução atende aos objetivos principais (upload rápido + preview)
- [ ] Trade-offs foram bem compreendidos (performance vs storage costs)
- [ ] Alternativas foram consideradas e comparadas (compression strategies, rate limits)
- [ ] Impacto na arquitetura está documentado (CDN invalidation, job queue)
- [ ] Planos de rollback estão definidos (preserve old avatar até confirmação)

---

## Referências

- [AWS S3 Upload API documentation](https://aws.amazon.com/s3/upload-api/)
- [FastAPI File Upload Examples](https://fastapi.tiangolo.com/tutorial/files/)
- [Best practices for file uploads](https://www.smashingmagazine.com/2015/07/file-uploads-best-practices/)

---

## Conclusão

Endpoint de upload de avatar implementado com:
- Compressão automática (512x512px, quality 85%)
- File validation (size, type)
- Rate limiting (10 uploads/min/user)
- Async processing para performance
- Comprehensive error handling

Próximos passos:
1. Implementar service layer em backend
2. Configurar CDN storage + invalidation
3. Write integration tests com diferentes file types/sizes
4. Documentation atualizada no OpenAPI spec
