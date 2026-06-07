# Glossário DTF

Termos e definições fundamentais da metodologia Documentação Técnica Funcional.

---

## Termos Principais

### DTF (Documentação Técnica Funcional)

Metodologia de engenharia orientada por contexto para desenvolvimento de software humano e assistido por IA. Transforma conhecimento implícito em explícito antes da implementação.

---

### Contexto Técnico

O conhecimento necessário para entender, modificar e evoluir um sistema de software. Inclui arquitetura, decisões, padrões, e justificativas técnicas.

**Existem dois níveis de contexto:**
- **Contexto da Metodologia (DTF)** — Explicado nesta documentação
- **Contexto do Projeto (`.dtc/`) — Específico para cada projeto usando DTF**

---

### Fonte da Verdade

Documento ou conjunto de documentos que definem o estado autorizado do sistema. No DTF, a fonte da verdade é a documentação técnica (`.dtc/context.md`), não o código existente.

---

### Conhecimento Implícito

Conhecimento que existe apenas na memória de indivíduos, não documentado sistematicamente. Inclui decisões arquiteturais, escolhas de design, e intenções por trás do código.

**Problema:** Morre com as pessoas.

**Solução DTF:** Tornar explícito através da documentação.

---

### Conhecimento Explícito

Conhecimento documentado sistematicamente, acessível independentemente das pessoas que originalmente o criaram.

**Vantagem:** Sobrevive às mudanças de equipe.

---

### Decisão Técnica

Qualquer escolha sobre como estruturar ou construir um sistema: linguagem, framework, padrão de design, estrutura de dados, API shape, etc.

**Regra DTF:** Toda decisão técnica importante deve ser documentada com contexto e justificativa.

---

### Arquitetura

Estrutura geral de um sistema, incluindo componentes principais, suas responsabilidades, interfaces, e relações entre eles. No DTF, a arquitetura é definida antes da implementação em `.dtc/architecture.md`.

---

### Implementação Derivada

Código escrito como consequência de documentação técnica clara, não do vazio ou prompts ambíguos para IA.

**Contraste:** Código direto sem contexto → implementação derivada com context.

---

## Documentação Técnica (DTF Documents)

### DTC (Documento Técnico de Contexto)

Define arquitetura, padrões e estrutura do sistema. É a fonte da verdade arquitetural do projeto. Deve responder: qual problema o sistema resolve? Qual arquitetura é utilizada? Quais tecnologias são permitidas? Quais restrições existem?

---

### DTR (Documento Técnico de Requisito)

Define o problema ou funcionalidade específica a ser implementada. Inclui requisitos funcionais e não funcionais, casos de uso, e critérios de sucesso.

**Fluxo:** Contexto → **DTR** → Implementação

---

### DTI (Documento Técnico de Implementação)

Define a solução técnica detalhada para uma funcionalidade específica. Inclui abordagem escolhida, estrutura de código, algoritmos, integrações, e considerações técnicas.

**Fluxo:** Requisito → Análise → **DTI** → Implementação

---

### DTA (Documento Técnico de Aceitação)

Define critérios de validação para a implementação. Inclui critérios de aceitação, testes automatizados necessários, testes manuais requeridos, e métricas de performance.

**Fluxo:** Contexto → Requisito → **DTA** + DTI → Validar

---

## Conceitos Fundamentais

### Engenharia Orientada por Contexto

Abordagem onde documentação técnica explícita precede e guia a implementação. O contexto é primeiro-cidadão no processo de engenharia.

**Contra:** Engenharia baseada apenas em prompts ou memória humana.

---

### Desenvolvimento Assistido por IA

Desenvolvimento de software que utiliza ferramentas de IA generativa como parte do fluxo. Com DTF, a IA recebe contexto estruturado para gerar código alinhado à arquitetura.

**Regra:** IA deve consumir engenharia (documentação), não apenas prompts.

---

### Ciclo de Vida DTF

Ciclo completo de desenvolvimento usando DTF: Contexto → Requisito → Implementação → Aceitação → Código → Manutenção/Evolução.

**Diferente:** Processos ágeis tradicionais que frequentemente ignoram documentação pré-implementação.

---

## Metáforas e Analogias

### "Código é Consequência"

Assim como uma casa é consequência de projetos, escolhas, e materiais - não surge do vazio - código é consequência de decisões documentadas.

**Sem projeto:** Construção aleatória.

**Com projeto (DTF):** Construção intencional.

---

### "Documentação Produz Software"

Inverter a mentalidade tradicional. Não documentação como artefato de validação, mas como ferramenta de produção.

**Velho:** Codar → Testar → Documentar (para auditoria)
**Novo:** Documentar → Codar → Validar (com documentação viva)

---

### "IA Consome Engenharia"

IA generativa é poderosa quando alimentada com contexto estruturado, não apenas prompts vagos. DTF fornece esse contexto.

**Sem DTF:** *"Crie uma API de login"* → Código genérico
**Com DTF:** Contexto completo + especificação → Código alinhado

---

## Termos Relacionados

### ADR (Architecture Decision Record)

Registro documentado de decisões arquiteturais importantes, incluindo contexto, alternativas consideradas, e decisão final. Geralmente armazenado em `.dtc/decisions/` ou repositório paralelo `adr/`.

### Design Pattern

Padrão de design reconhecido que resolve problemas comuns de arquitetura. No DTF, os padrões devem ser documentados em `.dtc/architecture.md`.

### Tech Stack

Conjunto de linguagens, frameworks, ferramentas e tecnologias utilizadas no projeto. Deve ser documentado explicitamente em `.dtc/context.md`.

---

> *"Temos o conhecimento na documentação, não apenas nas pessoas."*
