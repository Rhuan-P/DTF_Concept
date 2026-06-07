# Glossário de Termos DTF — Documentação Técnica Funcional

Este glossário define termos e conceitos importantes relacionados à metodologia DTF.

---

## DTF (Documentação Técnica Funcional)

**Definição**: Metodologia de engenharia orientada por contexto para desenvolvimento de software humano e assistido por IA, que transforma conhecimento implícito em explícito antes da implementação.

**Contexto**: O termo "DTF" foi adotado a partir de "Documented Technical Flow", uma metodologia criada originalmente como Documented Technical Flow (DTF) por Rhuan-P, posteriormente refinada pela LoopKode e expandida para ser um guia completo para desenvolvimento assistido por IA.

**Referências**:
- `foundation/dtf-agent.md` — Uso de IA no DTF
- `foundation/philosophy.md` — Filosofia do DTF
- `dtf/methodology/workflow.md` — Fluxo de trabalho detalhado

---

## Artefatos do DTF

### DTC (Documento Técnico de Contexto)

**Definição**: Define arquitetura, padrões e estrutura do sistema. É a fonte da verdade arquitetural do projeto.

**Conteúdo principal**:
- Arquitetura geral e padrões
- Tecnologias e frameworks utilizados
- Convenções de nomenclatura
- Estrutura de diretórios
- Princípios de design

**Quando criar**: Início do projeto ou grandes refatorações

**Referências**:
- `templates/DTC-template.md` — Template oficial completo
- `.dtc/context.md` — Exemplo em repositório atual (projeto)

### DTR (Documento Técnico de Requisito)

**Definição**: Define o problema ou funcionalidade específica a ser implementada. Inclui requisitos funcionais e não funcionais, casos de uso, e critérios de sucesso.

**Conteúdo principal**:
- Descrição do problema ou funcionalidade
- Requisitos funcionais e não funcionais
- Casos de uso
- Restrições e dependências
- Critérios de sucesso

**Quando criar**: Para cada nova funcionalidade ou modificação significativa

**Referências**:
- `templates/DTR-template.md` — Template oficial completo

### DTI (Documento Técnico de Implementação)

**Definição**: Define a solução técnica detalhada para implementar uma funcionalidade específica. Inclui abordagem escolhida, estrutura de código, algoritmos e considerações técnicas.

**Conteúdo principal**:
- Abordagem técnica escolhida
- Estrutura de código e classes
- Algoritmos e lógica
- Integrações com outros sistemas
- Considerações de performance

**Quando criar**: Após aprovação do DTR, antes da implementação

**Referências**:
- `templates/DTI-template.md` — Template oficial completo

### DTA (Documento Técnico de Aceitação)

**Definição**: Define critérios de validação para a implementação. Inclui critérios de aceitação, testes automatizados necessários, testes manuais requeridos, e métricas de performance.

**Conteúdo principal**:
- Critérios de aceitação
- Testes automatizados necessários
- Testes manuais requeridos
- Métricas de performance
- Checklist de qualidade

**Quando criar**: Junto com o DTI, antes da implementação (ou junto com DTR em alguns casos)

**Referências**:
- `templates/DTA-template.md` — Template oficial completo

---

## Conceitos Fundamentais

### Contexto Técnico

**Definição**: O conhecimento necessário para entender, modificar e evoluir um sistema de software. Inclui arquitetura, decisões, padrões, e justificativas técnicas.

**Níveis de contexto no DTF**:
1. **Contexto da Metodologia (DTF)** — Explicado nesta documentação (`foundation/`, `dtf/context/`)
2. **Contexto do Projeto** — Específico para cada projeto usando DTF (`.dtc/` no repositório)

### Fonte da Verdade

**Definição**: Documento ou conjunto de documentos que definem o estado autorizado do sistema. No DTF, a fonte da verdade é a documentação técnica (``.dtc/context.md``), não o código existente.

**Importância**: Permite que qualquer pessoa (humana ou IA) entenda o sistema sem depender da memória de indivíduos.

### Conhecimento Implícito vs. Explícito

#### Conhecimento Implícito

