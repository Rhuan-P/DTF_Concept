# Template ADR para API Route (Feature Específica)

---

## Contexto e Background

[C: **Motivação** — Por que esta route é necessária?]

[C: **Status Atual** — Como a aplicação lida com [funcionalidade] hoje?]

[C: **Objetivo** — O que queremos alcançar com esta route?]

---

## Proposta Técnica

```yaml
Route Name: [NOME_DO_ENDPOINT]
Path: [/path/to/resource]
Method: [GET | POST | PUT | DELETE | PATCH]
Authentication: [OAuth | API Key | JWT | Basic Auth | No Auth]
Authorization Scope: [Full | Read-only | Limited | Admin-only]
```

### Payload Schema (Request)
```json
{
  "pathParams": {
    // [Descrição dos path parameters se houver]
  },
  "queryParams": {
    // [Descrição dos query parameters]
  },
  "body": {
    // [Esquema JSON do body ou omitir para GET/DELETE]
  }
}
```

### Response Schema (Response)
```json
{
  "success": true,
  "data": {
    // [Estrutura dos dados de sucesso]
  },
  "metadata": {
    // [Cabeçalhos, pagination, etc.]
  }
}
```

### Error Handling
| Status Code | Quando Ocorre | Response Body |
|-------------|---------------|---------------|
| 400 | Request validation failed | `{ error: string, details?: array }` |
| 401 | Unauthorized (missing/bad token) | `{ error: "Unauthorized" }` |
| 403 | Forbidden (insufficient scope) | `{ error: "Forbidden" }` |
| 404 | Resource not found | `{ error: "Not Found", id?: string }` |
| 500 | Server error | `{ error: string, code?: string }` |

---

## Trade-offs

| Consideração | Otimização Ganhada | Compromisso Feito |
|-------------|-------------------|-------------------|
| **Performance** | Caching via CDN/Redis para GETs | Maior overhead de setup para cache invalidation |
| **Simplicidade** | Single endpoint com query params | Menos granularidade no routing |
| **Flexibilidade** | Multiple endpoints por resource | Mais boilerplate e potential for duplication |

---

## Decisões Chave

1. **D: [NOME_DA_DECISAO]**
   - **Descrição:** [Explique a decisão]
   - **Motivo:** [Por que foi tomada]
   - **Alternativas Consideradas:** [O que NÃO escolhemos]

2. **D: [OUTRA_DECISAO]**
   - **Descrição:** [Explique a decisão]
   - **Motivo:** [Por que foi tomada]
   - **Alternativas Consideradas:** [O que NÃO escolhemos]

---

## Checklist de Implementação

- [ ] Schema validation definida no request handler
- [ ] Error handling implementado para todos casos (4xx/5xx)
- [ ] Response schema consistente com especificação
- [ ] Rate limiting configurado para endpoint sensível
- [ ] Logging adequado em success/error paths
- [ ] Documentation atualizada (OpenAPI/Swagger)
- [ ] Tests escritos e passando

---

## Checklist de Decisão

- [ ] A solução atende aos objetivos principais
- [ ] Trade-offs foram bem compreendidos
- [ ] Alternativas foram consideradas e comparadas
- [ ] Impacto na arquitetura está documentado
- [ ] Planos de rollback estão definidos (se aplicável)

---

## Referências

[C: **Links para documentação relevante ou pesquisas]

---

## Conclusão

[C: Resumo das conclusões e próximos passos]
