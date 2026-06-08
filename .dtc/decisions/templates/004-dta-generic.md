# Template DTA (Documento Técnico de Aceitação) - Genérico

**Nota:** Este template é genérico para qualquer feature de validação. Substitua `[CURLASCOLETAS]` com valores reais.

---

## 1. Visão Geral da Aceitação

### 1.1 Feature para Validação
[C: **Descrição** — Implementar/upload/download/processamento de [feature_name]]

### 1.2 Objetivo de Validação
[C: **Finalidade** — Definir critérios objetivos para validar que a implementação atende aos requisitos do DTR e segue padrões arquiteturais]

### 1.3 Escopo da Validação
| Inclusivo | Exclusivo |
|-----------|-----------|
| [Funcionalidade A] | [Fora do escopo B] |
| [Funcionalidade C] | [Outro fluxo D] |

---

## 2. Critérios de Aceitação (Acceptance Criteria)

### AC-XXX: [NOME_DOC]

**Requisito do DTR:** [LINK_DO_REQUISITO]  
**Cenário de teste:** [DESCREVER_CENARIO]

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. [Ação inicial] | [Resultado esperado] | P0/P1/P2 |
| 2. [Próximo passo] | [Resultado esperado] | P0/P1/P2 |
| 3. [Validação final] | [Resultado esperado] | P0/P1/P2 |

**Acceptance test:**
```mermaid
[C: **Diagrama de sequência/fluxo do teste** — descreva ou inclua diagrama]
sequenceDiagram
    participant U as User
    participant S as System
    note over U,S: [DESCREVER_FLOUXO_DO_TESTE]
