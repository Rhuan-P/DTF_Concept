# DTF — Documentação Técnica Funcional

Uma metodologia de engenharia orientada por contexto para desenvolvimento de software humano e assistido por IA.

---

## 📖 O que é DTF?

O **DTF (Documentação Técnica Funcional)** é uma camada de engenharia que transforma conhecimento implícito em conhecimento explícito antes da implementação.

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

```
Contexto → Requisito → Implementação → Aceitação → Código
```

Os documentos técnicos são artefatos desse fluxo:

| Documento | Abreviação | Função |
|-----------|------------|---------|
| **Documento Técnico de Contexto** | **DTC** | Define arquitetura, padrões e estrutura do sistema. Fonte da verdade arquitetural. |
| **Documento Técnico de Requisito** | **DTR** | Define o problema ou funcionalidade a ser implementada. |
| **Documento Técnico de Implementação** | **DTI** | Define a solução técnica detalhada. |
| **Documento Técnico de Aceitação** | **DTA** | Define critérios de validação da implementação. |

---

## 📁 Estrutura do Repositório DTF

Todos os projetos que utilizam DTF devem ter esta estrutura:

```
seu-projeto/
├── .dtc/                          # ⭐ Contexto específico deste PROJETO
│   ├── context.md                 # Documentação principal do contexto
│   ├── vision.md                  # Visão e objetivos do projeto
│   ├── scope.md                   # Escopo e limites
│   ├── principles.md              # Princípios do projeto
│   ├── architecture.md            # Arquitetura do sistema
│   ├── glossary.md                # Glossário de termos
│   ├── templates/                 # Templates específicos do projeto
│   └── decisions/                 # Decisões arquiteturais (ADRs)
├── src/                           # Código fonte
├── tests/                         # Testes
├── docs/                          # Documentação geral
└── .dtc/README.md                 # ⭐ Explica a estrutura do .dtc/
```

### 📍 Onde é o `.dtc/`?

**`.dtc/` (Documentação Técnica de Contexto) é onde você guarda TUDO sobre seu projeto:**

- ✅ Arquitetura específica deste projeto
- ✅ Visão deste projeto  
- ✅ Escopo deste projeto
- ✅ Princípios deste projeto
- ✅ Decisões tomadas neste projeto
- ✅ Glossário específico deste projeto

**`.dtc/` é ESPECÍFICO DO PROJETO.** Não contém fundamentação da metodologia - isso fica na raiz do repositório DTF.

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

- **[dtf/context/](dtf/context/) **— Fundamentação conceitual detalhada**
  - [Visão e Objetivos](dtf/context/vision.md)
  - [Escopo e Aplicabilidade](dtf/context/scope.md)
  - [Princípios Fundamentais](dtf/context/principles.md)
  - [Arquitetura da Metodologia](dtf/context/architecture.md)
  - [Glossário](dtf/context/glossary.md)

- **[dtf/methodology/](dtf/methodology/) — Especificação completa**
  - [Metodologia DTF](dtf/methodology/dtf.md)
  - [Fluxo de Trabalho](dtf/methodology/workflow.md)

- **[dtf/standards/](dtf/standards/) — Padrões oficiais**
  - [Padrões de Documentação](dtf/standards/documentation.md)
  - [Estrutura de Repositórios](dtf/standards/repository.md)

### 4. Templates - `templates/`

Templates oficiais para criação dos documentos:

- [DTC-template.md](templates/DTC-template.md) — Template do Documento Técnico de Contexto
- [DTR-template.md](templates/DTR-template.md) — Template do Documento Técnico de Requisito  
- [DTI-template.md](templates/DTI-template.md) — Template do Documento Técnico de Implementação
- [DTA-template.md](templates/DTA-template.md) — Template do Documento Técnico de Aceitação

### 5. Exemplos Práticos - `examples/`

Veja casos de uso reais:

- [Projeto Mínimo](examples/minimal-project/) — Projeto mínimo com DTF
- [Feature Example](examples/feature-example/) — Adição de feature usando DTF

### 6. Ecossistema - `ecosystem/`

Ferramentas e integrações:

- [Extensões DTF](ecosystem/extension.md)
- [Automação via MCP](ecosystem/mcp.md)

### 7. Roadmap - `roadmap/`

Evolução da metodologia:

- [Evolução do DTF](roadmap/evolution.md)

---

## 🌟 Benefícios

### Para Desenvolvedores

- **Clareza**: Decisões técnicas explícitas antes do código
- **Consistência**: Arquitetura preservada ao longo do tempo
- **Eficiência**: Menos retrabalho e decisões improvisadas

### Para Equipes

- **Alinhamento**: Contexto compartilhado entre membros
- **Onboarding**: Nova equipe entende arquitetura rapidamente
- **Colaboração**: Base sólida para discussões técnicas

### Para Ferramentas de IA

- **Contexto Estruturado**: Informações organizadas para processamento
- **Decisões Explícitas**: Menos ambiguidade nas instruções
- **Qualidade**: Geração de código alinhada à arquitetura

---

## 🚀 Começando com DTF

### Para Novos Projetos

1. **Crie o `.dtc/`**: Defina contexto e arquitetura do projeto
2. **Estruture o Repositório**: Utilize o padrão `src/`, `tests/`, `.dtc/`
3. **Desenvolva Funcionalidades**: Siga o fluxo DTR → DTI → DTA
4. **Integre com IA**: Forneça contexto estruturado no `.dtc/`

### Para Projetos Existentes

1. **Documente Arquitetura**: Crie `.dtc/context.md` retroativo
2. **Estruture Novas Funcionalidades**: Aplique DTR → DTI → DTA
3. **Migre Gradualmente**: Adote DTF em novas implementações

---

## 💡 Filosofia

O DTF parte da premissa de que software é consequência de decisões.

> "Problemas de software raramente são problemas de implementação. Normalmente são problemas de contexto, entendimento, alinhamento ou arquitetura."

### Manifesto DTF

Acreditamos que:
- Código é consequência.
- Arquitetura é consequência.
- Qualidade é consequência.
- Tudo nasce da clareza do contexto.
- Nenhuma funcionalidade deve ser implementada sem contexto.
- Nenhuma decisão técnica deve permanecer implícita.
- Nenhuma IA deve gerar código sem arquitetura.
- Nenhum projeto deve depender da memória de indivíduos.
- O conhecimento do sistema deve existir fora das pessoas.
- O conhecimento deve existir antes do código.

---

## 🛠️ Exemplo de Uso

### Iniciando um Projeto Novo

```bash
# Criar estrutura básica
mkdir meu-projeto && cd meu-projeto
mkdir .dtc src tests
touch README.md LICENSE

# Iniciar documentação no .dtc/
cd .dtc
echo "# Contexto - Meu Projeto" > context.md
echo "# Visão do Projeto" > vision.md
echo "# Escopo" > scope.md
echo "# Arquitetura" > architecture.md
```

### Usando um Template

```bash
# Copiar template DTC
cp ../templates/DTC-template.md .dtc/context.md

# Preencher com informações do projeto
vi .dtc/context.md
```

---

## 📚 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para detalhes.

---

## ⭐ Contribua

O DTF é uma metodologia viva, projetada para evoluir:

- **Feedback Prático**: Ajuste baseado em uso real
- **Ferramentas**: Suporte crescente para automação
- **Comunidade**: Contribuições e melhorias
- **Casos de Uso**: Adaptação para diferentes contextos

---

> *DTF: Documentação Técnica Funcional guiando o desenvolvimento moderno.*
