# Fundamentação Conceitual — dtf/context/

Esta pasta contém a fundamentação conceitual da metodologia Documentação Técnica Funcional. Explica o **porquê** do DTF, não apenas o **como**.

---

## 📖 Arquivos nesta pasta:

| Arquivo | Propósito |
|---------|----------|
| [vision.md](vision.md) | Visão geral e objetivos da metodologia |
| [scope.md](scope.md) | Escopo de aplicação, limites, casos de uso |
| [principles.md](principles.md) | Princípios fundamentais do DTF |
| [architecture.md](architecture.md) | Arquitetura dos documentos DTC/DTR/DTI/DTA |
| [glossary.md](glossary.md) | Glossário de termos e definições |

---

## 📄 vision.md — Visão e Objetivos

[Consulte `foundation/vision.md` ou `.dtc/context.md` para visão atualizada.]

**Resumo**: O DTF (Documentação Técnica Funcional) é uma metodologia de engenharia orientada por contexto que transforma conhecimento implícito em explícito antes da implementação.

**Objetivos principais**:
- Estruturar desenvolvimento assistido por IA
- Tornar arquitetura explícita e preservável
- Melhorar compreensão de sistemas complexos
- Facilitar onboarding de novos desenvolvedores
- Reduzir inconsistências arquiteturais

---

## 📄 scope.md — Escopo e Aplicabilidade

[Consulte `foundation/manifesto.md` ou `.dtc/context.md` para escopo atualizado.]

**O DTF se aplica a**:
- ✅ Desenvolvedores solo (side projects, learning)
- ✅ Pequenas equipes (<10 pessoas)
- ✅ Projetos open source
- ✅ Startups em fase inicial
- ✅ Teams que utilizam ferramentas de geração de código por IA

**O DTF NÃO substitui**:
- ❌ Frameworks ou padrões de arquitetura existentes (DDD, microservices, etc.)
- ❌ Processos ágeis ou workflows DevOps
- ❌ Ferramentas de versionamento (Git)
- ❌ Testes automatizados

**O DTF complementa**:
- ✅ Documentação existente (README, docs/, ARCHITECTURE.md antigo)
- ✅ Processos de code review (mais estruturado)
- ✅ CI/CD pipelines (validação pré-merge)
- ✅ Ferramentas de IA generativa (contexto rico para geração mais precisa)

---

## 📄 principles.md — Princípios Fundamentais

[Consulte `foundation/principles.md` ou `.dtc/context.md` para princípios atualizados.]

**Princípios do DTF**:
1. **Contexto precede implementação** — Toda implementação deve nascer de um contexto explícito
2. **Decisões devem ser explícitas** — Arquitetura não pode viver apenas na memória da equipe
3. **Código é um artefato derivado** — Código é consequência de decisões técnicas documentadas
4. **IA consome engenharia** — IA deve consumir contexto estruturado, não apenas prompts
5. **Evolução preserva contexto** — Mudanças não podem destruir decisões anteriores sem justificativa explícita
6. **Documentação produz software** — A documentação existe para guiar implementação e validação

---

## 📄 architecture.md — Arquitetura da Metodologia

[Consulte `foundation/philosophy.md` ou `.dtc/architecture.md` para arquitetura do projeto.]

**Arquitetura dos documentos DTF**:

```
DTF Methodology Architecture
├── Contexto (.dtc/context.md)
│   ├── Visão Geral
│   ├── Arquitetura
│   ├── Stack Tecnológico
│   └── Convenções
│
├── Requisito (DTR/*.md)
│   ├── Problema a Resolver
│   ├── Requisitos Funcionais
│   └── Requisitos Não-Funcionais
│
├── Implementação (DTI/*.md)
│   ├── Abordagem Técnica
│   ├── Estrutura de Código
│   └── Considerações Técnicas
│
└── Aceitação (DTA/*.md)
    ├── Critérios de Aceitação
    └── Testes e Validação
```

---

## 📄 glossary.md — Glossário

[Consulte `foundation/glossary.md` ou `.dtc/glossary.md` para glossário atualizado.]

**Termos principais**:
- **DTC**: Documento Técnico de Contexto (font da verdade arquitetural)
- **DTR**: Documento Técnico de Requisito (define o problema/feature)
- **DTI**: Documento Técnico de Implementação (solução técnica detalhada)
- **DTA**: Documento Técnico de Aceitação (critérios de validação)

---

> **"A fundamentação em `dtf/context/` explica a metodologia. O contexto em `.dtc/` documenta o projeto específico."**
