# Princípios Fundamentais do DTF

Os princípios abaixo guiam a metodologia Documentação Técnica Funcional (DTF). Eles não são regras rígidas, mas diretrizes para aplicação conforme o contexto de cada projeto.

---

## P1 — Contexto precede implementação

**Toda implementação deve nascer de um contexto explícito.**

### Princípio
Antes de escrever código, pergunte:
- Qual é o problema que estou resolvendo?
- Quem vai usar isso e por quê?
- Como isso se conecta ao todo?
- Quais são as restrições e dependências?

### Aplicação Prática
```markdown
# .dtc/context.md deve conter:
- Visão geral do projeto
- Arquitetura escolhida
- Stack tecnológico (linguagens, frameworks, DB)
- Convenções de código e organização de diretórios

# Criar DTR antes de implementar feature nova:
cp ../templates/DTR-template.md .dtc/tasks/feature-name-DTR.md
# Preencher com requisitos da feature
```

### Pitfall
❌ **Código primeiro, documentação depois**:  
"Vou codar e depois documentar" → resultado: conhecimento morre com a implementação.

✅ **Documentação primeiro, código depois**:  
`.dtc/context.md` → DTR específico → DTI de implementação → Código → DTA de validação

---

## P2 — Decisões devem ser explícitas

**Arquitetura não pode viver apenas na memória da equipe.**

### Princípio
Cada decisão técnica importante deve ser:
1. **Documentada** — em `.dtc/decisions/` (ADRs)
2. **Contextualizada** — por que foi tomada?
3. **Alternativa-considerada** — o que rejeitamos e por quê?
4. **Revisável** — qualquer pessoa pode entender a decisão

### Aplicação Prática
```bash
# Criar ADR para decisões arquiteturais importantes:
cp ../templates/ADR-template.md .dtc/decisions/001-database-choice.md

# Conteúdo do ADR deve incluir:
- Contexto da decisão (por que precisamos decidir isso?)
- Alternativas consideradas (com prós e contras)
- Decisão tomada
- Justificativa para a decisão
```

### Pitfall
❌ **Arquitetura viva na memória**:  
"Ah, aquele sistema usa PostgreSQL porque era mais rápido, né?" → morre com o time.

✅ **Decisões documentadas**:  
`.dtc/decisions/001-database-choice.md` → novo dev lê e entende contexto imediatamente.

---

## P3 — Código é um artefato derivado

**Código é consequência de decisões técnicas documentadas.**

### Princípio
O fluxo correto:

```markdown
Contexto → Decisão → Arquitetura → Implementação → Código
       ↓           ↓            ↓              ↓
   .dtc/      ADRs         .dtc/architecture  DTI
                                            DTA (validação)
```

Fluxo errado (o que o DTF evita):

```markdown
Implementação → "Vou codar, depois documentar" → Dívida técnica acumulada
```

### Aplicação Prático
```python
# ❌ Código sem contexto:
def process_user_data(user):  # Por que esta função? O quê ela faz?
    return {"id": user["id"], "name": user["name"]}  # Magic?

# ✅ Código com contexto (DTI documenta antes de codar):
# DTI-feature-user-api-001.md explica:
# - Função process_user_data normaliza dados conforme contrato API
# - Contrato definido em .dtc/architecture.md section 3.2
# - Padrão followa JSON schema em docs/API-contracts/
```

### Pitfall
❌ **Código como fonte da verdade**:  
"Este código faz assim porque foi decidido antes (mas não documentado)" → novo dev perde contexto.

✅ **Documentação como fonte da verdade**:  
".dtc/architecture.md diz que process_user_data normaliza dados conforme contrato API" → clareza explícita.

---

## P4 — IA consome engenharia

**IA não deve consumir apenas prompts. Deve consumir contexto estruturado.**

### Princípio
Dar a uma IA: *"Crie uma API REST para login"* → resultado aleatório.

Dar a uma IA com contexto:
```markdown
# .dtc/context.md fornece:
- Domain: E-commerce de moda feminina
- Stack: Python/FastAPI, PostgreSQL
- Arquitetura: Domain-driven design com bounded contexts
- Principais entidades: Produto, Carrinho, Pedido, Cliente

# Resultado: IA gera código alinhado e consistente
```

### Aplicação Prático
```bash
# Configurar MCP server para Cursor AI:
{
  "mcpServers": {
    "dtf-context": {
      "command": "python -m dtf_context_server",
      "env": {"DTF_PATH": ".dtc/"}
    }
  }
}

# Prompt no Cursor AI:
@cursor ask dtf-context-server
"Use .dtc/context.md e .dtc/architecture.md para gerar código alinhado."
```

