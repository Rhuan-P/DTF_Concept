# Arquitetura dos Documentos da Metodologia DTF

Esta documentação descreve a arquitetura dos documentos técnicos (DTC, DTR, DTI, DTA) e como eles se relacionam no fluxo de engenharia do DTF.

---

## Visão Geral do Sistema de Documentos

```
DTF Documents Architecture
├── Contexto (.dtc/context.md)
│   ├── Visão Geral → Propósito, escopo, stakeholders
│   ├── Arquitetura → Estrutura e componentes
│   ├── Stack Tecnológico → Linguagens, frameworks, DB
│   └── Convenções → Código, Git, teste
│
├── Requisito (DTR/*.md)
│   ├── Problema a Resolver → O que será implementado
│   ├── Requisitos Funcionais → O que o sistema deve fazer
│   └── Requisitos Não-Funcionais → Performance, segurança, etc.
│
├── Implementação (DTI/*.md)
│   ├── Abordagem Técnica Escolhida → Como implementar
│   ├── Estrutura de Código → Organização de diretórios
│   └── Considerações Técnicas → Performance, segurança, etc.
│
└── Aceitação (DTA/*.md)
    ├── Critérios de Aceitação → O que significa "feito"
    └── Testes e Validação → Como validar a implementação
```

---

## Ciclo de Vida dos Documentos DTF

### Fluxo Completo: Contexto → Requisito → Implementação → Aceitação → Código

```markdown
1. Contexto (.dtc/context.md)
   ↓
2. Requisito (DTR-feature-X-001.md)
   ↓
3. Implementação (DTI-feature-X-001.md) + ADRs (.dtc/decisions/*)
   ↓
4. Aceitação (DTA-feature-X-001.md)
   ↓
5. Código
   ↓
6. Manutenção/Evolução (volta ao passo 1 quando necessário)
```

### Quando Criar Cada Documento

| Documento | Quando Criar | Propósito Principal |
|-----------|--------------|---------------------|
| **DTC (.dtc/context.md)** | No início do projeto ou para grandes refatorações | Estabelecer fundação técnica e contexto do projeto |
| **DTR (DTR-feature-X-001.md)** | Para cada nova funcionalidade ou modificação significativa | Definir claramente o que será implementado |
| **DTI (DTI-feature-X-001.md)** | Após aprovação do DTR, antes da implementação | Detalhar como a solução será implementada |
| **DTA (DTA-feature-X-001.md)** | Junto com o DTI, antes da implementação | Definir como a implementação será validada |

---

## Relações entre Documentos

### Depêndências e Ordens de Criação

```
DTC (.dtc/context.md)  ← Base para todos os documentos
      ↓
DTR (feature-specific)  ← Define requirements para feature
      ↓
DTI (feature-specific)  ← Especifica implementação técnica
   ↗ ↘
DTA  Código
      ↓
Manutenção/Evolução → Retorna a DTC ou cria novo DTR/DTI
```

### Como os Documentos Referenciam uns aos Outros

| Documento de Referência | Onde Referenciar | Por que Referenciar |
|------------------------|------------------|---------------------|
| **DTR referencia DTC** | Link para `.dtc/context.md` na seção Contexto Técnico | Garantir alinhamento com arquitetura do projeto |
| **DTI referencia DTR** | Link para DTR da feature na visão geral | Traçar origem da implementação aos requisitos |
| **DTA referencia DTI** | Link para DTI na visão geral | Vincular critérios de validação à implementação |
| **ADR referencia contexto** | Link para `.dtc/context.md` ou `.dtc/architecture.md` | Manter decisões dentro do contexto arquitetural |

### Estrutura de Referências

```markdown
# Exemplo em DTR-feature-auth-001.md:
## 4. Contexto Técnico (de .dtc/context.md)
[Verifique e cite stack relevante do DTC]
```

---

## Modelos de Dados dos Documentos

### Estrutura Padrão de Template

| Seção | Propósito | Onde Usar |
|-------|-----------|-----------|
| **Visão Geral** | Contexto da feature/projeto | Todos os documentos (DTC, DTR, DTI, DTA) |
| **Detalhamento Técnico** | Especificação específica do documento | Conforme tipo (requisitos, implementação, critérios) |
| **Referências** | Links para outros documentos | DTC → todos; DTR/DTI → contexto técnico |

### Campos Obrigatórios vs. Opcionais

| Campo | DTC | DTR | DTI | DTA |
|-------|-----|-----|-----|-----|
| Visão Geral | **Obrigatório** | **Obrigatório** | **Obrigatório** | **Obrigatório** |
| Título/ID | Obrigatório | **Obrigatório** | **Obrigatório** | **Obrigatório** |
| Data do Documento | **Obrigatório** | **Obrigatório** | **Obrigatório** | **Obrigatório** |
| Autor | **Obrigatório** | **Obrigatório** | **Obrigatório** | **Obrigatório** |
| Status (Rascunho/Revisão/Aprovado) | **Obrigatório** | **Obrigatório** | **Obrigatório** | **Obrigatório** |
| Referências a outros documentos | Obrigatório | **Obrigatório** (para DTC) | **Obrigatório** (para DTR) | **Obrigatório** (para DTI) |
| Aprovações necessárias | Opcional (recomendado) | **Obrigatório** | **Obrigatório** | **Obrigatório** |

