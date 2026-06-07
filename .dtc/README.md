# Sobre a Pasta `.dtc/`

## O que é `.dtc/`?

**`.dtc/` (Documentação Técnica de Contexto) é onde você guarda TODO o contexto específico deste PROJETO.**

É diferente da documentação do DTF em `foundation/` e `dtf/`, que explicam a metodologia.

---

## .dtc/ vs foundation/dtf/

| | `.dtc/` (projeto) | `foundation/` (metodologia) | `dtf/` (oficial) |
|--:|:--|:--|:--|
| **Escopo** | Específico deste projeto | Universal para todos os projetos | Especificação da metodologia |
| **Conteúdo** | Contexto do PROJETO | Fundamentação conceitual | Documentação oficial DTF |
| **Quando criar** | Cada projeto novo | Uma vez (repositório raiz) | Já existe na estrutura |
| **Atualizações** | Sempre que contexto muda | Raramente (padrões) | Apenas evoluções da metodologia |

---

## O que Fica em `.dtc/`

### Arquivos Principais

```
.dt c/
├── context.md      # ⭐ Contexto global do projeto
├── vision.md       # Visão e objetivos do projeto
├── scope.md        # Escopo e limites
├── architecture.md # Arquitetura do sistema
├── principles.md   # Princípios específicos do projeto
├── glossary.md     # Glossário de termos do projeto
├── decisions/      # ADRs (Architecture Decision Records)
│   ├── 001-integracao-http-axios.md
│   └── 002-database-postgresql.md
├── templates/      # Templates específicos do projeto
└── standards/      # Padrões do projeto
```

### Estrutura Detalhada

#### `.dtc/context.md` — O Coração

```markdown
# Contexto - [Nome do Projeto]

## Visão Geral
- **Problema**: O que este sistema resolve?
- **Stakeholders**: Quem usa e por quê?
- **Contexto de negócio**: Domínio do problema

## Arquitetura
- Tecnologias principais
- Padrões arquiteturais escolhidos
- Integrações externas

## Stack Tecnológico
- Linguagens e frameworks
- Banco de dados
- Infraestrutura/cloud
- Ferramentas CI/CD

## Convenções
- Convenções de código
- Estrutura de diretórios
- Git conventions
```

#### `.dtc/architecture.md` — O Mapa

Descreve componentes, interfaces, fluxos de dados. Inclui diagramas e ADRs importantes.

#### `.dtc/decisions/*.md` — Decisões Registradas

Cada decisão técnica importante:
- Contexto da decisão
- Alternativas consideradas
- Decisão tomada
- Justificativa

---

## Como Criar `.dtc/` em um Novo Projeto

### Passo a Passo

```bash
# 1. Inicializar estrutura
cd seu-novo-projeto
mkdir .dtc

# 2. Usar template DTC para começar
cp ../templates/DTC-template.md .dtc/context.md

# 3. Preencher com informações do projeto
vi .dtc/context.md  # Editar conforme necessário
```

### Alternativa: Criar Manualmente

```bash
cd seu-novo-projeto
mkdir .dtc context decisions templates standards

echo "# Contexto - [Nome do Projeto]" > .dtc/context.md
echo "" >> .dtc/context.md
echo "## Visão Geral" >> .dtc/context.md
# ... preencher com informações
```

---

## Quando Atualizar `.dtc/`

### Sempre que:

- ✅ **Nova tecnologia escolhida** → Atualize `context.md` stack section
- ✅ **Mudança de arquitetura significativa** → Crie novo ADR em `decisions/`
- ✅ **Novo bounded context/módulo** → Documente em `architecture.md`
- ✅ **Padrões importantes definidos** → Adicione a `standards/`
- ✅ **Requisitos fundamentais mudam** → Revise `context.md`, `vision.md`, `scope.md`

### Não precisa atualizar:

- ❌ Pequenos ajustes de feature (use DTR específico)
- ❌ Mudanças de implementação dentro da arquitetura
- ❌ Atualizações de versão do framework (a menos que mude comportamento)

---

## O Padrão do Mercado

Repositórios profissionais bem estruturados usam `.dtc/` ou `docs/architecture/`:

| Projeto | Estrutura equivalente |
|---------|----------------------|
| React Router docs | `architecture.md` |
| Node.js best practices | `principles.md`, `standards/` |
| Kubernetes patterns | `glossary.md`, `architecture.md` |
| ADR pattern | `.dtc/decisions/` |

**O DTF formaliza isso em um diretório único: `.dtc/`.**

---

## Backwards Compatibility

Se você já tem documentação espalhada:

```bash
# Migrar para .dtc/:
cp docs/architecture.md .dtc/architecture.md
cp docs/glossary.md .dtc/glossary.md
mv decisions/ .dtc/decisions/ 2>/dev/null || mkdir -p .dtc/decisions/

# Atualizar links:
sed -i 's|docs/\.md|.dtc/context.md|g' README.md
```

---

## Resumo

- **`.dtc/` é o coração do projeto** — guarda todo contexto específico
- **Crie em todos os projetos novos** — padrão do mercado
- **Atualize conforme mudanças significativas** — não cada detalhe
- **Use templates** para começar rápido e consistente

---

> **"Sem .dtc/, você depende da memória humana. Com .dtc/, o conhecimento sobrevive."**
