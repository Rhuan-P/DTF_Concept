# Best Practices para `.dtc/` (Decision Template Collections)

## 📋 Visão Geral
O diretório `.dtc/` serve como coleção de templates e guidelines para documentar decisões técnicas durante o desenvolvimento do DTF (Design Thinking First).

---

## 🗂️ Estrutura Recomendada

```
.dtac/
├── README.md                    # Introdução geral ao .dtc/
├── BEST-PRACTICES.md           # Estas instruções
├── templates/                  # Templates de ADR para diferentes tipos de decisões
│   ├── 001-generic.md          # Template genérico para qualquer decisão
│   ├── 002-api-validation-choice.md  # Template específico para validação de API
│   ├── 003-upload-feature.md   # Template para features de upload
│   └── ...                     # Mais templates conforme necessário
├── examples/                   # Exemplos preenchidos para referência
│   ├── context-md-exemplo-preenchido.md
│   ├── DTA-template-exemplo-preenchido.md
│   └── ...
└── decisions/                 # Decisões documentadas usando os templates acima
    └── ADR-XXX-decricao.md     # Cada ADR deve seguir o template apropriado
```

---

## 📝 Criando Novos ADRs

### Escolher o Template Correto

1. **Decisão genérica/qualquer:** Use `001-generic.md`
2. **Validação de API específica:** Use `002-api-validation-choice.md`
3. **Feature de upload/download:** Use `003-upload-feature.md`
4. **Caso não existir template adequado:** Copie o genérico e adapte

### Checklist ao Criar ADR

- [ ] Escolhi o template mais apropriado para este tipo de decisão
- [ ] Preenchi todas as seções do template (não omita `[CURLASCOLETAS]`)
- [ ] Usei a numeração sequencial (001, 002, 003...) para manter ordem
- [ ] Adicionei data de criação e versão
- [ ] Review por pelo menos uma pessoa antes de marcar como "Approved"

---

## 🚀 Guidelines Específicas

### Para `templates/`
- Mantenha templates **vazios** (apenas estrutura) para reuso
- Numere sequencialmente com padding (001, 002, 003...)
- Use prefixos semânticos no nome: `generic`, `api`, `upload`, etc.
- Documente claramente quando um template é obrigatório vs opcional

### Para `examples/`
- Exemplos devem ser **preenchidos** com dados reais (não placeholders)
- Inclua comentários explicando pontos importantes
- Use nomes de arquivo descritivos: `api-validation-example.md`, não `template1.md`
- Mantenha exemplos atualizados e relevantes

### Para `decisions/`
- Numere ADRs sequencialmente (ADR-001, ADR-002...)
- Cada ADR deve ter data de criação e autor
- Use tags: `[Draft]`, `[Review]`, `[Approved]`, `[Superseded]`
- Link para o template usado no cabeçalho do ADR

---

## 🧹 Manutenção

### Quando Adicionar Novo Template
1. Identifique gap na cobertura (qual tipo de decisão falta template?)
2. Crie template com numeração sequencial adequada
3. Atualize README.md listando todos os templates disponíveis
4. Adicione exemplos preenchidos se aplicável

### Quando Atualizar Exemplo
1. Verifique se exemplo ainda é relevante para o projeto
2. Atualize dados e contextos para refletir estado atual
3. Remova exemplos de tecnologias obsoletas
4. Mantenha máximo 5-10 exemplos mais relevantes (evite bloat)

---

## 🔍 Exemplos Reais vs Templates

| Tipo | Quando Usar | Características |
|------|-------------|-----------------|
| **Template** (`templates/`) | Durante processo de decisão, antes da escolha final | Vazio, placeholders `[CURLASCOLETAS]`, estrutura |
| **Exemplo** (`examples/`) | Para referência após decisão tomada ou para onboarding | Preenchido, dados reais, exemplos concretos |

**Importante:** Não confunda os dois! Templates são **esqueletos**, exemplos são **casos reais**.

---

## 📊 Checklist de Qualidade

Para ADRs em `decisions/`:
- [ ] Segue formato do template escolhido (ou template genérico como fallback)
- [ ] Todas as seções preenchidas (sem `[CURLASCOLETAS]` restantes)
- [ ] Trade-offs documentados claramente
- [ ] Checklist de decisão assinado
- [ ] Link para template usado no cabeçalho

Para Templates em `templates/`:
- [ ] Estrutura clara e bem organizada
- [ ] Instruções de uso no topo do template
- [ ] Placeholder comments explicativos `[CURLASCOLETAS]`
- [ ] Numeração sequencial (001, 002...)

---

## 🚦 Workflow Recomendado

```
1. Identificar necessidade de decisão → Escolher/template adequado
2. Criar ADR Draft usando template escolhido
3. Preencher com detalhes específicos do caso
4. Review por stakeholders
5. Atualizar status para [Review] ou [Approved]
6. Adicionar a `decisions/` 
7. (Opcional) Criar exemplo preenchido em `examples/` para referência futura
```

---

## 📚 Referências
- [Atomic Design](https://bradfrost.com/blog/post/atomic-web-design/) - Atomic design decisions
- [Backstage](https://backstage.io/docs/features/software-catalog/types) - Decision catalog patterns
- [GitLab Decision Records](https://docs.gitlab.com/ee/user/decision_records/adr/) - ADR best practices

---

**Última atualização:** 2026-06-XX
**Versão:** 1.0.0