### Pitfall
❌ **Prompts vazios sem contexto**:  
"Crie login OAuth2 com Google" → IA gera genérico, não alinhado ao projeto.

✅ **Contexto rico + prompts específicos**:  
"Use .dtc/context.md (stack: FastAPI v0.109+, DB: PostgreSQL) para implementar login social conforme DTR-feature-auth-001" → código alinhado.

---

## P5 — Evolução preserva contexto

**Mudanças não podem destruir decisões anteriores sem justificativa explícita.**

### Princípio
Ao refatorar ou evoluir um projeto:
- ✅ Documente o que mudou e por quê (em `.dtc/decisions/` ou ADI)
- ✅ Atualize `.dtc/context.md` quando necessário
- ✅ Crie ADR para mudanças arquiteturais importantes
- ❌ Não apague documentação sem substituição

### Aplicação Prático
```markdown
# Migração de SQL para AsyncORM:
# Criar ADR explicando mudança:
.dt c/decisions/002-migration-to-asyncorm.md

# Conteúdo do ADR:
## Contexto
Antigo ORM síncrono causa bloqueios em alta concorrência.

## Alternativas consideradas
1. AsyncORM (escolhido) - melhor performance async
2. SQLAlchemy core (alternativa leve)  
3. Retenção de ORM síncrono (opcional, mas não escolhido)

## Decisão tomada
Adotar AsyncORM para compatibilidade nativa com FastAPI.

## Impactos documentados
- Migration scripts necessários para converter models existentes
- Testes atualizados para usar async fixtures
```

### Pitfall
❌ **Refação sem documentação**:  
"Ah, agora vamos refatorar isso" → contexto perdido, novo dev confuso.

✅ **Evolução com ADRs**:  
".dtc/decisions/002-migration-to-asyncorm.md" → evolução documentada e compreensível.

---

## P6 — Documentação produz software

**A documentação existe para guiar implementação e validação.**

### Princípio
Inverter a mentalidade tradicional:

```markdown
# Velho (documentação como artefato posterior):
Codar → Testar → Escrever README → Atualizar docs após mudanças

# Novo (documentação como ferramenta de produção):
Documentar .dtc/ → Criar DTR → Elaborar DTI → Codar → Validar com DTA
         ↓              ↓             ↓          ↑        ↓
    (Fonte da       (Define      (Detalha      |         Critério
     verdade)       o quê         solução)     |         de aceitação)
```

### Aplicação Prático
```markdown
# Usar templates para documentação rápida:
cp ../templates/DTC-template.md .dtc/context.md  # Começar rápido
# Preencher com informações específicas do projeto
vi .dtc/context.md

# Para feature nova, criar DTR específico:
cp ../templates/DTR-template.md .dtc/tasks/new-feature-DTR.md
# Especificar requisitos antes de codar
```

### Pitfall
❌ **Documentação como artefato posterior**:  
"Escreverei README depois que o projeto estiver pronto" → nunca acontece, docs desatualizados.

✅ **Documentação como ferramenta de produção**:  
`cp ../templates/DTC-template.md .dtc/context.md` → documentação viva desde o início.

---

## Hierarquia dos Princípios

1. **Contexto (P1)** — A fundação de tudo
2. **Decisões Explícitas (P2)** — A arquitetura sobrevive
3. **Artefato Derivado (P3)** — Código vem depois
4. **Engenharia para IA (P4)** — Potencialize ferramentas
5. **Evolução Preservadora (P5)** — Mantenha o contexto vivo
6. **Documentação como Produção (P6)** — Escreva para construir

---

## Como Aplicar os Princípios

### Checklist de Adoção do DTF

```markdown
# Passo 1: Criar .dtc/ com context.md inicial
✅ Copiar template DTC
✅ Preencher com informações do projeto
✅ Salvar em .gitignore ou incluir conforme política

# Passo 2: Para feature nova, criar DTR específico
✅ Usar template DTR
✅ Especificar requisitos antes de codar
✅ Revisar com equipe (se houver)

# Passo 3: Elaborar DTI e implementar
✅ Definir abordagem técnica em DTI
✅ Criar ADR para decisões complexas
✅ Codar seguindo especificação do DTI

# Passo 4: Validar com DTA
✅ Especificar critérios de aceitação
✅ Escrever testes baseados em DTA
✅ Revisar implementação contra critério DTA

# Passo 5: Atualizar .dtc/ conforme necessário
✅ Decisões arquiteturais importantes → ADRs
✅ Mudanças significativas → atualizar context.md
✅ Review periódico da documentação
```

---

> *"Princípios, não regras. Aplique conforme o contexto do seu projeto."*
