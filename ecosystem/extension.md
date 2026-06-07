# Ecossistema DTF — Ferramentas e Extensões

O ecossistema DTF oferece extensões, integrações e ferramentas que amplificam a metodologia Documentação Técnica Funcional.

---

## 📦 Extensões Oficiais

### 1. DTF Generator CLI

Ferramenta linha de comando para gerar esqueleto de documentação DTF rapidamente.

**Comandos disponíveis**:
```bash
# Gerar template DTC completo
dtf generate dtc --project "meu-projeto" > .dtc/context.md

# Gerar todos os templates
dtf generate all --output-dir docs/dtf/

# Exportar decisions para formato JSON
dtf export decisions --format json
```

**Instalação**:
```bash
pip install dtf-generator
```

### 2. DTF Linter

Verificador de qualidade de documentação DTF. Verifica se todos os artefatos estão consistentes.

**Uso**:
```bash
# Verificar consistência entre DTC, DTR, DTI, DTA
dtf lint .dtc/

# Saída exemplo:
✅ .dtc/context.md exists
✅ .dtc/architecture.md exists  
❌ .dtc/decisions/001-database.md missing (required by context)
✅ Templates updated to latest spec

# Fix automático de issues comuns
dtf lint --fix
```

### 3. DTF Validator (CI/CD)

Plugin para GitHub Actions que valida documentação antes de merge.

**Workflow exemplo**:
```yaml
name: DTF Validation
on: [pull_request]

jobs:
  validate-dtf-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install dependencies
        run: pip install dtf-validator pydantic
        
      - name: Validate .dtc/ documentation
        run: dtf validate .dtc/
      
      - name: Check for missing DTC
        if: github.event_name == 'pull_request'
        run: |
          if [ ! -f ".dtc/context.md" ]; then
            echo "❌ Missing .dtc/context.md in PR"
            exit 1
          fi
      
      - name: Validate template consistency  
        run: dtf lint --strict .dtc/
```

---

## 🔌 Integrações MCP (Model Context Protocol)

O DTF suporta integrações via **MCP** para ferramentas de IA. Configure um servidor MCP no seu repositório com:

### 1. MCP Server para `.dtc/`

Servidor MCP que fornece contextos estruturados para ferramentas de IA como Cursor, Copilot Workspace, etc.

**Configure `config.yaml`**:
```yaml
servers:
  dtf-context-server:
    type: stdio
    command: python -m dtf_context_server
    env:
      DTF_PATH: ".dtc/"
      
  dtf-decisions-server:
    type: stdio  
    command: python -m dtf_decisions_server
    env:
      DECISIONS_PATH: ".dtc/decisions"
```

**Funcionalidades do MCP**:

| Tool | Descrição |
|------|-----------|
| `get_context` | Ler `.dtc/context.md` para IA entender o projeto |
| `get_architecture` | Ler `.dtc/architecture.md` para alinhamento arquitetural |
| `list_decisions` | Listar todas ADRs em `.dtc/decisions/` |
| `validate_context` | Verificar se todos os requisitos do DTF estão documentados |
| `generate_dtc_draft` | Gerar rascunho inicial de context.md baseado em prompts |

### 2. Usando MCP com Cursor AI

No VS Code/Cursor:

```bash
# Configurar MCP no .cursor/rules:
{
  "mcpServers": {
    "dtf-context": {
      "type": "stdio",
      "command": "python -m dtf_context_server",
      "env": {
        "DTF_PATH": "${workspaceFolder}/.dtc/"
      }
    }
  }
}
```

**Prompt exemplo com MCP**:
```
@cursor ask dtf-context-server

Use .dtc/context.md e .dtc/architecture.md para gerar código alinhado à arquitetura do projeto. Se o contexto não estiver suficiente, pergunte ao usuário para adicionar documentação antes de codar.
```

---

## 🛠️ Ferramentas Recomendadas

### Para Gestão de Arquivos

