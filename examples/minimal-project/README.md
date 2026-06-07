# Minimal Project — Exemplo de Projeto Mínimo com DTF

Este é um exemplo de projeto mínimo que implementa a metodologia DTF (Documentação Técnica Funcional) com todos os artefatos necessários.

---

## 📁 Estrutura do Projeto

```
minimal-project/
├── .dtc/                      # Contexto específico deste projeto ⭐
│   ├── README.md             # Explica o propósito do .dtc/
│   ├── context.md            # Visão geral do contexto do projeto
│   ├── architecture.md       # Arquitetura detalhada
│   └── decisions/            # ADRs (Architecture Decision Records)
├── src/                      # Código fonte
│   └── main.py               # Entry point
├── tests/                    # Testes unitários
├── docs/                     # Documentação geral
├── .gitignore                # Padrões de ignore do Git
└── README.md                 # Quick start para novos devs
```

---

## 🚀 Quick Start (5 minutos)

### 1. Clone o Projeto

```bash
git clone https://github.com/Rhuan-P/DTF_Concept.git
cd DTF_Concept/examples/minimal-project
```

### 2. Configure Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 4. Execute o Projeto

```bash
uvicorn src.main:app --reload
```

Acesse `http://localhost:8000` para ver a API funcionando.

---

## 📖 O que Aprender Aqui

### Conceitos do DTF Demonstrados

1. **`.dtc/` é o coração do projeto** — Todo contexto específico do projeto fica aqui
2. **Fluxo DTF**: Contexto → Requisito → Implementação → Aceitação → Código
3. **Documentação precede implementação** — Veja como os arquivos de `.dtc/` guiam a codificação

### Artefatos Demonstrados

- `.dtc/context.md`: Visão geral do contexto do projeto
- `.dtc/architecture.md`: Arquitetura detalhada do sistema
- `.dtc/decisions/*`: Decisões arquiteturais documentadas (ADRs)
- Templates DTF em `../templates/` para referência

---

## 📄 Exemplo de `.dtc/context.md`

Crie ou edite `.dtc/context.md` com esta estrutura:

```markdown
# Contexto - Minimal Project

## Visão Geral
Este projeto minimal demonstra a implementação da metodologia DTF (Documentação Técnica Funcional).

**Problema**: Muitos projetos ignoram documentação técnica antes da implementação, levando a código inconsistent e difícil de manter.

**Solução**: Este exemplo mostra como documentar contexto técnico explicitamente em `.dtc/`.

## Arquitetura
- **Linguagem**: Python 3.11+
- **Web Framework**: FastAPI v0.109+
- **Database**: SQLite (para simplicidade do exemplo)

## Stack Tecnológico
- Language: Python 3.11+
- Web Framework: FastAPI v0.109+
- Validation: Pydantic v2
- Testing: pytest + httpx

## Convenções
- Code style: Black + ruff
- Git: Conventional Commits (feat:, fix:, etc.)
- Testing: pytest com 80%+ coverage alvo
```

### Por que `.dtc/`?

`.dtc/` concentra TODO o contexto específico deste projeto:
- ✅ Visão deste projeto
- ✅ Arquitetura deste projeto
- ✅ Stack deste projeto
- ✅ Principípios deste projeto
- ❌ NÃO contém fundamentação da metodologia (isso fica em `foundation/`)

---

## 🔧 Exemplo de Decisão Arquitetural (`.dtc/decisions/001-database.md`)

```markdown
# ADR 001: Escolha de Banco de Dados

## Contexto
O projeto precisa escolher um banco de dados para persistência inicial.

## Alternativas Consideradas
| Option | Pros | Cons |
|--------|------|------|
| PostgreSQL | Production-ready, robust | Complexidade de setup |
| SQLite | Zero-config, ideal para exemplos | Não escalar bem em produção |
| MongoDB | Flexible schema | Different paradigm than relational DBs |

## Decisão
**SQLite** para o exemplo minimal.

**Justificativa**: 
- Zero configuration required (ideal para learning example)
- No additional dependencies (keeps example simple)
- Still ACID compliant and reliable

## Trade-offs
- **Benefit gained**: Simplicidade de deploy e setup
- **Cost accepted**: Não escalar em produção sem upgrades arquiteturais futuros
```

---

## 📋 Referências

### Templates Oficiais DTF

Use estes templates para expandir este exemplo:

| Template | Uso |
|----------|------|
| `../templates/DTC-template.md` | Expansão completa do context.md |
| `../templates/DTR-template.md` | Criar novas features (requisitos) |
| `../templates/DTI-template.md` | Especificação de implementação de feature |
| `../templates/DTA-template.md` | Validação de feature implementada |

### Guia de Uso do DTF

Para aprender mais sobre a metodologia:

- [README principal](../../README.md) — Portal oficial da metodologia
- `foundation/manifesto.md` — O que acreditamos
- `foundation/principles.md` — Princípios fundamentais
- `methodology/workflow.md` — Fluxo de trabalho DTF

### Exemplos Adicionais

| Exemplo | Propósito |
|---------|-----------|
| `feature-example/` | Adicionar uma nova feature usando DTF |

---

## 🛠️ Próximo Passos

Para transformar este exemplo minimal em projeto real:

1. **Expanda `.dtc/context.md`**:
   - Adicione stack completo (database, cache, etc.)
   - Defina convenções específicas do projeto
   - Documente padrões de code

2. **Crie `.dtc/decisions/`**:
   - Decisão 001: Escolha de banco de dados
   - Decisão 002: API versioning strategy
   - Decisão 003: Error handling approach

3. **Use templates para novas features**:
   ```bash
   # Criar nova feature: user management
   cp ../templates/DTR-template.md .dtc/tasks/user-management-DTR.md
   
   # Editar com detalhes do requisito da feature
   vi .dtc/tasks/user-management-DTR.md
   ```

---

> **"Este exemplo minimal demonstra a estrutura `.dtc/` como coração do projeto DTF."**  
> Expanda conforme o projeto cresce, mantendo todos os contextos em `.dtc/`.
