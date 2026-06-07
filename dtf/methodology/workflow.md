# Fluxo de Trabalho da Metodologia DTF — Workflow Principal

Este documento descreve o fluxo de trabalho principal para adoção da metodologia Documentação Técnica Funcional em projetos reais.

---

## Visão Geral do Fluxo Principal

O fluxo DTF é projetado para ser iterativo e incremental, não oneroso:

```markdown
Problema → Contexto → Requisito → Aceitação → Implementação → Testes → Código
         ↓             ↓          ↓              ↓           ↓        ↓
     .dtc/context.md  DTR/*.md   DTA/*.md       DTI/*.md   Code    Tests
                                    ↑            ↑
                                    └─────────────┘
```

**Regra fundamental**: Nenhuma implementação deve iniciar sem contexto, requisito e validação definidos.

---

## Ordem Operacional Detalhada

### 1. Consultar ou Criar DTC (`.dtc/context.md`)

**Quando**: 
- Projeto novo → criar `.dtc/context.md` com stack tecnológico, convenções
- Feature nova que impacta arquitetura existente → verificar `.dtc/context.md`
- Grandes refatorações → atualizar `.dtc/context.md`

**Checklist DTC**:
```markdown
✅ Stack tecnológico documentado (linguagens, frameworks, DB)
✅ Convenções de código especificadas
✅ Estrutura de diretórios definida
✅ Integrações documentadas (APIs externas, sistemas legados)
```

---

### 2. Criar DTR (`.dtc/tasks/DTR-feature-X-001.md`)

**Quando**: Feature nova ou modificação significativa no escopo

**Checklist DTR**:
```markdown
✅ Problema/funcionalidade claramente descrita
✅ Requisitos funcionais específicos e mensuráveis
✅ Casos de uso bem definidos
✅ Restrições e dependências documentadas
✅ Critérios de sucesso estabelecidos
✅ Referencia `.dtc/context.md` para contexto arquitetural
```

**Exemplo de workflow**:
```bash
# Criar diretório para feature nova
mkdir .dtc/tasks/DTR-feature-payment-gateway-001

# Copiar template DTR oficial
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-payment-gateway-001.md

# Editar com requisitos específicos da feature
vi .dtc/tasks/DTR-feature-payment-gateway-001.md  # Preencher:
# - O que resolve: "Pagamentos via Stripe, PayPal"
# - Requisitos funcionais:
#   - RF-001: Process payment through Stripe
#   - RF-002: Handle webhook from payment provider
```

---

### 3. Definir DTA (`.dtc/tasks/DTA-feature-X-001.md`)

**Quando**: Junto com DTI, antes de completar feature

**Checklist DTA**:
```markdown
✅ Critérios de aceitação objetivos e mensuráveis
✅ Testes automatizados especificados
✅ Performance metrics definidas
✅ Checklist de qualidade específico para feature
```

---

### 4. Elaborar DTI (`.dtc/tasks/DTI-feature-X-001.md`)

**Quando**: Após aprovação do DTR, antes da implementação

**Checklist DTI**:
```markdown
✅ Abordagem técnica detalhada e justificada
✅ Estrutura de código especificada
✅ Algoritmos/lógica principais descritos
✅ Integrações documentadas
✅ Considerações de performance incluídas
```

---

### 5. Implementar (Codar)

**Quando**: Após aprovação do DTI, com checklist DTA em mente

**Checklist implementação**:
```markdown
✅ Segue especificação técnica do DTI
✅ Testes escritos conforme DTA
✅ Code review baseado em critérios DTA
✅ Documentação atualizada se necessário (.dtc/context.md)
```

---

### 6. Executar Testes

**Quando**: Após implementar feature nova

**Fluxo de teste**:
```bash
# Unit tests (conforme checklist do DTA):
pytest tests/unit/test_feature_name.py

# Integration tests:
pytest tests/integration/test_feature_integration.py

# E2E tests (critical paths):
pytest tests/e2e/test_feature_e2e.py
```

---

### 7. Validar Critérios de Aceitação

**Quando**: Após implementar e rodar testes

**Checklist validação DTA**:
```markdown
✅ RF-001: [x] Autenticação OAuth2 com Google funciona
✅ RF-002: [x] Account linking works corretamente
✅ NFR-001: [x] Performance p95 < 500ms
✅ AC-001: [x] Critérios de aceitação do DTA passados

# Run acceptance tests:
pytest --acceptance-tests tests/acceptance/test_oauth2_auth.py
```