| Tool | Uso com DTF | Por que usar |
|------|-------------|--------------|
| **VS Code** + Multi-cursor | Editar context.md e decisions/*.md lado a lado | Contexto completo visível |
| **Git + Conventional Commits** | `git commit -m "feat(.dtc): add ADR for database choice"` | Commit messages consistentes |

### Para Code Generation com IA

| Tool | Uso com DTF | Por que usar |
|------|-------------|--------------|
| **Cursor AI** | `@.dtc/context.md` + `.dtc/architecture.md` no prompt | Código alinhado à arquitetura do projeto |
| **GitHub Copilot** | Contexto rico em `.dtc/` para sugestões de código | Sugestões mais precisas e consistentes |

### Para Code Quality & Review

| Tool | Uso com DTF | Por que usar |
|------|-------------|--------------|
| **ESLint / Ruff + Pyright** | Linter verifica contra regras em `.dtc/context.md` section 4.1 | Consistência de código |
| **Prettier + daisyUI themes** | Formatting automático seguindo convenções do DTC | Código limpo e consistente |

### Para Testing & Validation

| Tool | Uso com DTF | Por que usar |
|------|-------------|--------------|
| **pytest** + `DTA-template.md` | Testes escritos baseados em critérios de aceitação | Testes alinhados à documentação |
| **httpx** | Async HTTP testing para APIs conforme DTI | Mocking fácil com async fixtures |

### Para CI/CD Validation

| Tool | Uso com DTF | Por que usar |
|------|-------------|--------------|
| **GitHub Actions + dtf-validator** | Validação pré-merge de `.dtc/` | Garante qualidade da documentação antes de deploy |
| **Codecov** | Coverage tracking para testes baseados em DTAs | Visualização clara de cobertura de testes |

---

## 📚 Templates Avançados

### DTF Template Generator

Extensão que gera templates personalizados para seus contextos:

```bash
dtf template generate \
  --base-template DTC-template.md \
  --output .dtc/templates/project-x-DTC.md \
  --config config/dtf-template-config.yaml
```

**Config de exemplo**:
```yaml
# config/dtf-template-config.yaml
project: "X-Project"
tech_stack:
  language: Python 3.11+
  framework: FastAPI
  database: PostgreSQL 15+
conventions:
  code_style: Black + ruff
  commit_message: Conventional Commits
test_framework: pytest
```

### DTF Decision Logger

Ferramenta CLI para documentar decisões arquiteturais rapidamente:

```bash
# Criar novo ADR interativo
dtf decision create \
  --context "Database choice for user project" \
  --alternatives "PostgreSQL, MongoDB, SQLite" \
  --chosen "PostgreSQL" \
  --output .dtc/decisions/YYYY-MM-DD-database.md

# Gerar ADR baseado em template pré-criteriado
dtf decision create \
  --template ddb-architecture.md \
  --project-domain user-management
```

---

## 🎨 IDE Extensions & Plugins

### VS Code

| Extension | Purpose |
|-----------|---------|
| **Markdown Preview Enhanced** | Preview `.dtc/*.md` com TOC, search, etc. |
| **Git Lens** | Contexto de git history para decisões documentadas |
| **Prettier** | Auto-formatting baseado em convenções do DTC |

### Neovim + Lazy.nvim

```lua
-- .config/nvim/lua/config/extensions/dtf.lua
return {
  "nvim-lualatex.lualatex",
  -- Configure dante renderer for markdown docs
}

-- Keybindings for DTF workflow:
vim.keymap.set("n", "<leader>dc", ":Telescope file find_dir_pattern='.dtc/decisions/'$")
vim.keymap.set("n", "<leader>dt", ":Telescope find_files pattern='.*template.md$'")
```

---

## 📊 Dashboards de Monitoramento DTF

### Grafana Dashboard para Saúde do DTF

| Metric | Query | Descrição |
|--------|-------|-----------|
| `documentation_coverage` | `SELECT COUNT(*) FROM files WHERE path LIKE '%.dtc/%'` | Cobertura de documentação existente |
| `adr_count` | `SELECT COUNT(*) FROM files WHERE path LIKE '%.dtc/decisions/*'` | Número de ADRs documentados |
| `dtr_to_code_ratio` | `(code_files / dtr_files) * 100` | Quantos DTRs por implementação (ideal ~1:1 para features novas) |

### Prometheus Metrics para CI/CD

```python
# src/metrics/dtf_metrics.py (para monitorar qualidade da documentação)
from prometheus_client import Counter, Gauge, Histogram

dtf_docs_written = Counter("dtf_docs_written", "Docs written by dtf")
dtf_validation_errors = Counter("dtf_validation_errors", "Validation errors caught")
dtf_coverage_score = Gauge("dtf_coverage_score", "Documentation coverage score 0-100")

def record_doc_written(doc_type: str):
    dtf_docs_written.labels(type=doc_type).inc()

def record_validation_error(error_type: str):
    dtf_validation_errors.labels(type=error_type).inc()
```

---

## 🔧 Ferramentas de Migracao

### DTF Migrate — Para Projetos Legados

Migrar projeto existente para estrutura `.dtc/`:

```bash
# Scan existing docs and migrate to .dtc/:
dtf migrate scan --dir ./src/docs/ --target-dir .dtc/

# Auto-generate ADRs from existing commit messages:
dtf migrate adr-extract --git-log --patterns="feat:.*architecture,refactor:.*design"

# Generate context.md from README + docs/:
dtf migrate generate-context --from README.md --include src/docs/architecture.md
```

### DTF Retroactive Analysis

Analisar projeto para identificar oportunidades de documentação retroativa:

```bash
dtf analyze --project ./my-legacy-project/ \
  --detect undocumented-decisions \
  --suggest-arcs \
  --output analysis.md
```

---

## 📖 Recursos Adicionais

### Webinars & Workshops DTF

| Webinar | Link | Quando |
|---------|------|--------|
| **Introdução ao DTF** | [youtube.com/watch?v=example-dtf-1](link) | Mensal |
| **MCP + IA para DTF** | [docs.nousresearch.com/dtf/mcp](docs-link) | Quarterly |

### Comunidade & Contribuição

```bash
# Join Discord channel #dtf-methodology
# Issues: https://github.com/Rhuan-P/DTF_Concept/issues
# PRs welcome to templates/, examples/, ecosystem/
```

---

## 🎯 Próximos Lançamentos (Roadmap)

| Feature | ETA | Status |
|---------|------|--------|
| DTF GitHub Action auto-generate context.md | Q3 2024 | 🚧 In development |
| DTF MCP server para Cursor AI | Q3 2024 | 🔜 Planned |
| DTF Validator com LLM analysis | Q4 2024 | 🚧 In development |

---

## 📝 Licença do Ecossistema DTF

As ferramentas e extensões do ecossistema estão licenciadas sob a mesma licença MIT. Consulte o arquivo [LICENSE](../../LICENSE) para detalhes.

---

> *"O ecossistema DTF cresce com você. Contribua, use as ferramentas que ampliam sua produtividade na documentação técnica."*
