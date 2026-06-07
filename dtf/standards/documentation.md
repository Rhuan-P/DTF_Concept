# Padrões de Uso da Metodologia DTF — Documentation Standards

Este documento descreve padrões para uso dos documentos DTF (DTC, DTR, DTI, DTA) em projetos que utilizam a metodologia Documentação Técnica Funcional.

---

## Padrão de Nomenclatura de Arquivos

### Estrutura Recomendada:

```
.dt c/tasks/
├── DTC-project-name.md              # Contexto do projeto
├── DTR-feature-authentication-001.md  # Requisito feature 1
│   └── DTI-feature-authentication-001.md  # Implementação feature 1
│       └── DTA-feature-authentication-001.md  # Aceitação feature 1
├── DTR-feature-payments-002.md
│   └── DTI-feature-payments-002.md
│       └── DTA-feature-payments-002.md
└── ADRs                               # Architecture Decision Records em .dtc/decisions/
    ├── 001-database-choice.md
    └── 002-api-versioning.md
```

### Nomenclatura Oficial:

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| **DTR** | `DTR-feature-{feature-name}-{sequential-id}.md` | `DTR-feature-auth-001.md` |
| **DTI** | `DTI-feature-{feature-name}-{sequential-id}.md` | `DTI-feature-auth-001.md` |
| **DTA** | `DTA-feature-{feature-name}-{sequential-id}.md` | `DTA-feature-auth-001.md` |
| **ADR** | `{n}-{short-description}.md` | `001-database-choice.md` |

### Regras:

1. **Feature name**: Nome descritivo em kebab-case (ex: "auth" para login)
2. **Sequential ID**: Número ordenado por data de criação (001, 002, ...)
3. **Arquivos juntos**: DTR/DTI/DTA da mesma feature ficam na mesma pasta

---

## Padrões de Formato Markdown

### Checklist de Qualidade do Documento:

```markdown
# Cada documento DTF deve ter:
[ ] Título claro e específico
[ ] Data atualizada (YYYY-MM-DD)
[ ] Autor identificado (nome completo ou nickname de equipe)
[ ] Status definido (Rascunho | Em Revisão | Aprovado)
[ ] Referências claras para outros documentos (.dtc/context.md, etc.)
[ ] Aprovações solicitadas conforme necessário
```

### Checklist de DTC (`.dtc/context.md`):

```markdown
# Seção obrigatória:
- [ ] Visão Geral → Propósito do projeto
- [ ] Arquitetura → Estrutura e componentes principais
- [ ] Stack Tecnológico → Linguagens, frameworks, DB
- [ ] Convenções → Código, organização de diretórios, Git
- [ ] Integrações → APIs externas, sistemas legados

# Seção recomendada:
- [ ] Princípios de Design → Princípios arquiteturais
- [ ] Segurança → Requisitos de segurança do projeto
- [ ] Performance → Requisitos e estratégias
```

### Checklist de DTR (`.dtc/tasks/DTR-feature-X-001.md`):

```markdown
# Seção obrigatória:
- [ ] Visão Geral da Feature
- [ ] Requisitos Funcionais → RF-001, RF-002, etc.
- [ ] Requisitos Não-Funcionais → NFR-001, NFR-002, etc.

# Seção recomendada:
- [ ] Casos de Uso → Quem usa, como usam
- [ ] Restrições e Assumptions
- [ ] Fluxo de Trabalho Completo (diagramas Mermaid/PlantUML)
```

### Checklist de DTI (`.dtc/tasks/DTI-feature-X-001.md`):

```markdown
# Seção obrigatória:
- [ ] Abordagem Técnica Escolhida → Por que esta abordagem?
- [ ] Estrutura de Código → Organização de diretórios
- [ ] Implementação Detalhada → Códigos de exemplo, pseudocódigo
- [ ] Considerações Técnicas → Performance, segurança

# Seção recomendada:
- [ ] Diagramas de Arquitetura da Implementação
- [ ] Checklist de Implementação (para dev implementar)
```

### Checklist de DTA (`.dtc/tasks/DTA-feature-X-001.md`):

