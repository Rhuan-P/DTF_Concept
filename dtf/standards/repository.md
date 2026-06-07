# Estrutura de Repositórios para Metodologia DTF

Este documento descreve padrões para estrutura de repositórios que utilizam a metodologia Documentação Técnica Funcional.

---

## Padrão Recomendado de Estrutura

### Repositório Único com Pasta `.dtc/`:

```bash
projeto-dtf/
├── .gitignore               # ✅ Deve incluir .venv/, __pycache__/, etc.
├── README.md                # Quick start guide
├── LICENSE                  # MIT License (padrão mercado)
│
├── src/                     # Código fonte principal
│   ├── components/         # Componentes reutilizáveis
│   ├── services/           # Lógica de negócio
│   ├── utils/              # Utilitários
│   └── tests/              # Testes unitários (opcional: repo separado)
│
├── tests/                   # Testes integrados/E2E
│   ├── unit/
│   │   └── test_components.py
│   ├── integration/
│   └── e2e/
│
├── docs/                    # Documentação geral (READMEs, guias de usuário)
│   ├── getting-started.md
│   ├── api-reference.md
│   └── architecture-decision-records.md  # Link para .dtc/decisions/
│
├── .dtc/                    # ⭐ DOCUMENTAÇÃO TÉCNICA DE CONTEXTO (coração do projeto DTF)
│   ├── context.md          # Visão geral do contexto do projeto
│   ├── architecture.md     # Arquitetura detalhada
│   ├── vision.md           # Visão e objetivos
│   ├── scope.md            # Escopo e limites
│   ├── glossary.md         # Glossário de termos
│   ├── decisions/          # ADRs (Architecture Decision Records)
│   │   ├── 001-database-choice.md
│   │   └── 002-api-versioning.md
│   └── tasks/              # DTR, DTI, DTA específicos de features
│       ├── feature-auth-001/
│       │   ├── DTR-feature-auth-001.md
│       │   ├── DTI-feature-auth-001.md
│       │   └── DTA-feature-auth-001.md
│       └── feature-comments-002/
│           ├── DTR-feature-comments-002.md
│           ├── DTI-feature-comments-002.md
│           └── DTA-feature-comments-002.md
│
├── .dtc/                      # Symlink ou link para .dtc/ (se usar symlink)
│   # ou incluir em repositório conforme política do projeto

└── ecosystem/               # Ferramentas e integrações DTF oficial
    ├── extension.md         # Extensões oficiais DTF
    └── mcp.md               # Integração com IA via MCP
```

---

## Repositório Separado para Testes (Recomendado)

### Estrutura com repositório de testes separado:

```bash
# Repositório principal do projeto (src/)
projeto-dtf-main/
├── src/
│   ├── components/
│   └── services/
│
└── .dtc/                    # DOCUMENTAÇÃO TÉCNICA DE CONTEXTO
    ├── context.md
    ├── architecture.md
    └── ...

# Repositório separado de testes (ex: github.com/user/project-dtf)
projeto-dtf-tests/
├── tests/unit/
│   └── test_components.py
├── tests/integration/
└── tests/e2e/

# Repositório `.dtc/` como exemplo de estrutura DTF (recomendado para docs)
projeto-dtf-docs/
├── README.md
└── .gitignore (.gitignore deve incluir .venv/, __pycache__/, etc.)
```

### Vantagens do Repositório Separado:
- ✅ **Performance**: Commit de código não polui com docs DTF grandes
- ✅ **Modularidade**: Testes podem ser contribuidos independentemente
- ✅ **Clareza**: Separação clara entre código fonte e documentação técnica

---

## Symlink para `.dtc/` (Opcional)

### Quando usar symlink:

```bash
# Criar link para .dtc/ em outro lugar do repositório
cd projeto-dtf-main/
mkdir -p docs/dtf  # Criar pasta docs/dtf/
ln -s ../.dtc/ docs/dtf/  # Link symlink
```

### Quando NÃO usar symlink:
- Repositórios com muitos arquivos de `.gitignore` (symlink não é ignorado automaticamente)
- Ferramentas CI/CD específicas que exigem `.dtc/` em diretório raiz
- Compartilhamento entre equipes diferentes com políticas de repositório estritas

---

## Checklist de Estrutura para Novo Repositório DTF

### Passo 1: Estrutura Básica

```bash
# Criar estrutura inicial do projeto DTF
mkdir -p projeto-dtf/{src/{components,services,utils,tests},tests/{unit,integration,e2e},docs,.dtc}

# Criar .gitignore com padrões de Python
echo ".venv/" > projeto-dtf/.gitignore
echo "__pycache__/" >> projeto-dtf/.gitignore
echo "*.py[cod]" >> projeto-dtf/.gitignore
echo ".DS_Store" >> projeto-dtf/.gitignore

# Criar LICENSE (MIT)
cp /path/to/MIT-license.txt projeto-dtf/LICENSE

# Commit inicial
cd projeto-dtf/
git add .gitignore LICENSE
git commit -m "feat(.dtc): initial project structure with Python/DTF standards"
```

