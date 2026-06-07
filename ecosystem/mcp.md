# Automação DTF via Model Context Protocol (MCP)

O **Model Context Protocol (MCP)** permite que ferramentas de IA conectem-se à sua documentação técnica `.dtc/` para compreender contexto completo antes de gerar código.

---

## 🎯 O que é MCP?

**MCP (Model Context Protocol)** é um padrão aberto para conectar LLMs a dados e ferramentas externas de forma segura e estruturada.

### Exemplo de uso com DTF:

```
IA generativa → Conecta MCP server → Lê .dtc/context.md → 
Gera código alinhado à arquitetura do projeto (não genérico)
```

**Sem MCP:**  
*"Crie uma API para login"* → Código genérico, não alinhado ao projeto.

**Com MCP:**  
IA conecta `.dtc/` → Gera code alinhado a `.dtc/architecture.md` + decisões em `.dtc/decisions/`.

---

## 📦 Configurando MCP com DTF

### 1. Instalar Server DTF-MCP

```bash
pip install dtf-mcp-server
```

**Server Python**:
```python
# .cursorrules ou config.yaml para Cursor AI:
{
  "mcpServers": {
    "dtf-context": {
      "type": "stdio",
      "command": "python -m dtf_context_server",
      "env": {
        "DTF_PATH": "${workspaceFolder}/.dtc/",
        "LOG_LEVEL": "info"
      }
    },
    
    "dtf-decisions": {
      "type": "stdio",
      "command": "python -m dtf_decisions_server",
      "env": {
        "DECISIONS_PATH": "${workspaceFolder}/.dtc/decisions",
        "AUTO_INDEX": true
      }
    }
  }
}
```

### 2. Server CLI Standalone

```bash
python -m dtf_mcp_server \
  --dtf-path .dtc/ \
  --decisions-path .dtc/decisions \
  --port 8080
```

**Server expose via HTTP API**:
```bash
curl http://localhost:8080/tools/list \
  -H "Content-Type: application/json"

# Response:
{
  "tools": [
    {
      "name": "get_context",
      "description": "Get project context from .dtc/context.md"
    },
    {
      "name": "list_decisions",
      "description": "List all architecture decisions"
    }
  ]
}
```

---

## 🛠️ Tools do DTF-MCP Server

### Tool: `get_context`

Lê o arquivo `.dtc/context.md` para IA entender o projeto.

**Request**:
```json
{
  "name": "get_context",
  "arguments": {
    "section": ["architectures", "stack"],  # Sections to focus on
    "max_lines": 50
  }
}
```

**Response**:
```json
{
  "type": "text",
  "content": [
    {
      "type": "text",
      "text": "# Stack Tecnológico\n\n- **Linguagem Principal**: Python 3.11+\n- **Framework Web**: FastAPI v0.109+\n- **Database**: PostgreSQL 15+..."
    }
  ]
}
```

### Tool: `get_architecture`

Lê `.dtc/architecture.md` para alinhamento arquitetural completo.

**Request**:
```json
{
  "name": "get_architecture",
  "arguments": {
    "component": "user-authentication"  # Specific component to query
  }
}
```

### Tool: `list_decisions`

Listar todas as Architecture Decision Records (ADRs).

**Request**:
```json
{
  "name": "list_decisions",
  "arguments": {
    "sort_by": "created_at",
    "limit": 10
  }
}
```

### Tool: `validate_context`

Verifica se documentação `.dtc/` está completa conforme metodologia DTF.

**Request**:
```json
{
  "name": "validate_context",
  "arguments": {
    "checks": [
      "drc-exists",
      "architecture-exists",
      "decisions-listed",
      "templates-updated"
    ]
  }
}
```

### Tool: `generate_dtc_draft`

Gera rascunho de `.dtc/context.md` baseado em prompts.

**Request**:
```json
{
  "name": "generate_dtc_draft",
  "arguments": {
    "project_type": "e-commerce",
    "features": ["user auth", "cart", "checkout"],
    "target_stack": "fastapi,postgresql"
  }
}
```

---

## 💬 Prompts Otímo com MCP DTF

