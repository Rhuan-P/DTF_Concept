# Escopo e Aplicabilidade da Metodologia DTF

O **DTF (Documentação Técnica Funcional)** tem escopo claro: é uma metodologia complementar, não substituta, de processos existentes de desenvolvimento.

---

## O que o DTF Aborda (In-Scope)

### ✅ Documentação Pré-Implementação
- Definir arquitetura antes de codar
- Documentar decisões técnicas importantes
- Estabelecer convenções e padrões

### ✅ Fluxo de Desenvolvimento Estruturado
- Contexto → Requisito → Implementação → Aceitação → Código
- Uso dos documentos DTC, DTR, DTI, DTA como artefatos do fluxo

### ✅ Integração com Ferramentas de IA
- Fornecer contexto rico para geração de código alinhado
- Usar `.dtc/` como fonte da verdade para prompts de IA

### ✅ Preservação de Conhecimento
- Decisões arquiteturais documentadas e acessíveis
- Contexto técnico sobrevive às mudanças de equipe

---

## O que o DTF NÃO Aborda (Out-of-Scope)

### ❌ Substituir Processos Ágeis
O DTF **complementa** processos ágeis, não substitui:
- Não é um framework como Scrum ou Kanban
- Não define cerimônias (stand-ups, planning, etc.)
- Não substitui backlog management

### ❌ Testes Automatizados
O DTF **não substitui** testes automatizados:
- Não é ferramenta de unit testing
- Não define frameworks de testagem específicos
- Complementa com documentação para escrever melhores testes (via DTAs)

### ❌ Ferramentas de Versionamento
O DTF **complementa** Git, não substitui:
- Não é alternativa ao Git para versionamento
- Não gerencia histórico de commits automaticamente
- Integra com Git hooks para validação pré-commit

### ❌ DevOps/CI-CD Pipeline
O DTF **não define** pipelines de deploy ou CI/CD:
- Não inclui scripts de build ou deploy
- Não substituir ferramentas como GitHub Actions, Jenkins, etc.
- Complementa com validação documental antes do deploy

---

## Casos de Uso

### ✅ Desenvolvedor Solo

**Contexto**: Dev trabalhando sozinho, querendo garantir qualidade e alinhamento técnico.

**Como usar DTF**:
```bash
# Criar .dtc/ no projeto novo
mkdir .dtc && cd .dtc

# Usar template para contexto rápido
cp ../templates/DTC-template.md context.md

# Adicionar feature: criar DTR específico
cp ../templates/DTR-template.md tasks/feature-name-DTR.md
```

**Benefício**: Clareza de pensamento ao documentar antes de codar, base sólida para IA.

---

### ✅ Pequenas Equipes (<10 pessoas)

**Contexto**: Equipe pequena que precisa de alinhamento técnico e onboarding rápido.

**Como usar DTF**:
- `.dtc/context.md` como fonte da verdade arquitetural acessível a todos
- Code reviews baseados em `.dtc/architecture.md`
- DTAs definem critérios objetivos para PRs

**Benefício**: Alinhamento técnico entre membros, onboarding acelerado.

---

### ✅ Projetos Open Source

**Contexto**: Projeto open source com contribuintes distribuídos geograficamente.

**Como usar DTF**:
- `.dtc/` em repositório público como documentação clara para novos contribuintes
- Templates disponíveis para criar features novas de forma consistente
- ADRs documentam decisões complexas para comunidade ler

**Benefício**: Contribuições alinhadas à arquitetura, documentação para a comunidade.

---

### ✅ Startups

**Contexto**: Startup em fase inicial que precisa escalar rapidamente com qualidade.

**Como usar DTF**:
- `.dtc/context.md` define arquitetura desde o início (não refatorar depois)
- DTAs definem critérios de aceitação claros para features incrementais
- Integração com IA para acelerar desenvolvimento com contexto estruturado

**Benefício**: Escalabilidade desde o início, decisões explícitas, contexto preservado.

---

### ✅ Teams com Geração de Código por IA

**Contexto**: Equipe usando GitHub Copilot, Cursor AI, ou similar para geração de código.

**Como usar DTF**:
- `.dtc/` fornece contexto rico para prompts de IA (não genérico!)
- `.dtc/architecture.md` guia IA a gerar código alinhado à arquitetura
- ADRs documentam decisões que IA pode consultar antes de sugerir código

**Benefício**: Contexto estruturado para IA, menos ambiguidade nas instruções.

---

## Limitações Conhecidas

### ⚠️ Curva de Aprendizado Inicial

**Desafio**: Devs novos no DTF precisam entender o fluxo e usar templates corretamente.

**Mitigação**:
- Documentação em `foundation/` explica fundamentos
- Exemplos em `examples/` demonstram uso prático
- Templates bem estruturados guiam escrita de documentos

---

### ⚠️ Overhead de Documentação?

**Desafio**: Criar `.dtc/context.md`, DTRs, DTIs parece trabalho extra.

**Mitigação**:
- Começar pequeno: `.dtc/context.md` + 1 ADR para decisões críticas
- Usar templates para economizar tempo
- Integração com IA acelera documentação após configuração inicial

---

### ⚠️ Não é Framework Automático

**Desafio**: DTF não define convenções específicas de linguagem ou framework.

**Mitigação**:
- Projetado para ser adaptável a diferentes stacks
- Padrões definidos em `.dtc/context.md` (seção 4)
- Integrar com ferramentas existentes (Git, CI/CD, etc.)

---

## Integração com Ferramentas Existentes

### ✅ Git
O DTF **complementa** Git:
```bash
# Adicionar .gitignore para .dtc/:
echo ".dtc/" >> .gitignore  # Ou incluir conforme política do team

# Commit messages alinhados a convenções em .dtc/context.md:
git commit -m "feat(.dtc): add ADR for database choice"
```

### ✅ CI/CD (GitHub Actions, etc.)
O DTF **integra** com CI/CD:
```yaml
name: Validate DTF Documentation
on: [pull_request]
jobs:
  validate-dtf-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install dtf-validator && dtf validate .dtc/
```

### ✅ GitHub Copilot / Cursor AI
O DTF **alimenta** IA com contexto:
```bash
# Configurar MCP server para Cursor AI:
{
  "mcpServers": {
    "dtf-context": {
      "type": "stdio",
      "command": "python -m dtf_context_server",
      "env": {
        "DTF_PATH": ".dtc/"
      }
    }
  }
}
```

### ✅ Pytest / Testing Frameworks
O DTF **complementa** testes automatizados:
- DTAs definem critérios objetivos para escrever melhores testes
- Documentação clara facilita entendimento dos requisitos de teste

---

> **"O DTF complementa, não substitui. É uma camada de engenharia que transforma conhecimento implícito em explícito."**