---

## Regra Fundamental

**Nenhuma implementação deve iniciar sem contexto, requisito e validação definidos.**

### Por quê?

- ❌ **Contexto implícito**: "Ah, o código já usa PostgreSQL, né?" → conhecimento morre com devs
- ❌ **Requisito vago**: "Crie algo para login" → código genérico, não alinhado ao projeto
- ❌ **Validação ad-hoc**: "Vou testar depois que codar" → bugs passados para produção

### Com DTF:

✅ **Contexto explícito**: `.dtc/context.md` define stack tecnológico, convenções  
✅ **Requisito específico**: DTR-feature-X-001.md especifica o quê será implementado  
✅ **Validação pré-definida**: DTA feature-X-001.md lista critérios de aceitação antes de codar

---

## Fluxo para Projeto Novo (Do Zero ao Primeiro Commit)

```bash
# Passo 1: Inicializar repositório
git init
git add .
git commit -m "feat(.dtc): initial project structure"

# Passo 2: Criar .dtc/context.md com template
cp ../templates/DTC-template.md .dtc/context.md
vi .dtc/context.md  # Preencher:
#   - Stack: Python 3.11+, FastAPI, PostgreSQL
#   - Convenções: Black + ruff, Git Conventional Commits

# Passo 3: Adicionar .gitignore se não existir
echo ".venv/" > .gitignore
echo "__pycache__/" >> .gitignore

# Commit inicial
git add .dtc/context.md .gitignore
git commit -m "feat(.dtc): add context documentation for Python/FastAPI project"

# Passo 4: Criar entry point
touch src/main.py
echo "from fastapi import FastAPI\napp = FastAPI()" > src/main.py

# Commit código inicial
git add src/main.py
git commit -m "feat(src): initial FastAPI app"

# Projeto básico DTF pronto para receber primeira feature! 🎉
```

---

## Fluxo para Feature Nova (Incremental)

```bash
# Passo 1: Criar diretório DTR para nova feature
mkdir .dtc/tasks/DTR-feature-auth-001

# Passo 2: Copiar template DTR
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-auth-001.md

# Passo 3: Editar DTR com requisitos específicos da feature
vi .dtc/tasks/DTR-feature-auth-001.md  # Preencher:
#   - Título: "DTR-feature-auth-001 — Sistema de Comentários em Posts"
#   - Visão geral: "Usuários podem comentar posts do blog"
#   - Requisitos funcionais (RF-001 a RF-005)
#   - Requisitos não-funcionais (NFR-001, NFR-002)

# Passo 4: Revisar DTR com equipe (se tiver)
# Review checklist:
# [ ] Requisitos claros e mensuráveis?
# [ ] Casos de uso bem descritos?
# [ ] Critérios de sucesso definidos?

# Commit documentação antes de codar!
git add .dtc/tasks/DTR-feature-auth-001.md
git commit -m "docs(.dtc): add DTR for blog comments feature (PR review pending)"

# Passo 5: Elaborar DTI após aprovação do DTR
cp ../templates/DTI-template.md .dtc/tasks/DTI-feature-auth-001.md
vi .dtc/tasks/DTI-feature-auth-001.md  # Especificar implementação técnica

# Commit DTI aprovado
git add .dtc/tasks/DTI-feature-auth-001.md
git commit -m "docs(.dtc): add DTI for blog comments feature (approved)"

# Passo 6: Criar DTA junto com DTI
cp ../templates/DTA-template.md .dtc/tasks/DTA-feature-auth-001.md
vi .dtc/tasks/DTA-feature-auth-001.md  # Checklist de aceitação específico

# Commit DTA definido
git add .dtc/tasks/DTA-feature-auth-001.md
git commit -m "docs(.dtc): add DTA for blog comments feature"

# Passo 7: Implementar código seguindo DTI
mkdir -p src/comments/{models, routes, schemas, service}
touch src/comments/__init__.py src/comments/models.py src/comments/routes.py
# ... codar conforme especificação do DTI ...

git add src/comments/
git commit -m "feat(src): implement blog comments feature per DTI-feature-auth-001"

# Passo 8: Validar com DTA (testes)
pytest --acceptance-tests tests/acceptance/test_comments_feature.py
# ou rodar manualmente testes aceitação

# Commit após validação completa
git add tests/acceptance/
git commit -m "tests(.dtc): add acceptance tests for comments feature"

# Feature completa! 🎉
```

