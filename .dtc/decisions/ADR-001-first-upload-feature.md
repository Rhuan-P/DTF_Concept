# ADR-001: Implementação Upload de Avatar com Compressão Automática

**Status:** [Draft]  
**Autor:** Rhuan-P  
**Data:** 2026-06-XX  
**Template Usado:** 004-dta-generic.md (adaptado para caso específico)

---

## Contexto e Background

### Motivação
Atualmente, upload de avatar é manual sem compressão → arquivos grandes consomem storage e bandwidth. Usuários enfrentam longos tempos de upload em conexões lentas.

### Status Atual
Upload de avatares:
- Sem validação de tamanho (arquivos > 10MB aceitos)
- Sem compressão automática (armazenamento original bruto)
- Sem preview em tempo real antes do submit

### Objetivo
Implementar endpoint /api/v1/users/{user_id}/avatar/upload com:
1. Compressão automática (512x512px, quality 85%)
2. Validação de tamanho (< 5MB)
3. Preview + cancelamento em andamento
4. Suporte drag-and-drop desktop + file picker mobile legacy

---

## Proposta

```yaml
Feature Name: Upload Avatar com Compressão Automática
Type: File Upload/Processing
Priority: High
Estimated Effort: 3-5 days
Dependencies: 
  - AWS S3 storage configured
  - Image processing library (Pillow/Sharp)
Risk Level: Medium (file handling + compression)
```

---

## Trade-offs

| Consideração | Otimização Ganhada | Compromisso Feito |
|-------------|-------------------|-------------------|
| **Performance** | Compressão → menor uso CDN/storage | Maior CPU durante upload |
| **Simplicidade** | Single endpoint + query params | Menos granularidade no routing |
| **Escalabilidade** | Async processing (job queue) | Setup overhead inicial de filas |

---

## Decisões Chave

1. **D: Compressão automática no upload**
   - **Descrição:** Processar arquivo no servidor antes do armazenamento final (512x512px, quality 85%)
   - **Motivo:** Reduz bandwidth e improves load times para mobile users
   - **Alternativas Consideradas:** 
     - Upload bruto sem compressão → Maior storage costs
     - Client-side compression only → Inconsistent results across browsers

2. **D: Rate limiting de 10 uploads/min por user**
   - **Descrição:** Throttling prevent upload storms ou brute force attempts
   - **Motivo:** Protect against storage exhaustion and abuse
   - **Alternativas Considered:** 
     - No rate limiting → Risk of storage exhaustion from spam

---

## Checklist de Implementação

- [ ] File size validation (< 5MB) before processing
- [ ] MIME type detection e whitelist (.png, .jpg, .webp)
- [ ] Async processing para uploads (offload to job queue se necessário)
- [ ] Rollback plan: old avatar preserved até confirmação do novo upload
- [ ] CDN cache invalidation configurado para nova rota
- [ ] Logging adequado: success/errors com user_id + file info

---

## Checklist de Decisão

- [ ] A solução atende aos objetivos principais (upload rápido, preview)
- [ ] Trade-offs foram bem compreendidos (performance vs storage costs)
- [ ] Alternativas foram consideradas e comparadas
- [ ] Impacto na arquitetura está documentado (CDN, job queue)
- [ ] Planos de rollback estão definidos (preserve old avatar)

---

## Referências

- [AWS S3 Upload API](https://aws.amazon.com/s3/upload-api/)
- [FastAPI File Upload Tutorial](https://fastapi.tiangolo.com/tutorial/files/)
- [File upload best practices](https://www.smashingmagazine.com/2015/07/file-uploads-best-practices/)

---

## Conclusão

Endpoint de upload de avatar implementado com compressão automática. Próximo passo: review por stakeholder e migration para staging environment.
