# Índice de Templates para .dtc/ (Decision Template Collections)

Este documento lista todos os templates disponíveis no diretório `.dtc/decisions/templates/`. Escolha o template mais apropriado para seu caso.

---

## 📋 Templates Disponíveis

| Num | Nome | Tipo | Quando Usar |
|-----|------|------|-------------|
| **001** | `upload-feature-generic.md` | ADR | Feature de upload/download genérica (placeholder-heavy) |
| **002** | `api-validation-choice.md` | ADR | Validação específica de API choice |
| **003** | `upload-feature.md` | ADR | Upload feature completo e detalhado |
| **004** | `dta-generic.md` | DTA | Qualquer feature de validação genérica |
| **005** | `api-route.md` | ADR | API route específica com schemas |
| **006** | `database-schema.md` | ADR | Modificações/adicionais de schema de banco |
| **007** | `api-documentation.md` | ADR | Documentação de API (OpenAPI/Postman/etc) |

---

## 🎯 Guia de Escolha Rápida

### Para Features de Upload/Download:
- Precisa ser **simples/rápida**? → Use **001** `upload-feature-generic.md`
- Quer exemplo completo e detalhado? → Use **003** `upload-feature.md`

### Para Validação de API:
- É sobre validação específica de choice de endpoint? → Use **002** `api-validation-choice.md`
- É feature genérica de qualquer tipo? → Use **004** `dta-generic.md`

### Para Documentação/Schema/API:
- Criando nova API route? → Use **005** `api-route.md`
- Modificando database schema? → Use **006** `database-schema.md`
- Melhorando documentação de API? → Use **007** `api-documentation.md`

---

## 📚 Workflow Recomendado

```
1. Identificar tipo de decisão (upload, validation, api, schema, docs)
2. Escolher template mais específico (se houver) ou genérico (fallback)
3. Copiar para decisions/: ADR-XXX-[decisao].md
4. Preencher [CURLASCOLETAS] com dados do seu caso
5. Review e publicam
```

---

## 🔀 Templates Genéricos como Fallback

Se nenhum template específico atender ao seu caso, use **001** `upload-feature-generic.md` ou **004** `dta-generic.md` como base e adapte conforme necessário.

---

## 📊 Comparação Rápida

| Feature | Template Específico | Template Genérico Fallback |
|---------|---------------------|---------------------------|
| Upload/Download | 003, 001 | 004 (dta-generic) |
| API Validation | 002 | 004 (dta-generic) |
| Any Feature | - | 004 (dta-generic) |

---

## 📝 Template Genérico Padrão

**Recomendação:** Se em dúvida, use **004** `dta-generic.md` — cobre cenários gerais bem e pode ser adaptado.

---

## 🔗 Relacionado
- [BEST-PRACTICES](../BEST-PRACTICES.md) — Guidelines detalhadas de uso
- [examples/](../examples/) — Exemplos preenchidos para referência
- [README](../README.md) — Documentação geral do .dtc/