### Prompt 1: Gerar Código Alinhado à Arquitetura

**Contexto**: IA já conectada ao server MCP `.dtc-context`.

```
@cursor ask dtf-context-server

Use .dtc/context.md para gerar código alinhado à arquitetura do projeto.

Contexto extraído de .dtc/context.md:
- Stack: FastAPI v0.109+, Python 3.11+
- Database: PostgreSQL 15+ with asyncpg driver
- Auth: JWT OAuth2PasswordBearer via fastapi.security

Requisito: Implementar endpoint POST /auth/login conforme DTR-feature-auth-001
```

### Prompt 2: Revisar Código Contra Decisões Arquiteturais

```
@cursor ask dtf-decisions-server

Liste todas as decisões arquiteturais registradas em .dtc/decisions/.

Review este código novo contra essas decisões e alerte sobre violações.

Código novo:
[insere código aqui]
```

### Prompt 3: Gerar Testes Baseados em DTAs

```
@cursor ask dtf-context-server

Use templates de DTA (.dtc/templates/DTA-template.md) para gerar
testes automatizados que validam critérios de aceitação.

Cenário: endpoint POST /comments/{post_id}
Critérios de aceitação:
- [ ] Comment created with correct fields
- [ ] Response time < 200ms p95
- [ ] Database integrity maintained
```

---

## 🔌 Integração com Cursor AI (VS Code)

### Configurar `settings.json` do VS Code:

```jsonc
// .vscode/settings.json
{
  "mcpServers.dtf-context": {
    "type": "stdio",
    "command": "python -m dtf_context_server",
    "env": {
      "DTF_PATH": "${workspaceFolder}/.dtc/"
    }
  },
  
  "codeium.advancedContextEnabled": true,
  "editor.tabSize": 2,  // Match .dtc/context.md conventions
  
  // Auto-suggest based on context:
  "ai.chat.context.includeDocs": true,
  "ai.chat.context.paths": [
    "${workspaceFolder}/.dtc/context.md",
    "${workspaceFolder}/.dtc/architecture.md",
    "${workspaceFolder}/.dtc/decisions/*.md"
  ]
}
```

### Prompt Otímo no Cursor:

```markdown
@cursor ask dtf-context-server
Use .dtc/context.md e .dtc/architecture.md para gerar código alinhado à arquitetura do projeto. Se o contexto não for suficiente, pergunte ao usuário para adicionar documentação antes de codar.

Requisito: Implementar feature X (ver DTR-feature-X-001)
```

---

## 🌐 Integração com GitHub Copilot

### Configurar GitHub Copilot Workspace:

```json
// .github/copilot/config.json
{
  "context": {
    "folders": [".dtc", ".github"],
    "files": ["README.md", ".dtc/context.md"]
  },
  
  "tools": [
    {
      "name": "get_dtf_context",
      "type": "mcp",
      "command": "python -m dtf_context_server"
    }
  ]
}
```

### Prompt no GitHub Copilot:

```markdown
Use .dtc/context.md e .dtc/architecture.md para gerar código alinhado.

Contexto do projeto:
- FastAPI v0.109+
- PostgreSQL with asyncpg
- JWT auth via OAuth2PasswordBearer

Gerar endpoint GET /comments/{post_id} conforme arquitetura em .dtc/architecture.md.
```

---

## 📚 Exemplo Completo de Uso com MCP

### Setup de projeto novo com DTF-MCP:

```bash
# 1. Criar estrutura inicial do projeto
mkdir new-project && cd new-project
dtf init --template minimal > .gitignore

# 2. Gerar context.md inicial com MCP
@cursor ask dtf-context-server
"Gerar rascunho de .dtc/context.md para projeto Python/FastAPI/e-commerce"

# Output gerado em .dtc/context.md:
echo "# Contexto - E-Commerce API" > .dtc/context.md
# ... resto do arquivo gerado pelo MCP

# 3. Gerar templates com MCP
@cursor ask dtf-context-server  
"Gerar template DTC para este projeto"
cp ../templates/DTC-template.md .dtc/context.md

# Preencher com informações específicas do projeto
vi .dtc/context.md

# 4. Codar com IA alinhada à arquitetura
# Prompt no Cursor:
@cursor ask dtf-context-server
"Use .dtc/architecture.md para gerar código de user service"
```

