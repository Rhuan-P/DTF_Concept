# DTF — Documentação Técnica Funcional

Uma metodologia de engenharia orientada por contexto para desenvolvimento de software humano e assistido por IA.

---

## 📖 O que é DTF?

O **DTF (Documentação Técnica Funcional)** é uma camada de engenharia que
transforma conhecimento implícito em conhecimento explícito antes da
implementação.

> "Nenhuma implementação deve existir sem contexto, requisito e validação definidos."

---

## 🎯 O Problema

Grande parte dos problemas em projetos de software **não surge durante a implementação**. Surge **antes**:

- ❌ Requisitos implícitos
- ❌ Arquitetura não documentada
- ❌ Decisões contraditórias
- ❌ Perda de contexto
- ❌ Código gerado sem alinhamento arquitetural
- ❌ Dependência da memória de indivíduos

**A implementação é apenas a consequência.**

---

## 💡 A Premissa

> "Código é consequência. Arquitetura é consequência. Qualidade é consequência."

O DTF parte do princípio que **tudo nasce da clareza do contexto**.

### Princípios Fundamentais

- **P1 — Contexto precede implementação**
- **P2 — Decisões devem ser explícitas**
- **P3 — Código é um artefato derivado**
- **P4 — IA consome engenharia (não apenas prompts)**
- **P5 — Evolução preserva contexto**
- **P6 — Documentação produz software**

---

## 📋 Fluxo da Metodologia

### O Ciclo DTF

```bash
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────────┐
│  DTC    │ →  │   DTR   │ →  │  DTI    │ →  │   DTA    │
│Contexto │    │Requisito│    │Implantaç.│    │Aceitação │
└─────────┘    └──────────┘    └─────────┘    └──────────┘
```

| Documento | Pergunta Principal | Entregável Principal |
| ----------- | ------------------- | --------------------- |
| **DTC** (Contexto) | O QUE está sendo construído? | .dtc/context.md + decisões |
| **DTR** (Requisito) | COMO será implementado? | DTRs para features complexas |
| **DTI** (Implementação) | CÓDIGO finalizado | Código + exemplos de uso |
| **DTA** (Aceitação) | FUNCIONA conforme esperado? | Testes + checklist de validação |

> 📌 **Importante**: DTC é único por projeto. DTR/DTI/DTA são criados
conforme features evoluem!

---

## 🛠️ Ferramentas

### Para humanos

- GitHub Desktop (interface gráfica para Git)
- VSCodium + extensão Prettier/ESLint

### Para IA

- Prompt com contexto explícito via `.dtc/`
- ADRs como referência de decisões passadas

---

## 📦 Estrutura de Repositório

```bash
[Project Root]/
├── .dtc/                           # ⭐ DOCUMENTAÇÃO TÉCNICA DE CONTEXTO
│   ├── context.md                 # Fonte da verdade arquitetural + contexto geral
│   ├── vision.md                  # Visão e objetivos do projeto
│   ├── scope.md                   # O que está dentro/fora do escopo
│   ├── architecture.md            # Detalhes arquiteturais
│   ├── principles.md              # Princípios de design
│   ├── glossary.md                # Terminologia específica
│   └── decisions/                 # Decisões arquiteturais (ADRs)
│       ├── 001-database-choice.md # ADRs completos
│       └── ...
├── .dtc/examples/                 # Exemplos preenchidos de documentos (CRÍTICO!)
│   ├── context-md-exemplo-preenchido.md  # DTC COMPLETO PREENCHIDO
│   └── dta-template-exemplo-preenchido.md # DTA COMPLETO PREENCHIDO
├── templates/                     # Templates oficiais
│   ├── DTC-template.md            # Template vazio para novos projetos
│   ├── DTR-template-genérico-preenchido.md  # ⭐ TEMPLATE GENÉRICO
│   ├── DTI-template.md            # Template de implementação
│   ├── DTA-template.md            # Template de aceitação
│   └── ADR-template.md            # Template de decisão arquitetural
├── src/                           # Código fonte
├── tests/                         # Testes
├── docs/                          # Documentação geral
├── .gitignore                     # Padrão DTF
├── LICENSE                        # MIT License
└── README.md                      # Este arquivo (portal)
```

### 📍 Onde é o `.dtc/`?

**`.dtc/` (Documentação Técnica de Contexto) é onde você guarda
TUDO sobre seu projeto:**

- ✅ Arquitetura específica deste projeto
- ✅ Visão deste projeto
- ✅ Escopo deste projeto
- ✅ Princípios deste projeto
- ✅ Decisões tomadas neste projeto
- ✅ Glossário específico deste projeto

**`.dtc/` é ESPECÍFICO DO PROJETO.** Não contém fundamentação da
metodologia - isso fica na raiz do repositório DTF.

### 📋 Como Usar `.dtc/`

```bash
# Inicializar projeto com DTF
mkdir .dtc && cd .dtc

# Criar documentos principais
echo "# Contexto" > context.md
echo "# Visão" > vision.md
echo "# Escopo" > scope.md
echo "# Arquitetura" > architecture.md

# Ver templates disponíveis
cat ../templates/DTC-template.md  # Template completo do DTC
cat ../templates/DTR-template-genérico-preenchido.md  # ⭐ TEMPLATE GENÉRICO!
```

---

## 📖 Guia de Leitura