**Definição**: Conhecimento que existe apenas na memória de indivíduos, não documentado sistematicamente. Inclui decisões arquiteturais, escolhas de design, e intenções por trás do código.

**Problema**: Morre com as pessoas → refatoração difícil, onboarding lento, dívida técnica oculta.

#### Conhecimento Explícito

**Definição**: Conhecimento documentado sistematicamente, acessível independentemente das pessoas que originalmente o criaram.

**Vantagem**: Sobrevive às mudanças de equipe → conhecimento compartilhado, alinhamento garantido.

### Decisão Técnica

**Definição**: Qualquer escolha sobre como estruturar ou construir um sistema: linguagem, framework, padrão de design, estrutura de dados, API shape, etc.

**Regra DTF**: Toda decisão técnica importante deve ser documentada com contexto e justificativa (em `.dtc/decisions/` ou ADRs).

### Arquitetura (no DTF)

**Definição**: Estrutura geral de um sistema, incluindo componentes principais, suas responsabilidades, interfaces, e relações entre eles. No DTF, a arquitetura é definida **antes da implementação** em `.dtc/architecture.md`.

**Contraste**: 
- Com DTF: Arquitetura explícita documentada antes do código
- Sem DTF: Arquitetura viva na memória de desenvolvedores

### Implementação Derivada

**Definição**: Código escrito como consequência de documentação técnica clara, não do vazio ou prompts ambíguos para IA.

**Contraste**: 
- Com DTF: Contexto primeiro → implementação derivada
- Sem DTF: Prompt genérico → código aleatório sem contexto

---

## Processos e Fluxos

### Ciclo de Vida DTF

**Definição**: Ciclo completo de desenvolvimento usando DTF: Contexto → Requisito → Implementação → Aceitação → Código → Manutenção/Evolução.

