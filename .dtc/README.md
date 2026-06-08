# .dtc/ — Decision Template Collections

Coleção de **templates**, **guidelines** e **exemplos** para documentar **Decision Template Architecture** (DTA) durante o desenvolvimento do DTF.

---

## 📚 Estrutura

```
.dtc/
├── README.md                    # Este arquivo — documentação geral
├── BEST-PRACTICES.md           # Guidelines detalhadas de uso
├── TEMPLATE-INDEX.md           # Índice rápido de todos os templates
├── decisions/                  #决 decisões documentadas usando templates
│   └── templates/              # Templates disponíveis para criar ADRs
│       ├── 001-upload-feature-generic.md     # Upload/download genérico (placeholder)
│       ├── 002-api-validation-choice.md      # Validação de API choice específica
│       ├── 003-upload-feature.md           # Upload feature completo e detalhado
│       ├── 004-dta-generic.md             # Qualquer validação genérica (fallback)
│       ├── 005-api-route.md              # API route com schemas
│       ├── 006-database-schema.md        # Schema de banco modificações
│       └── 007-api-documentation.md      # Documentação de API (OpenAPI/Postman)
├── examples/                   # Exemplos preenchidos para referência rápida
│   ├── context-md-exemplo-preenchido.md    # Context MD exemplo completo
│   ├── DTA-template-upload-generico-exemplo-preenchido.md  # Upload upload exemplo
│   └── README.md                 # Quick reference do exemplos/
└── decisions/                  # Decisões documentadas (criar conforme necessário)
```

---

## 🎯 Quando Usar

Use arquivos em `.dtc/` quando:

1. **Documentando decisão técnica** → Crie ADR em `decisions/` usando template de `decisions/templates/`
2. **Precisando de referência rápida** → Consulte exemplos em `examples/` ou [`TEMPLATE-INDEX.md`](./TEMPLATE-INDEX.md)
3. **Criando nova feature complexa** → Use guidelines em [`BEST-PRACTICES.md`](./BEST-PRACTICES.md)

---

## 🚀 Quick Start

### Criando Novo ADR (Rápido)

```bash
# 1. Escolher template baseado no tipo de decisão
cp decisions/templates/[TEMPLATE].md /c/Users/rhuan/DTF_Concept/.dtc/decisions/ADR-XXX-decision.md

# 2. Preencher com contexto específico
vim decisions/ADR-XXX-decision.md

# 3. Commit com mensagem descriptiva
git add decisions/ADR-XXX-decision.md
```

**Quick reference:** Consulte [`TEMPLATE-INDEX.md`](./decisions/templates/TEMPLATE-INDEX.md) para escolher o template apropriado.

---

## 📋 Checklist de Qualidade

Para cada ADR criado:

- [ ] Template apropriado escolhido (ou genérico adaptado como fallback)
- [ ] Todas seções preenchidas (sem `[CURLASCOLETAS]` restantes)
- [ ] Trade-offs documentados claramente
- [ ] Checklist de decisão assinado
- [ ] Status atualizado ([Draft] → [Review] → [Approved])

---

## 🧹 Manutenção

### Adicionando Novo Template
1. Identifique gap (qual tipo de decisão não tem template?)
2. Crie com numeração sequencial (`001`, `002`, `003`...)
3. Atualize [`TEMPLATE-INDEX.md`](./decisions/templates/TEMPLATE-INDEX.md) listando o novo template

### Mantendo Exemplos Relevantes
- Remova exemplos obsoletos de tecnologias deprecated
- Atualize exemplos com contextos atuais do projeto
- Mantenha máximo 10 exemplos mais relevantes (evite bloat)

---

## 📊 Diferença: Template vs Exemplo

| Aspecto | Template (`decisions/templates/`) | Exemplo (`examples/`) |
|---------|-----------------------------------|----------------------|
| **Conteúdo** | Estrutura vazia com placeholders `[CURLASCOLETAS]` | Dados reais e concretos |
| **Uso** | Durante processo de decisão (esqueleto) | Para referência pós-decisão/onboarding |
| **Numeração** | Sequencial (`001`, `002`...) | Descritivo (`api-validation-example.md`) |

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
| [`examples/README.md`](./examples/README.md) | Quick reference para exemplos preenchidos |

---

**Última atualização:** 2026-06-XX  
**Versão:** 1.0.1 (Melhoria v2.0 com templates categorizados)