### Fluxo completo de desenvolvimento com MCP:

```bash
# Fase 1: Criar .dtc/context.md inicial
@cursor ask dtf-context-server "Gerar context.md template baseado em projeto X"
vi .dtc/context.md  # Preencher detalhes específicos

# Fase 2: Documentar feature nova
@cursor ask dtf-context-server "Criar DTR-feature-auth-001 para login social"
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-auth-001.md
vi .dtc/tasks/DTR-feature-auth-001.md  # Preencher com requisitos

# Fase 3: Implementar DTI e código
@cursor ask dtf-context-server "Use DTR-feature-auth-001 para criar DTI"
cp ../templates/DTI-template.md .dtc/tasks/DTI-feature-auth-001.md
vi .dtc/tasks/DTI-feature-auth-001.md

# Gera estrutura de código sugerida no prompt de IA:
mkdir -p src/auth
touch src/auth/controllers.py
touch src/auth/services.py

# Fase 4: Codar com AI alinhada a DTF
@cursor ask dtf-context-server "Implementar endpoint POST /auth/social/{provider} conforme DTI"
# Cursor gera código com:
#   - Código alinhado a .dtc/architecture.md
#   - Patterns consistentes com .dtc/context.md section 4.1

# Fase 5: Criar DTA para validação
@cursor ask dtf-context-server "Gerar DTA conforme critério de aceitação"
cp ../templates/DTA-template.md .dtc/tasks/DTA-feature-auth-001.md
```

---

## 🎨 Diagrama de Fluxo com MCP

```
┌─────────────────┐
│  Nova Feature   │
└────────┬────────┘
         │
         ▼
┌───────────────────────────────────────┐
│  .dtc/ (Contexto do Projeto)           │
│  ├── context.md                        │
│  ├── architecture.md                   │
│  └── decisions/*.md                    │
└───────────────────────────────────────┘
         │
         ▼
┌───────────────────────────────────────┐
│  MCP Server (.dtc-context-server)      │
│  ├─ get_context()                     │
│  ├─ get_architecture()                │
│  └─ list_decisions()                  │
└───────────────────────────────────────┘
         │
         ▼
┌───────────────────────────────────────┐
│  Cursor AI / Copilot Workspace         │
│  "Use .dtc/context.md para gerar..."   │
└───────────────────────────────────────┘
         │
         ▼
┌───────────────────────────────────────┐
│  Código Gerado Alinhado                │
│  - Segue padrões de .dtc/context.md   │
│  - Arquitetura em .dtc/architecture.md│
│  - Decisões em .dtc/decisions/*.md    │
└───────────────────────────────────────┘
```

---

## 📝 Best Practices com MCP

### ✅ FAÇA

- Configure MCP server antes de usar IA para codificar novas features
- Sempre referencie `.dtc/context.md` nos prompts da IA
- Use tool `get_architecture()` antes de implementar componentes complexos
- Valide código gerado contra ADRs listados via `list_decisions`

### ❌ NÃO FAÇA

- Não dependente 100% da IA sem leitura de `.dtc/context.md`
- Não peça para IA "adivinhar" arquitetura do projeto (use MCP)
- Não ignorer ADRs existentes quando gerar código novo

---

## 🛠️ Debugging MCP

### Verificar connection:

```bash
# Testar se MCP server está respondendo:
curl http://localhost:8080/tools/list

# Expected response:
{
  "tools": [
    {"name": "get_context", ...},
    {"name": "get_architecture", ...}
  ]
}
```

### Log levels para debug:

```bash
python -m dtf_context_server --dtf-path .dtc/ --log-level DEBUG
```

---

> **"MCP transforma IA de ferramenta genérica em assistente contextualizado no seu projeto."**  
> Use `.dtc/` com MCP para gerar código alinhado à arquitetura, não aleatório.