```markdown
# Seção obrigatória:
- [ ] Critérios de Aceitação → AC-001, AC-002, etc.
- [ ] Testes Unitários → Casos de teste específicos
- [ ] Testes Integrados → Flows completos

# Seção recomendada:
- [ ] Checklist Completo de Testes
- [ ] Performance Targets (p95 latency, throughput)
- [ ] Aprovações Necessárias
```

---

## Padrões de Code Review DTF

### Pre-Requisitos para PR com Feature Nova:

```markdown
# Checklist do Code Reviewer (baseado em DTF):
[ ] DTI da feature exist? Verificar .dtc/tasks/DTI-feature-X-001.md
[ ] Código segue especificação técnica do DTI?
[ ] Testes escritos conforme checklist DTA?
[ ] `.dtc/context.md` atualizado se necessário?
[ ] ADR criado para decisões arquiteturais importantes?
```

### Template de Code Review:

```markdown
# Review Checklist DTF-feature-auth-001:

## ✅ DTI Alignment
- [ ] Implementação segue especificação do DTI
- [ ] Código organizado conforme estrutura definida no DTI
- [ ] Testes unitários cobrem casos principais (>80% coverage alvo)

## ✅ DTA Criteria Met
- [ ] AC-001: OAuth2 flow completo (Google/GitHub)
- [ ] AC-002: Account linking funciona
- [ ] AC-003: PKCE implemented corretamente
- [ ] AC-004: Token encryption at rest

## ✅ Documentation Updated
- [ ] .dtc/context.md stack atualizado com nova feature
- [ ] ADR documentando decisão de usar OAuth2 library X
```

---

## Padrões de Commit Message DTF

### Convencional Commits + DTF:

```bash
# Formato recomendado:
git commit -m "{type}(.dtc|docs): {message}"

# Exemplos:

feat(.dtc): add DTR-feature-auth-001.md
fix(.dtc): update .dtc/context.md stack section (add Redis)
docs(dt f): add DTI-feature-payments-001.md for Stripe integration
tests(.dtc): implement acceptance tests from DTA-feature-comments-002

feat(src): implement OAuth2 auth per DTI-feature-auth-001
refactor(.dtc): update .dtc/architecture.md reflect microservices decision (ADR 002)
```

### Tipos de Commit:

| Tipo | Uso com DTF | Exemplo |
|------|-------------|---------|
| **feat** | Feature nova conforme DTI | `feat(src): implement OAuth per DTI-feature-auth-001` |
| **.dtc** | Alteração da documentação técnica | `docs(.dtc): update .dtc/context.md stack section` |
| **.doc s(dt f)** | Documentação adicional DTF | `docs(dtf): add ADR for database migration strategy` |
| **fix** | Correção de bugs (sempre atualizar docs se impacto) | `fix(src): correct OAuth token encryption per DTI spec + docs(.dtc): update token_encryption.md` |
| **refactor** | Refatoração com atualização de docs | `refactor(.dtc): update .dtc/architecture.md reflect microservices` |
| **tests** | Adição de testes (conforme checklist DTA) | `tests(.dtc): implement acceptance tests from DTA-feature-comments-002` |

---

## Padrões de Validação Automática

### GitHub Actions Workflow:

```yaml
# .github/workflows/dtf-validation.yml
name: DTF Validation
on: [pull_request]

jobs:
  validate-dtf-docs:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Install validation tools
        run: pip install dtf-validator pydantic pytest httpx
      
      - name: Validate .dtc/ exists (PR requirement)
        if: github.event_name == 'pull_request' && !contains(github.event.pull_request.paths.0, '.dtc/')
        run: |
          if [ ! -f ".dtc/context.md" ]; then
            echo "❌ Missing .dtc/context.md in PR. Create DTC documentation first!"
            exit 1
          fi
      
      - name: Validate template consistency  
        run: dtf lint --strict .dtc/
      
      - name: Check for missing DTI (DTI required before coding)
        if: github.event_name == 'pull_request'
        run: |
          DTR_COUNT=$(ls .dtc/tasks/DTR-*.md 2>/dev/null | wc -l)
          DTI_COUNT=$(ls .dtc/tasks/DTI-*.md 2>/dev/null | wc -l)
          
          # Require DTI for each DTR (or consolidated DTI if multiple features sharing same DTI)
          if [ $DTR_COUNT -gt 0 ] && [ $DTI_COUNT -eq 0 ]; then
            echo "⚠️ Found DTRs without corresponding DTIs. Add DTI documentation!"
            # Não fail automaticamente, apenas warning
          fi
      
      - name: Run acceptance tests (if feature implemented)
        run: pytest --acceptance-tests tests/acceptance/ 2>/dev/null || true
        
      - name: Code coverage check
        run: |
          coverage report --show-missing || true
```

