# Fluxo de Trabalho da Metodologia DTF — Workflow Principal

Este documento descreve o fluxo de trabalho principal para adoção da metodologia Documentação Técnica Funcional em projetos reais.

---

## Visão Geral do Fluxo Principal (v1.0.0)

O fluxo DTF é projetado para ser iterativo e incremental, não oneroso:

```markdown
Problema → Contexto → Requisito → Aceitação → Implementação → Testes → Código
         ↓             ↓          ↓              ↓           ↓        ↓
     .dtc/context.md  DTR/*.md   DTA/*.md       DTI/*.md   Code    Tests
                                    ↑            ↑
                                    └─────────────┘
```

**Regra fundamental**: Nenhuma implementação deve iniciar sem contexto, requisito e validação definidos.

---

## Ordem Operacional Detalhada

### 1. Consultar ou Criar DTC (`.dtc/context.md`)

**Quando**: 
- Projeto novo → criar `.dtc/context.md` com stack tecnológico, convenções
- Feature nova que impacta arquitetura existente → verificar `.dtc/context.md`
- Grandes refatorações → atualizar `.dtc/context.md`

**Checklist DTC**:
```markdown
✅ Stack tecnológico documentado (linguagens, frameworks, DB)
✅ Convenções de código especificadas
✅ Estrutura de diretórios definida
✅ Integrações documentadas (APIs externas, sistemas legados)
```

---

### 2. Criar DTR (Detailed Task Request) (`.dtc/tasks/DTR-feature-X-001.md`)

**Quando**: Feature nova ou modificação significativa no escopo. O DTR deve ser um pedido de tarefa detalhado e formatado.

**Checklist DTR**:
```markdown
✅ Problema Proposto: Descrição clara do "o quê", "por que" e "como acontece".
✅ Detalhamento da Solicitação: Requisitos funcionais específicos e mensuráveis (nada de pedidos rasos).
✅ Lógicas e Regras: Descrição detalhada das regras de negócio, exceções e comportamentos esperados.
✅ Critérios de Sucesso (Negócio): O que o requerente espera ver funcionando.
✅ Referência ao Contexto: Deve apontar para o `.dtc/context.md` para contexto arquitetural.
```

---

### 3. Definir DTA (Design Task Acceptance) (`.dtc/tasks/DTA-feature-X-001.md`)

**Quando**: Junto com DTI, antes de completar feature. É o local onde o Cliente e o Dev entram em acordo sobre a validação.

**Checklist DTA**:
```markdown
✅ Critérios de Aceitação Objetivos: Como o requerente validará o sucesso (visão não técnica).
✅ Critérios de Validação Técnicos: Quais testes (unitários, integrados, E2E) devem passar (visão técnica).
✅ Resultado Esperado: Descrição clara do estado final desejado.
✅ Acordo de Validação: Assinatura ou validação mútua entre Requerente e Desenvolvedor.
```

---

### 4. Elaborar DTI (Design Technical Implementation) (`.dtc/tasks/DTI-feature-X-001.md`)

**Quando**: Após aprovação do DTR, antes da implementação. É a análise técnica do desenvolvedor.

**Checklist DTI**:
```markdown
✅ Análise de Contexto: Como essa tarefa se conecta ao DTC atual.
✅ Impacto em ADRs: Quais decisões arquiteturais foram afetadas ou precisam ser criadas.
✅ Plano de Implementação: Descrição técnica detalhada do "como" (nuances, estrutura de dados, chamadas de API, etc.).
✅ Riscos Técnicos: Identificação de possíveis gargalos ou riscos de performance/segurança.
```

---

### 5. Implementar (Codar)

**Quando**: Após aprovação do DTI, com checklist DTA em mente.

**Checklist implementação**:
```markdown
✅ Segue especificação técnica do DTI
✅ Testes escritos conforme DTA
✅ Code review baseado em critérios DTA
✅ Documentação atualizada se necessário (.dtc/context.md)
```

---

### 6. Executar Testes

**Quando**: Após implementar feature nova.

**Fluxo de teste**:
```bash
# Unit tests (conforme checklist do DTA):
pytest tests/unit/test_feature_name.py

# Integration tests:
pytest tests/integration/test_feature_integration.py

# E2E tests (critical paths):
pytest tests/e2e/test_feature_e2e.py
```

---

### 7. Validar Critérios de Aceitação

**Quando**: Após implementar e rodar testes.

**Checklist validação DTA**:
```markdown
✅ RF-001: [x] Critério de negócio 1 validado
✅ RF-002: [x] Critério de negócio 2 validado
✅ NFR-001: [x] Performance p95 < 500ms
✅ AC-001: [x] Critérios de aceitação do DTA passados
```

---

## Regra Fundamental

**Nenhuma implementação deve iniciar sem contexto, requisito e validação definidos.**

### Por quê?

- ❌ **Contexto implícito**: "Ah, o código já usa PostgreSQL, né?" → conhecimento morre com devs
- ❌ **Requisito vago**: "Crie algo para login" → código genérico, não alinhado ao projeto
- ❌ **Validação ad-hoc**: "Vou testar depois que codar" → bugs passados para produção

### Com DTF:

✅ **Contexto explícito**: `.dtc/context.md` define stack tecnológico, convenções  
✅ **Requisito específico**: DTR-feature-X-001.md especifica o quê será implementado  
✅ **Validação pré-definida**: DTA feature-X-001.md lista critérios de aceitação antes de codar