---

## Fluxo para Feature Existentes (Manutenção/Evolução)

**Quando adicionar feature a projeto existente**:

```bash
# 1. Verificar .dtc/context.md atualizado com stack tecnológico?
cat .dtc/context.md  # Se não está na seção Stack, atualizar antes de codar!
git add .dtc/context.md
git commit -m "docs(.dtc): update context.md to reflect Python/FastAPI stack"

# 2. Criar DTR específico para feature existente
mkdir .dtc/tasks/DTR-feature-user-management-001
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-user-management-001.md
# ... editar com requisitos ...

git add .dtc/tasks/DTR-feature-user-management-001.md
git commit -m "docs(.dtc): add DTR for user management feature"

# 3. Criar DTI e DTA (se necessário)
cp ../templates/DTI-template.md .dtc/tasks/DTI-feature-user-management-001.md
cp ../templates/DTA-template.md .dtc/tasks/DTA-feature-user-management-001.md
# ... editar especificações ...

git add .dtc/tasks/DTI* .dtc/tasks/DTA*.md
git commit -m "docs(.dtc): add DTI and DTA for user management feature"

# 4. Implementar e testar conforme fluxo incremental (passos anteriores)
```

---

## Fluxo para Grandes Refatorações

**Quando mudar arquitetura significativamente**:

```bash
# Passo 1: Documentar decisão de refatoração em ADR
cp ../templates/ADR-template.md .dtc/decisions/003-architecture-refactor.md
vi .dtc/decisions/003-architecture-refactor.md

# Passo 2: Atualizar .dtc/context.md com nova arquitetura
vi .dtc/context.md  # Seção Arquitetura atualizada

# Commit ADR e context.md
git add .dtc/decisions/*.md .dtc/context.md
git commit -m "docs(.dtc): update architecture for refactoring project to microservices"

# Passo 3: Criar DTRs para features novas com nova arquitetura
mkdir .dtc/tasks/DTR-feature-auth-microservice-001
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-auth-microservice-001.md
# ... editar conforme nova arquitetura microservices ...

git add .dtc/tasks/DTR-feature-auth-microservice-001.md
git commit -m "docs(.dtc): add DTR for auth microservice (refactored architecture)"
```

---

## Checklist de Qualidade do Workflow DTF

### Antes de Codar Primeira Feature:

```markdown
✅ `.dtc/context.md` existe e está atualizado
✅ Stack tecnológico documentado em .dtc/context.md
✅ Convenções de código especificadas (.dtc/context.md)
✅ Estrutura de diretórios definida
✅ Referências a templates incluídas
```

### Para Cada Feature Nova:

```markdown
✅ DTR específico criado (`.dtc/tasks/DTR-feature-X-001.md`)
✅ DTI específico elaborado (`.dtc/tasks/DTI-feature-X-001.md`)
✅ DTA definido para validação (`.dtc/tasks/DTA-feature-X-001.md`)
✅ Código implementado seguindo DTI especificado
✅ Testes escritos conforme checklist DTA
```

### Após Implementar Feature:

```markdown
✅ Critérios de aceitação do DTA validados
✅ Code review baseado em critérios DTA feito
✅ `.dtc/context.md` atualizado se necessário (stack, convenções)
✅ ADR criado para decisões arquiteturais importantes
```

---

## Integração com CI/CD

### GitHub Actions Workflow:

```yaml
name: DTF Validation Workflow
on: [pull_request]

jobs:
  validate-dtf-docs:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Install dependencies
        run: pip install dtf-validator pytest httpx
        
      - name: Validate .dtc/ exists (PR requirement)
        if: github.event_name == 'pull_request'
        run: |
          if [ ! -f ".dtc/context.md" ]; then
            echo "❌ Missing .dtc/context.md in PR. Create DTC documentation first!"
            exit 1
          fi
          
      - name: Validate template consistency  
        run: dtf lint --strict .dtc/
        
      - name: Run acceptance tests (from DTAs)
        run: pytest --acceptance-tests tests/acceptance/
```

---

> *"DTF é incremental. Comece pequeno, evolua conforme o projeto cresce."*  
> Referências: [.dtc/context.md](../.dtc/context.md), [`foundation/workflow.md`](../../methodology/workflow.md)