### Pre-commit Hooks DTF:

```yaml
# .pre-commit-config.yaml (exemplo)
repos:
  - repo: local
    hooks:
      - id: dtf-lint
        name: DTF Documentation Linter
        entry: dtf lint --strict .dtc/
        language: python
        pass_filenames: false
        
      - id: dtf-format
        name: DTF Markdown Formatter
        entry: prettier --write .dtc/**/*.md
        language: system
        files: '\.dtc/.*\.md$'
```

---

## Padrões de Estrutura de Repositórios DTF

### Repositório Completo com DTF:

```bash
projeto-dtf/
├── README.md                 # Quick start guide
├── LICENSE                   # MIT License
│
├── .dtc/                    # ⭐ DOCUMENTAÇÃO TÉCNICA DE CONTEXTO
│   ├── context.md           # Fonte da verdade do projeto
│   ├── architecture.md      # Arquitetura detalhada
│   ├── vision.md            # Visão e objetivos
│   ├── scope.md             # Escopo e limites
│   ├── glossary.md          # Glossário de termos
│   ├── decisions/           # ADRs (Architecture Decision Records)
│   │   ├── 001-database-choice.md
│   │   └── 002-api-versioning.md
│   └── tasks/               # DTR, DTI, DTA específicos de features
│       ├── feature-auth-001/
│       │   ├── DTR-feature-auth-001.md
│       │   ├── DTI-feature-auth-001.md
│       │   └── DTA-feature-auth-001.md
│       └── feature-comments-002/
│           ├── DTR-feature-comments-002.md
│           ├── DTI-feature-comments-002.md
│           └── DTA-feature-comments-002.md
│
├── src/                     # Código fonte principal
│   ├── auth/               # Implementação feature OAuth (conforme DTI-feature-auth-001)
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── service.py
│   └── comments/           # Implementação feature comentários (conforme DTI-feature-comments-002)
│       ├── models.py
│       ├── routes.py
│       └── service.py
│
├── tests/                   # Testes unitários e integração
│   ├── unit/
│   │   └── test_auth_models.py
│   ├── integration/
│   │   └── test_oauth_flow.py
│   └── acceptance/         # Testes de aceitação (conforme DTA)
│       └── test_feature_comments-002.py
│
├── docs/                    # Documentação geral do projeto
│   ├── getting-started.md  # Guia para novos devs
│   ├── api-reference.md    # API documentation
│   └── architecture-decision-records.md  # Link para .dtc/decisions/
│
├── templates/               # Templates customizados do projeto (opcional)
│   ├── DTC-template-custom.md
│   └── ADR-template-project-specific.md
│
├── ecosystem/              # Ferramentas e integrações (padrão DTF oficial)
│   ├── extension.md        # Extensões oficiais DTF
│   └── mcp.md              # Integração com IA via MCP
│
├── roadmap/                # Roadmap de evolução da metodologia
│   └── evolution.md        # Evolução planejada do DTF
│
└── .gitignore              # Padrões: .venv/, __pycache__/, etc.
```

---

## Referências e Leitura Recomendada

| Arquivo | Propósito | Quando Ler |
|---------|-----------|------------|
| [README principal](../../README.md) | Guia geral do DTF + estrutura | Primeiro acesso ao repositório |
| `foundation/manifesto.md` | O que acreditamos sobre software | Iniciando com metodologia DTF |
| `dtf/context/architecture.md` | Arquitetura dos documentos | Configurando estrutura do projeto |
| `templates/DTC-template.md` | Template completo para DTC | Criando contexto novo |
| `ecosystem/mcp.md` | Integração com IA via MCP | Usando IA com DTF |
| `roadmap/evolution.md` | Evolução planejada da metodologia | Contribuindo com o DTF |

---

> *"Documentação técnica estruturada deve guiar o desenvolvimento. O padrão de uso DTF torna a metodologia consistente e escalável."*