### 1. Fundamentação Conceitual - `foundation/`

Entenda os fundamentos da metodologia:

- [Manifesto](foundation/manifesto.md) — O que acreditamos sobre software e engenharia
- [Filosofia](foundation/philosophy.md) — Por que DTF existe
- [Princípios](foundation/principles.md) — Princípios fundamentais do DTF
- [Problema](foundation/problem.md) — Problemas resolvidos pelo DTF
- [Glossário](foundation/glossary.md) — Terminologia e definições
- [Agente DTF](foundation/dtf-agent.md) — Como usar IA com o DTF

### 2. Metodologia - `methodology/`

Aprenda a utilizar o DTF:

- [Introdução ao DTF](methodology/workflow.md) — Fluxo principal e uso
- [Ciclo de Vida](methodology/lifecycle.md) — Ciclo de vida dos projetos
- [Modelo de Decisão](methodology/decision-model.md) — Tomada de decisões no DTF
- [Desenvolvimento com IA](methodology/ai-assisted-development.md) — Integração com IA

### 3. Estrutura da Metodologia - `dtf/`

Documentação técnica oficial e especificação completa:

- **[dtf/context/](dtf/context/)** — Fundamentação conceitual detalhada
  - [Visão e Objetivos](dtf/context/vision.md)
  - [Escopo e Aplicabilidade](dtf/context/scope.md)
  - [Princípios Fundamentais](dtf/context/principles.md)
  - [Arquitetura da Metodologia](dtf/context/architecture.md)
  - [Glossário](dtf/context/glossary.md)
- **[dtf/methodology/](dtf/methodology/)** — Especificação completa
  - [Metodologia DTF](dtf/methodology/dtf.md)
  - [Fluxo de Trabalho](dtf/methodology/workflow.md)
- **[dtf/standards/](dtf/standards/)** — Padrões oficiais
  - [Padrões de Documentação](dtf/standards/documentation.md)
  - [Estrutura de Repositórios](dtf/standards/repository.md)

### 4. Templates - `templates/`

Templates oficiais para criação dos documentos:

- [DTC-template.md](templates/DTC-template.md) — Template do Documento Técnico de Contexto
- [DTR-template-genérico-preenchido.md](templates/DTR-template-genérico-preenchido.md) — ⭐ TEMPLATE GENÉRICO (upload, feature qualquer)
- [DTI-template.md](templates/DTI-template.md) — Template do Documento Técnico de Implementação
- [DTA-template.md](templates/DTA-template.md) — Template do Documento Técnico de Aceitação
- [ADR-template.md](templates/ADR-template.md) — Template de Decisão Arquitetural

### 5. Exemplos Práticos - `examples/`

Veja casos de uso reais:

- [Projeto Mínimo](examples/minimal-project/) — Projeto mínimo com DTF
- [Feature Example](examples/feature-example/) — Adição de feature usando DTF

### 6. Ecossistema - `ecosystem/`

Ferramentas e integrações:

- [Extensões DTF](ecosystem/extension.md)

### 7. Roadmap - `roadmap/`

Evolução da metodologia:

- [Evolução do DTF](roadmap/evolution.md) — Próximos passos no desenvolvimento

---

## 🚀 Começando Rápido

```bash
# Clonar repositório oficial DTF
git clone https://github.com/LoopKode/DTF-Method.git dtf-concept

cd dtf-concept/.dtc/examples

# Copiar exemplo de contexto preenchido para seu projeto novo
cp context-md-exemplo-preenchido.md ../context.md

# Iniciar feature complexa
cat ../templates/DTR-template-genérico-preenchido.md > .dtc/DTR-feature-upload-avatar-001.md
vi .dtc/DTR-feature-upload-avatar-001.md  # Editar conforme necessidade!

# Commit inicial
git add .dtc/context.md .dtc/DTR-feature-upload-avatar-001.md
git commit -m "feat(.dtc): add context + DTR para feature upload de avatar"
```

> ⚠️ **Importante**: Use `.dtc/examples/` como referência! Copie e edite, não comece do zero!

---

## ✅ Checklist de Qualidade

Antes de push, verifique:

- [ ] `.dtc/context.md` está atualizado com decisões arquiteturais
- [ ] DTRs usam placeholders genéricos (não hardcoded OAuth em features sociais)
- [ ] Templates disponíveis em `templates/` são genéricos e reutilizáveis
- [ ] Exemplos preenchidos em `.dtc/examples/` estão disponíveis
- [ ] ADRs em `.dtc/decisions/` explicam trade-offs com exemplos

---

## 🛠️ Contribuindo

Este repositório é um **portal da metodologia DTF**, não o código principal. Contribuições são bem-vindas!

### Como contribuir:

1. Fork este repositório
2. Crie branch de feature (`git checkout -b feature/amelioracao-dtr-template`)
3. Commit com convenção commits
4. Abra pull request

**Antes de criar PR:**

- [ ] Leia [Princípios da Metodologia](foundation/principles.md)
- [ ] Verifique se sua contribuição alinha ao manifesto ([manifesto.md](foundation/manifesto.md))
- [ ] Documente suas mudanças no `.dtc/decisions/` (ADR necessário)

---

## 📜 Licença

[MIT License](LICENSE) — Código e documentação sob MIT.

> "Software livre, conhecimento aberto, documentação como primeira classe."