**Fase por fase**:
1. **Contexto (.dtc/context.md)** — Fundamentação do projeto
2. **Requisito (DTR/*.md)** — O que será feito
3. **Implementação (DTI/*.md)** — Como será feito
4. **Aceitação (DTA/*.md)** — Como validar
5. **Código** — Implementação prática
6. **Manutenção/Evolução** — Volta ao passo 1 ou cria novo DTR

**Contraste**: Processos ágeis tradicionais frequentemente ignoram documentação pré-implementação; DTF inverte esta mentalidade.

### Engenharia Orientada por Contexto

**Definição**: Abordagem onde documentação técnica explícita precede e guia a implementação. O contexto é primeiro-cidadão no processo de engenharia.

**Contraste**: Engenharia baseada apenas em prompts ou memória humana (comum com IA, sem DTF).

### Desenvolvimento Assistido por IA

**Definição**: Desenvolvimento de software que utiliza ferramentas de IA generativa como parte do fluxo. Com DTF, a IA recebe contexto estruturado para gerar código alinhado à arquitetura.

**Regra fundamental**: "IA consome engenharia, não apenas prompts" → DTF fornece contexto estruturado.

---

## Estrutura e Organização

### ADR (Architecture Decision Record)

**Definição**: Registro documentado de decisões arquiteturais importantes, incluindo contexto, alternativas consideradas, e decisão final. Geralmente armazenado em `.dtc/decisions/` ou repositório paralelo `adr/`.

**Estrutura padrão**:
```markdown
# ADR {n}: {Short Description}

## Contexto
[Por que estamos tomando esta decisão?]

## Alternativas Consideradas
| Option | Pros | Cons |
|--------|------|------|
| ...    | ...  | ...  |

## Decisão Tomada
[Espaço da escolha final]

## Justificativa
[Por que esta escolha foi feita]

## Trade-offs
[Benefícios ganhos, custos aceitos]
```

### Design Pattern

**Definição**: Padrão de design reconhecido que resolve problemas comuns de arquitetura. No DTF, os padrões devem ser documentados em `.dtc/architecture.md` (seção 4) ou referenciados com links explícitos.

**Exemplos de design patterns mencionados no DTC**:
- Domain-Driven Design (DDD) — Para sistemas complexos com múltiplos bounded contexts
- CQRS — Quando separação leitura/escrita traz benefícios claros
- Clean Architecture / Hexagonal — Para desacoplamento entre domínio e infraestrutura

### Tech Stack

**Definição**: Conjunto de linguagens, frameworks, ferramentas e tecnologias utilizados no projeto. Deve ser documentado explicitamente em `.dtc/context.md` (seção 3).

**Categorização típica**:
- Linguagens e Frameworks
- Banco de Dados
- Infraestrutura / Cloud
- Ferramentas CI/CD
- Observabilidade (logging, metrics, tracing)

---

## Termos Relacionados ao DTF

### Documentação como Artefato Posterior vs. Primeiro-Cidadão

#### Como Artefato Posterior (Antigo modelo)

**Definição**: Prática de documentar apenas após implementação ("documento para auditoria").

**Problemas**:
- Documentação desatualizada rapidamente
- Código existente sem contexto
- Novos devs perdem tempo descobrindo "por que"
- IA gera código genérico sem compreensão do projeto

#### Como Primeiro-Cidadão (Novo modelo com DTF)

**Definição**: Prática de documentar **antes** implementação para guiar desenvolvimento.

**Benefícios**:
- Decisões arquiteturais explícitas antes da codificação
- Alinhamento garantido entre devs humanos e IA
- Conhecimento sobrevive a mudanças de equipe
- Menos dívida técnica, mais clareza

### Validação vs. Produção

#### Validação (DTA)

**Definição**: Fase onde critérios de aceitação são definidos para validar que a implementação atende aos requisitos do DTR.

**Artefato**: DTA (*Documento Técnico de Aceitação*)

#### Produção (Código)

**Definição**: Implementação final após validação e revisão.

**Fluxo**: Contexto → Requisito → Implementação → **Validação** → Código → Manutenção

### Observabilidade (no contexto DTF)

**Definição**: Conjunto de práticas e ferramentas para monitorar, debuggar, e entender o comportamento do sistema em produção.

**Componentes típicos em `.dtc/context.md`**:
- Logging — Centralized logging solution
- Metrics — Prometheus/Grafana ou equivalentes  
- Tracing — OpenTelemetry, Jaeger, etc.
- Alertas — Thresholds para alertar sobre problemas

---

## Metáforas e Analogias

### "Código é Consequência"

**Analogia**: Assim como uma casa é consequência de projetos, escolhas, e materiais — não surge do vazio — código é consequência de decisões documentadas.

**Sem DTF** ("Vou codar depois"):  
→ Construção aleatória, sem projeto, resultado imprevisível.

**Com DTF** (`.dtc/` primeiro):  
→ Projeto claro → construção intencional, resultados previsíveis.

### "Documentação Produz Software"

**Analogia**: Inverter a mentalidade tradicional onde documentação serve apenas para validar código depois feito.

**Velho** ("Codar → Testar → Documentar (para auditoria)"):  
→ Dívida técnica acumulada, documentação desatualizada.

**Novo** ("Documentar → Codar → Validar (com documentação viva)"):  
→ Documentação como ferramenta de produção, não apenas validação.

### "IA Consome Engenharia"

**Analogia**: Ferramenta culinária sem receita vs. com ingredientes e técnicas documentadas.

**Sem DTF** (*"Crie uma API REST"*):  
→ Martelo em busca de prenda → resultado genérico, não alinhado ao projeto.

**Com DTF** (`.dtc/context.md` completo):  
→ Faca de precisão com ingredientes claros, técnicas específicas → resultado alinhado e consistente.

---

## Referências Adicionais

- [Manifesto DTF](../foundation/manifesto.md) — O que acreditamos sobre software e engenharia
- [Princípios Fundamentais](principles.md) — Princípios do DTF aplicáveis a qualquer projeto
- [Escopo](scope.md) — Casos de uso, limites, integração com outras ferramentas
- [Arquitetura da Metodologia](architecture.md) — Especificação completa dos documentos e fluxos

---

> *"Temos o conhecimento na documentação, não apenas nas pessoas."*