### Passo 2: Template DTC Inicial

```bash
# Criar .dtc/context.md usando template
cp ../templates/DTC-template.md .dtc/context.md

# Editar com informações do projeto
vi .dtc/context.md

# Commit da documentação inicial
git add .dtc/context.md
git commit -m "docs(.dtc): add initial context documentation for Python project"
```

### Passo 3: Entry Point e Primeiras Features

```bash
# Criar entry point do projeto (ex: FastAPI app)
mkdir -p src/
touch src/main.py
echo "from fastapi import FastAPI\napp = FastAPI()" > src/main.py

# Commit código inicial
git add src/main.py
git commit -m "feat(src): initial FastAPI app entry point"

# Criar primeira feature (ex: auth) conforme fluxo DTF incremental
mkdir -p .dtc/tasks/DTR-feature-auth-001
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-auth-001.md
vi .dtc/tasks/DTR-feature-auth-001.md

# Commit documentação de feature
git add .dtc/tasks/DTR-feature-auth-001.md
git commit -m "docs(.dtc): add DTR for auth feature (pending implementation)"
```

---

## Padrão para Contribuição em Repositório Existente

### Checklist Contribuidor:

```markdown
# Ao contribuir com repositório DTF existente:

✅ Verificar se `.gitignore` está configurado corretamente (inclui .venv/)
✅ Ler `.dtc/context.md` antes de implementar novas features
✅ Usar templates do repositório (.dtc/templates/ ou ../templates/)
✅ Criar ADR em `.dtc/decisions/` para decisões arquiteturais importantes
✅ Seguir nomenclatura: DTR-feature-X-001.md, DTI-feature-X-001.md, etc.
✅ Adicionar testes conforme checklist do DTA existente
✅ Atualizar `.dtc/context.md` se alterar stack tecnológico
```

### Workflow Contribuinte:

```bash
# 1. Clone repositório e verificar estrutura .dtc/
git clone https://github.com/user/projeto-dtf.git
cd projeto-dtf/
ls -la .dtc/  # Verificar estrutura existente

# 2. Ler documentação técnica relevante
cat .dtc/context.md        # Stack tecnológico, convenções
cat .dtc/architecture.md   # Arquitetura do sistema
cat .dtc/decisions/*.md    # Decisões arquiteturais passadas

# 3. Criar DTR para feature nova (antes de codar!)
mkdir -p .dtc/tasks/DTR-feature-user-management-001
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-user-management-001.md

vi .dtc/tasks/DTR-feature-user-management-001.md  # Preencher requisitos

git add .dtc/tasks/DTR-feature-user-management-001.md
git commit -m "docs(.dtc): add DTR for user management feature"

# 4. Implementar conforme DTI existente (ou criar DTI se necessário)
cp ../templates/DTI-template.md .dtc/tasks/DTI-feature-user-management-001.md
vi .dtc/tasks/DTI-feature-user-management-001.md

git add .dtc/tasks/DTI-feature-user-management-001.md
git commit -m "docs(.dtc): add DTI for user management feature"

# 5. Implementar código seguindo DTI (e criar DTA)
mkdir -p src/users
touch src/users/models.py src/users/routes.py

git add src/users/
git commit -m "feat(src): implement user management per DTI-feature-user-management-001"

# 6. Adicionar testes conforme checklist do DTA
pytest tests/unit/test_users.py --acceptance-tests
```

---

## Referências e Leitura Recomendada

| Arquivo | Propósito | Quando Ler |
|---------|-----------|------------|
| [README principal](../../README.md) | Guia geral da metodologia DTF | Primeiro acesso ao repositório |
| `.dtc/context.md` | Stack tecnológico, convenções, estrutura do projeto | Antes de implementar qualquer feature |
| `.dtc/architecture.md` | Arquitetura detalhada do sistema | Para entender contexto de implementação |
| `.dtc/decisions/*.md` | Decisões arquiteturais passadas (ADRs) | Para manter consistência com arquitetura existente |
| `templates/DTC-template.md` | Template oficial para criar DTC inicial | Criando contexto novo ou refatorando |
| `ecosystem/mcp.md` | Integração com IA via MCP | Usando IA com DTF no projeto |

---

> *"Estrutura de repositório clara + `.dtc/` bem mantido = conhecimento que sobrevive às mudanças de equipe."*  
> Referências: [`foundation/repository.md`](../../dtf/standards/repository.md), [.gitignore padrão](../.gitignore)
