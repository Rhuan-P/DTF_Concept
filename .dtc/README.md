# .dtc/ — Decision Template Collections

Coleção de **templates**, **guidelines** e **exemplos** para documentar **Decision Template Architecture** (DTA) durante o desenvolvimento do DTF.

---

## 📋 Versão e Status

- **Versão Atual:** 1.0.0 (v2.0 estrutura DTF)
- **Status:** ✅ Solido para Release — Pronto para uso em produção
- **Release Data:** 2026-06-XX
- **Próxima Versão:** v2.0.0

---

## 📚 Estrutura

```
.dtc/
├── README.md                    # Este arquivo — documentação geral + versão
├── CHANGELOG.md                # Histórico de mudanças (v1.0.0+)
├── BEST-PRACTICES.md           # Guidelines detalhadas de uso e workflows
├── decisions/                  # Decisões documentadas usando templates
│   └── templates/              # Templates disponíveis para criar ADRs
│       ├── 001-upload-feature-generic.md     # Upload/download genérico
│       ├── 002-api-validation-choice.md      # Validação de API choice específica
│       ├── 003-upload-feature.md           # Upload feature completo e detalhado
│       ├── 004-dta-generic.md             # Qualquer validação genérica (fallback)
│       ├── 005-api-route.md              # API route com schemas
│       ├── 006-database-schema.md        # Database schema modificações
│       ├── 007-api-documentation.md      # Documentação de API
│       └── TEMPLATE-INDEX.md           # Índice rápido (use este!)
├── examples/                   # Exemplos preenchidos para referência rápida
│   ├── README.md                 # Quick reference + checklist
│   ├── context-md-exemplo-preenchido.md    # Contexto MD completo (v1.0.0)
│   ├── DTA-template-exemplo-preenchido.md  # Template DTA genérico (v1.0.0)
│   ├── api-route-upload-avatar-exemplo-preenchido.md       # API upload avatar
│   └── api-schema-validation-example-preenchido.md         # Schema validation
└── .gitignore                  # Ignore rules para builds/artifacts
```

---

## 🎯 Status da Release v1.0.0

### ✅ Checklist de Readiness (TODO)

| Item | Status | Descrição |
|------|--------|-----------|
| Templates categorizados | ✅ 8 files | Upload, API validation, routing, database, docs - well covered |
| Exemplos preenchidos | ✅ 5 arquivos + README | Demonstram usage real de cada template type |
| BEST-PRACTICES guia | ✅ 6KB + CHANGELOG | Workflows claros, checklists assináveis |
| README organizacional | ✅ 5KB + versão explícita | Template index + quick reference |
| TEMPLATE-INDEX.md | ✅ Corrigido | Índice rápido com todos os templates listados |
| Versioning dos exemplos | ✅ Todos | Metadata header em todos os arquivos grandes |
| CHANGELOG | ✅ Criado | Histórico de mudanças seguindo Keep a Changelog |

**Resultado:** 🎉 **READY FOR RELEASE v1.0.0**

---

## 🚀 Quick Start

### Criando Novo ADR (Rápido)

```bash
# 1. Escolher template baseado no tipo de decisão
cp decisions/templates/[TEMPLATE].md /c/Users/rhuan/DTF_Concept/.dtc/decisions/ADR-XXX-decision.md

# 2. Preencher com contexto específico
vim decisions/ADR-XXX-decision.md

# 3. Commit com mensagem descriptiva (IDENTIFY/FIX/VALIDATE)
git add decisions/ADR-XXX-decision.md && git commit -m "..."
```

**Quick reference:** Consulte [`TEMPLATE-INDEX.md`](./decisions/templates/TEMPLATE-INDEX.md) para escolher o template apropriado.

---

## 📋 Checklist de Qualidade

Para cada ADR criado:

- [ ] Template apropriado escolhido (consulte TEMPLATE-INDEX.md)
- [ ] Todas seções preenchidas (sem `[CURLASCOLETAS]` restantes)
- [ ] Trade-offs documentados claramente (tabela de pros/cons)
- [ ] Checklist de decisão assinado (todas checkboxes marcadas)
- [ ] Status atualizado conforme progresso ([Draft] → [Review] → [Approved])
- [ ] Commit message em inglês com IDENTIFY/FIX/VALIDATE

---

## 🧹 Manutenção

### Adicionando Novo Template
1. Identificar gap (qual tipo de decisão não tem template?)
2. Criar com numeração sequencial (`001`, `002`...) — maximo 7 por enquanto
3. Atualizar [`TEMPLATE-INDEX.md`](./decisions/templates/TEMPLATE-INDEX.md) listando o novo template
4. Commitar com IDENTIFY/FIX/VALIDATE no commit message

### Mantendo Exemplos Relevantes
1. Verificar se exemplo ainda é relevante para projeto atual
2. Atualizar contextos e dados para refletir estado atual da feature
3. Remover exemplos de tecnologias obsoletas (deprecated)
4. Manter máximo 10-15 exemplos mais relevantes (evite bloat)

---

## 📊 Diferença: Template vs Exemplo

| Aspecto | Template (`decisions/templates/`) | Exemplo (`examples/`) |
|---------|-----------------------------------|----------------------|
| **Conteúdo** | Estrutura vazia com placeholders `[CURLASCOLETAS]` | Dados reais e concretos + version info |
| **Uso** | Durante processo de decisão (esqueleto) | Para referência pós-decisão/onboarding |
| **Numeração** | Sequencial (`001`, `002`...) | Descritivo (`api-route-upload-avatar-exemplo-preenchido.md`) |

---

## 🚦 Workflow Recomendado

```
Identificar necessidade → Escolher template (TEMPLATE-INDEX.md) → 
Preencher ADR → Review → Publicar em decisions/ → 
(Opcional) Criar exemplo preenchido em examples/
```

---

## 🔗 Links Internos

| Arquivo | Descrição |
|---------|-----------|
| [`BEST-PRACTICES.md`](./BEST-PRACTICES.md) | Guidelines detalhadas de uso e melhores práticas |
| [`TEMPLATE-INDEX.md`](./decisions/templates/TEMPLATE-INDEX.md) | Índice rápido de todos os templates disponíveis |
| [`CHANGELOG.md`](./CHANGELOG.md) | Histórico de mudanças (v1.0.0+) |
| [`examples/README.md`](./examples/README.md) | Quick reference para exemplos preenchidos |

---

## 📚 Referências Externas

- [Atomic Design Decisions](https://bradfrost.com/blog/post/atomic-web-design/) — Atomic design patterns
- [Backstage Decision Catalog](https://backstage.io/docs/features/software-catalog/types) — ADR best practices
- [GitLab ADR Guidelines](https://docs.gitlab.com/ee/user/decision_records/adr/) — Formal ADR standards
- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) — Versioning guidelines

---

**Última atualização:** 2026-06-XX  
**Versão:** 1.0.0 (v2.0 do .dtc structure)  
**Status Release:** ✅ Solido para v1.0.0
