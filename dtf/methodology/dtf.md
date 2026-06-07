# Metodologia DTF — Especificação Completa

Este documento descreve a metodologia Documentação Técnica Funcional em detalhes, incluindo fluxo completo de trabalho, exemplos práticos e diretrizes para adoção.

---

## Premissa Fundamental

**Documentação técnica estruturada deve guiar o desenvolvimento.**

A metodologia parte do princípio simples que **decisões técnicas devem ser registradas antes da implementação**, criando um contexto estruturado para ferramentas de IA e equipes humanas.

---

## Estrutura da Metodologia

### Quatro Documentos Técnicos

| Documento | Abreviação | Função |
|-----------|------------|---------|
| **Documento Técnico de Contexto** | **DTC** | Define arquitetura, padrões e estrutura do sistema. Fonte da verdade arquitetural. |
| **Documento Técnico de Requisito** | **DTR** | Define o problema ou funcionalidade a ser implementada. |
| **Documento Técnico de Implementação** | **DTI** | Define a solução técnica detalhada. |
| **Documento Técnico de Aceitação** | **DTA** | Define critérios de validação da implementação. |

### Fluxo de Engenharia

```markdown
Contexto → Requisito → Implementação → Aceitação → Código
         ↓      ↓             ↓          ↓         ↓
   .dtc/context.md  DTR/*.md   DTI/*.md  DTA/*.md  Código
```

---

## Documentação do DTC (.dtc/context.md)

**Objetivo**: Estabelecer a fundação técnica do sistema.

### Conteúdo Principal:

- **Visão Geral**: Propósito, escopo, stakeholders
- **Arquitetura**: Estrutura e componentes principais
- **Stack Tecnológico**: Linguagens, frameworks, banco de dados, infraestrutura
- **Convenções**: Código, organização de diretórios, Git, testes
- **Integrações**: APIs externas, sistemas legados, serviços de terceiros

### Quando Criar:

- ✅ Início do projeto novo
- ✅ Grandes refatorações (atualizar DTC existente)
- ✅ Mudanças significativas na arquitetura ou stack tecnológico

### Template Oficial:

Use [`templates/DTC-template.md`](../templates/DTC-template.md) como ponto de partida.

---

## Documentação do DTR (DTR-feature-X-001.md)

**Objetivo**: Definir claramente o que será implementado.

### Conteúdo Principal:

- **Descrição do problema ou funcionalidade**: O que resolve, por quê
- **Requisitos funcionais**: O que o sistema deve fazer
- **Requisitos não-funcionais**: Performance, segurança, etc.
- **Casos de uso**: Quem usa, como usam
- **Restrições e dependências**: Limitações do projeto

### Quando Criar:

- ✅ Para cada nova funcionalidade ou feature significativa
- ✅ Antes de implementar qualquer código novo para essa feature
- ✅ Após aprovação do DTC (verificar alinhamento com arquitetura)

### Fluxo Prático:

```bash
# Criar diretório para feature nova
mkdir .dtc/tasks/feature-authentication-001

# Copiar template e editar
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-auth-001.md
vi .dtc/tasks/DTR-feature-auth-001.md  # Preencher com requisitos
```

---

## Documentação do DTI (DTI-feature-X-001.md)

**Objetivo**: Detalhar como a solução será implementada.

### Conteúdo Principal:

- **Abordagem técnica escolhida**: Por que esta abordagem?
- **Estrutura de código e classes**: Organização de diretórios
- **Algoritmos e lógica**: Fluxos principais
- **Integrações com outros sistemas**: APIs, DB, serviços externos
- **Considerações de performance**: Métricas alvo, otimizações

### Quando Criar:

- ✅ Após aprovação do DTR (revisão completa)
- ✅ Antes de qualquer código ser implementado para feature
- ✅ Em conjunto ou antes de DTA (preferencialmente junto com)

### Fluxo Prático:

```bash
# Copiar template e editar
cp ../templates/DTI-template.md .dtc/tasks/DTI-feature-auth-001.md
vi .dtc/tasks/DTI-feature-auth-001.md  # Especificar implementação técnica
```

---

## Documentação do DTA (DTA-feature-X-001.md)

**Objetivo**: Definir como a implementação será validada.

### Conteúdo Principal:

- **Critérios de aceitação**: O que significa "feito" para essa feature
- **Testes automatizados necessários**: Unittests, integration tests
- **Testes manuais requeridos**: E2E flows críticos
- **Métricas de performance**: P95 latencies, throughput, etc.
- **Checklist de qualidade**: Code review checklist específico

### Quando Criar:

- ✅ Junto com o DTI (preferencialmente)
- ✅ Antes que feature seja marcada como "completed"
- ✅ Após implementação inicial (validação e iteração)

---

## Implementação Prática do Fluxo

### Exemplo de Ciclo Completo (Feature: Login Social OAuth2)

#### Passo 1: Criar DTC do Projeto (se novo projeto)

```bash
# No início do projeto, criar .dtc/context.md
cp ../templates/DTC-template.md .dtc/context.md
vi .dtc/context.md  # Preencher com stack tecnológico: FastAPI, PostgreSQL
```

#### Passo 2: Criar DTR para Feature Nova

```bash
# Definir feature nova (login social OAuth2)
cp ../templates/DTR-template.md .dtc/tasks/DTR-feature-auth-001.md

# Editar DTR com requisitos específicos
vi .dtc/tasks/DTR-feature-auth-001.md

# Preencher:
# - O que resolve: "Usuários querem login rápido via Google/GitHub"
# - Requisitos funcionais:
#   - RF-001: Autenticação OAuth2 com Google
#   - RF-002: Autenticação OAuth2 com GitHub
#   - RF-003: Linkar múltiplos providers
```

#### Passo 3: Revisar DTR (com equipe)

```markdown
# Checklist de revisão do DTR:
✅ Requisitos funcionais claros e mensuráveis?
✅ Casos de uso bem descritos?
✅ Restrições documentadas?
✅ Critérios de aceitação definidos?
```

#### Passo 4: Criar DTI para Feature

```bash
# Especificar implementação técnica antes de codar
cp ../templates/DTI-template.md .dtc/tasks/DTI-feature-auth-001.md

# Editar com abordagem escolhida e estrutura de código
vi .dtc/tasks/DTI-feature-auth-001.md

# Preencher:
# - Usar FastAPI OAuth2PasswordBearer + authlib
# - Estrutura: src/auth/{controllers, services, models}
# - Implementar PKCE conforme RFC7636
```

#### Passo 5: Criar DTA (junto com DTI)

```bash
# Definir critérios de aceitação antes de completar feature
cp ../templates/DTA-template.md .dtc/tasks/DTA-feature-auth-001.md

# Preencher checklist completo:
# [ ] OAuth2 flow completo para Google
# [ ] OAuth2 flow completo para GitHub  
# [ ] Account linking works
# [ ] PKCE implementation verified
# [ ] Token encryption validated
```

#### Passo 6: Implementar Código

```bash
# Agora codar seguindo especificação do DTI
mkdir -p src/auth/{controllers, services, models}
touch src/auth/__init__.py
# ... implementar conforme DTI ...
```

#### Passo 7: Revisar e Validar

```bash
# Code review usando DTA como checklist de qualidade
# Verificar critérios de aceitação um por um
pytest tests/unit/test_auth/
pytest tests/integration/test_oauth_flow.py
```

---

## Melhorias Práticas

### Documentos Eficazes:

- ✅ **Sejam concisos**: Informação necessária, sem excesso
- ✅ **Sejam específicos**: Evite ambiguidade ("fast database" → "PostgreSQL 15+")
- ✅ **Sejam atualizados**: Mantenha sincronia com o código (atualize `.dtc/context.md` quando mudar stack)
- ✅ **Sejam acessíveis**: Linguagem clara para toda a equipe

### Fluxo Eficiente:

