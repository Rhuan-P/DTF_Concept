# Template ADR para API Documentation (Feature Específica)

---

## Contexto e Background

[C: **Motivação** — Por que precisamos documentar esta API?]

[C: **Status Atual** — Como clientes consomem a API hoje?]

[C: **Objetivo** — O que queremos alcançar com esta documentação?]

---

## Proposta Documentação

```yaml
Documentation Type: [OpenAPI/Swagger | Postman Collection | Markdown Pages]
Scope: [Full API | Specific Endpoint Group | New Feature Only]
Maintenance: [Automated from code | Manual updates | Hybrid approach]
Priority: [High | Medium | Low]
```

### Documentation Structure
```markdown
# Nome da API/Roteamento

## Visão Geral
[C: Descrição do propósito desta documentação]

## Endpoints
| Endpoint | Método | Autenticação | Rate Limit |
|----------|--------|--------------|------------|
| /resource | GET | Bearer Token | 100 req/min |
| /resource/:id | POST | None | Unlimited |

### Request/Response Specs
```json
[C: Esquemas JSON de request e response]
```

## Authentication & Authorization
[C: Como os endpoints são autenticados e autorizados]

## Error Handling
[C: Padrões de erro e status codes esperados]
```

---

## Trade-offs

| Consideração | Otimização Ganhada | Compromisso Feito |
|-------------|-------------------|-------------------|
| **Automated Docs** | Sempre atualizadas com código | Complexidade no schema definition |
| **Manual Docs** | Flexibilidade e detalhes ricos | Pode ficar desatualizado |
| **Hybrid** | Melhores dos dois mundos | Maior overhead de manutenção |

---

## Decisões Chave

1. **D: [NOME_DA_DECISAO]**
   - **Descrição:** [Explique a decisão]
   - **Motivo:** [Por que foi tomada]
   - **Alternativas Consideradas:** [O que NÃO escolhemos]

---

## Checklist de Documentação

- [ ] API endpoints listados com métodos corretos
- [ ] Request/response schemas completos e validados
- [ ] Authentication/authorization documentada para cada endpoint
- [ ] Error handling patterns explicados
- [ ] Rate limiting e throttling documentado
- [ ] Versioning strategy definida (se aplicável)
- [ ] Examples fornecidos para casos de uso comuns

---

## Checklist de Decisão

- [ ] A documentação atende aos objetivos principais
- [ ] Trade-offs foram bem compreendidos
- [ ] Alternativas foram consideradas e comparadas
- [ ] Impacto na maintainability está documentado

---

## Referências

[C: **Links para especificações externas ou padrões de indústria]

---

## Conclusão

[C: Resumo das conclusões e próximos passos]
