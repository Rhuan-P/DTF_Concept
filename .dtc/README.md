# .dtc/ — Decision Template Collections

Coleção de templates, guidelines e exemplos para documentar **Decision Template Architecture** (DTA) durante o desenvolvimento do DTF.

---

## 📚 Estrutura

```
.dtc/
├── README.md              # Este arquivo — documentação geral
├── BEST-PRACTICES.md     # Guidelines e melhores práticas de uso
├── templates/           # Templates vazios para diferentes tipos de decisão
│   ├── 001-upload-feature-generic.md    # Template genérico para upload features
│   ├── 002-api-validation-choice.md     # Template específico: validação de API
│   └── 003-upload-feature.md          # Template específico: upload feature completo
├── examples/           # Exemplos preenchidos para referência
│   ├── context-md-exemplo-preenchido.md
│   ├── DTA-template-exemplo-preenchido.md
│   └── DTA-template-upload-generico-exemplo-preenchido.md  *(novo)*
└── decisions/         # Decisões documentadas usando os templates acima
    ├── ADR-XXX-decricao.md     # (criar conforme necessário)
    └── templates/             # Templates específicos para decisões
        └── [00X]-*.md
```

---

## 🎯 Quando Usar

Use arquivos em `.dtc/` quando:

1. **Documentando decisão técnica** → Crie ADR em `decisions/` usando template de `templates/`
2. **Precisando de referência rápida** → Consulte exemplos em `examples/`
3. **Criando nova feature complexa** → Use guidelines em `BEST-PRACTICES.md`

---

## 🚀 Quick Start

### Criando Novo ADR

```bash
# 1. Identificar tipo de decisão
#    - API validation? → Use template 002
#    - Upload feature? → Use template 003 ou genérico 001
#    - Outro? → Use genérico (001) e adapte

# 2. Copiar template
cp .dtc/templates/[TEMPLATE].md /c/Users/rhuan/DTF_Concept/.dtc/decisions/ADR-XXX-decision.md

# 3. Preencher com detalhes específicos
#    - Remova placeholders [CURLASCOLETAS]
#    - Adicione contexto, decisão, trade-offs
#    - Atualize status: [Draft] → [Review] → [Approved]

# 4. Review por stakeholder (opcional)
#    - Verifique checklist de decisão
#    - Garanta trade-offs compreendidos

# 5. Commit
git add .dtc/decisions/ADR-XXX-decision.md
```

---

## 📋 Checklist de Qualidade

Para cada ADR criado:

- [ ] Template apropriado escolhido (ou genérico adaptado)
- [ ] Todas seções preenchidas (sem `[CURLASCOLETAS]` restantes)
- [ ] Trade-offs documentados claramente
- [ ] Checklist de decisão assinado
- [ ] Status atualizado ([Draft] → [Review] → [Approved])

---

## 🧹 Manutenção

### Adicionando Novo Template
1. Identifique gap (qual tipo de decisão não tem template?)
2. Crie com numeração sequencial (001, 002, 003...)
3. Atualize `templates/` e `examples/README.md` se necessário

### Mantendo Exemplos Relevantes
- Remova exemplos obsoletos de tecnologias deprecated
- Atualize exemplos com contextos atuais do projeto
- Mantenha máximo 10 exemplos mais relevantes (evite bloat)

---

## 📊 Diferença: Template vs Exemplo

| Aspecto | Template (`templates/`) | Exemplo (`examples/`) |
|---------|------------------------|----------------------|
| **Conteúdo** | Estrutura vazia com placeholders | Dados reais e concretos |
| **Uso** | Durante processo de decisão | Para referência pós-decisão/onboarding |
| **Estado** | `[Template]` por padrão | Preenchido/Ativo |
| **Numeração** | Sequencial (001, 002...) | Descritivo (`api-validation-example.md`) |

---

## 🚦 Workflow Recomendado

```
Identificar necessidade → Escolher template → Preencher ADR → Review → 
Publicar em decisions/ → (Opcional) Criar exemplo preenchido
```

---

## 🔗 Links Relacionados
- [Best Practices](./BEST-PRACTICES.md) — Guidelines detalhadas
- [Templates](./templates/) — Escolha template apropriado
- [Examples](./examples/) — Referências rápidas

---

**Última atualização:** 2026-06-XX  
**Versão:** 1.0.0