---

## Estrutura de Repositórios com DTF

### Modelo Recomendado de Pastas

```
projeto-dtf/
├── .gitignore                  # Padrões do Git + .dtc/ no git? (conforme política)
├── README.md                   # Quick start guide
├── LICENSE                     # Licença do projeto
│
├── src/                        # Código fonte principal
│   ├── components/            # Componentes reutilizáveis
│   ├── services/              # Lógica de negócio
│   ├── utils/                 # Utilitários
│   └── tests/                 # Testes unitários (opcional: repo separado)
│
├── tests/                      # Testes integrados/E2E (separate repo ou nesta pasta)
│   ├── unit/
│   │   └── test_components.py
│   ├── integration/
│   └── e2e/
│
├── docs/                       # Documentação geral (READMEs, guias de usuário)
│   ├── getting-started.md
│   ├── api-reference.md
│   └── architecture-decision-records.md  # Link para .dtc/decisions/
│
├── .dtc/                       # ⭐ DOCUMENTAÇÃO TÉCNICA DE CONTEXTO (coração do projeto DTF)
│   ├── context.md             # Visão geral do contexto do projeto
│   ├── architecture.md        # Arquitetura detalhada
│   ├── vision.md              # Visão e objetivos
│   ├── scope.md               # Escopo e limites
│   ├── principles.md          # Princípios do projeto (opcional: pode usar foundation/principles.md)
│   ├── glossary.md            # Glossário de termos
│   ├── decisions/             # ADRs (Architecture Decision Records)
│   │   ├── 001-database-choice.md
│   │   └── 002-api-versioning.md
│   └── tasks/                 # DTRs, DTIs, DTAs específicos de features
│       ├── feature-auth-001/
│       │   ├── DTR-feature-auth-001.md
│       │   ├── DTI-feature-auth-001.md
│       │   └── DTA-feature-auth-001.md
│       └── feature-comments-002/
│           ├── DTR-feature-comments-002.md
│           ├── DTI-feature-comments-002.md
│           └── DTA-feature-comments-002.md
│
├── .dtc/                      # Link para .dtc/ (se usar symlink)
│   # ou incluir em repositório conforme política do projeto

└── templates/                  # Templates customizados do projeto (opcional: usar padrão DTF)
    ├── DTC-template-custom.md
    └── ADR-template-project-specific.md
```

### Padrão de Nomenclatura

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| **DTR** | `DTR-feature-{feature-name}-{sequential-id}.md` | `DTR-feature-auth-001.md` |
| **DTI** | `DTI-feature-{feature-name}-{sequential-id}.md` | `DTI-feature-auth-001.md` |
| **DTA** | `DTA-feature-{feature-name}-{sequential-id}.md` | `DTA-feature-auth-001.md` |
| **ADR** | `{n}-{short-description}.md` | `001-database-choice.md`, `002-api-versioning.md` |

---

## Checklist de Qualidade da Documentação DTF

### Antes de Commit (individual)

```markdown
# Checklist: DTC (.dtc/context.md)
✅ Visão geral atualizada com informações do projeto
✅ Stack tecnológico documentado corretamente
✅ Convenções de código especificadas
✅ Referências para templates incluídas
✅ Histórico de versões mantido
```

### Antes de Revisão (equipe)

```markdown
# Checklist: DTR-feature-X-001.md
✅ Requisitos funcionais claros e mensuráveis
✅ Critérios de aceitação definidos
✅ Referências a `.dtc/context.md` corretas
✅ Contexto técnico alinhado com arquitetura do projeto
✅ Aprovações da equipe solicitadas antes de implementar
```

### Antes de Implementar (individual)

```markdown
# Checklist: DTI-feature-X-001.md
✅ Abordagem técnica detalhada e justificada
✅ Estrutura de código específica e completa
✅ Considerações de performance e segurança incluídas
✅ Referências a requisitos do DTR corretas
✅ Decisões técnicas documentadas ou referenciadas (ADRs)
```

### Antes de Validar (individual/equipe)

```markdown
# Checklist: DTA-feature-X-001.md
✅ Critérios de aceitação objetivos e mensuráveis
✅ Testes alinhados a critérios definidos
✅ Performance metrics especificados
✅ Aprovações solicitadas conforme checklist DTF
```

---

> **"A documentação existe para guiar implementação, não apenas validar código. O `.dtc/` é o coração do projeto DTF."**