- ✅ **Iterativo**: Pequenos ciclos de DTR → DTI → DTA, não documentar tudo no início
- ✅ **Colaborativo**: Revisão em cada etapa (code review do documento antes de codar)
- ✅ **Automatizado**: Templates e validação (GitHub Actions para verificar `.dtc/`)
- ✅ **Adaptável**: Ajuste conforme necessário (não seja rígido com templates)

### Integração com IA:

- ✅ **Contexto rico**: Forneça informações completas de `.dtc/context.md` + `.dtc/architecture.md`
- ✅ **Instruções claras**: Seja específico nas solicitações ("Use DTI para implementar")
- ✅ **Validação humana**: Revise código gerado contra checklist do DTA
- ✅ **Aprendizado contínuo**: Melhore prompts com base nos resultados

---

## Casos de Uso

### Desenvolvedor Solo:

**Benefícios**:
- Clareza de pensamento ao documentar antes de codar
- Base sólida para ferramentas de IA
- Manutenção futura facilitada pelo contexto explícito

**Fluxo simplificado para solo**:
```bash
# Feature nova rápida:
cp ../templates/DTR-template.md .dtc/tasks/dtr-feature-name.md
vi .dtc/tasks/dtr-feature-name.md  # Preencher requisitos

cp ../templates/DTI-template.md .dtc/tasks/dti-feature-name.md  
vi .dtc/tasks/dti-feature-name.md  # Especificar implementação técnica

mkdir -p src/{feature_name}         # Criar pasta do feature
# Codar seguindo DTI...
```

### Pequenas Equipes (<10 pessoas):

**Benefícios**:
- Alinhamento técnico entre membros
- Onboarding acelerado por contexto explícito
- Code reviews mais efetivas com checklist DTA

**Processo recomendado**:
- Revisão em equipe de DTR e DTI antes de implementar
- `.dtc/context.md` como fonte da verdade arquitetural acessível a todos
- Integração com CI/CD para validação automática (GitHub Actions)

### Projetos Open Source:

**Benefícios**:
- Contribuições alinhadas à arquitetura
- Documentação clara para comunidade
- Processo de contribuição estruturado e reproduzível

**Prática comum**:
- `.dtc/context.md` em repositório público
- Templates públicos na documentação do projeto
- ADRs documentam decisões complexas para contributors ler

### Startups:

**Benefícios**:
- Escalabilidade desde o início (arquitetura explícita não perde)
- Tomada de decisões explícitas para investimento em produto
- Adaptação rápida com contexto preservado

**Fluxo startup inicial**:
- `.dtc/context.md` define arquitetura desde o início (evita refatoração cara depois)
- Features incrementais via DTR → DTI → DTA
- Integração com IA para acelerar desenvolvimento com contexto estruturado

---

## Evolução da Metodologia

O DTF é uma metodologia viva, projetada para evoluir:

- ✅ **Feedback Prático**: Ajuste baseado em uso real (contribuições welcome no `templates/`, `examples/`, `ecosystem/`)
- ✅ **Ferramentas**: Suporte crescente para automação (CLI tools, MCP servers, CI validators)
- ✅ **Comunidade**: Contribuições e melhorias (GitHub issues, PRs, Discord community)
- ✅ **Casos de Uso**: Adaptação para diferentes contextos (solo dev vs. teams vs. startups)

---

## Conclusão

O **Documented Technical Flow**, agora traduzido como **Documentação Técnica Funcional**, transforma documentação de artefato posterior para parte ativa do processo de engenharia. Ao estruturar decisões técnicas antes da implementação, cria-se um ambiente mais previsível, auditável e colaborativo para desenvolvimento de software moderno.

A metodologia não impõe tecnologias específicas, mas estabelece princípios universais que se aplicam a diferentes stacks, equipes e contextos, tornando-se uma base sólida para o futuro do desenvolvimento assistido por IA.

---

> *"DTF: Documentação Técnica Funcional guiando o desenvolvimento moderno."*
