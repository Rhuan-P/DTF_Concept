# Princípios Fundamentais do DTF

Estes princípios guiam a metodologia Documentação Técnica Funcional.

---

## P1 — Contexto precede implementação

**Toda implementação deve nascer de um contexto explícito.**

Antes de escrever código, pergunte:

- Qual é o problema que estou resolvendo?
- Quem vai usar isso e por quê?
- Como isso se conecta ao todo?
- Quais são as restrições e dependências?

**Sem contexto, o código é apenas código.**

---

## P2 — Decisões devem ser explícitas

**Arquitetura não pode viver apenas na memória da equipe.**

Cada decisão técnica importante deve ser:

1. **Documentada** — em `.dtc/` ou `.decisions/`
2. **Contextualizada** — por que foi tomada?
3. **Alternativa-considerada** — o que rejeitamos e por quê?
4. **Revisável** — qualquer pessoa pode entender a decisão

> "Uma arquitetura não documentada é uma dívida técnica garantida."

---

## P3 — Código é um artefato derivado

**Código é consequência de decisões técnicas documentadas.**

Fluxo correto:

```
Contexto → Decisão → Arquitetura → Implementação
```

Fluxo errado (o que o DTF evita):

```
Implementação → "Vou implementar, depois documentar"
```

O código não nasce do vazio. Nasce de documentação técnica clara.

---

## P4 — IA consome engenharia

**IA não deve consumir apenas prompts.**

**IA deve consumir contexto estruturado.**

Dar a uma IA: *"Crie uma API REST"* → Resultado aleatório.

Dar a uma IA:
```markdown
# Contexto (.dtc/context.md)
- Domínio: E-commerce de moda
- Stack: Python/FastAPI, PostgreSQL
- Arquitetura: Domain-driven design
- Principais entidades: Produto, Carrinho, Pedido, Cliente
```

→ Resultado alinhado e consistente.

**A IA é uma ferramenta poderosa quando alimentada com documentação técnica.**

---

## P5 — Evolução preserva contexto

**Mudanças não podem destruir decisões anteriores sem justificativa explícita.**

Ao refatorar ou evoluir um projeto:

- ✅ Documente o que mudou e por quê
- ✅ Atualize `.dtc/context.md` quando necessário
- ✅ Crie ADR (Architecture Decision Record) para mudanças arquiteturais
- ❌ Não apague documentação sem substituição

> "Evolução sem preservação é destruição."

---

## P6 — Documentação produz software

**A documentação existe para guiar implementação e validação.**

Documentação boa → Implementação mais rápida.

Documentação ruim → Implementação cheia de ambiguidade.

Documentação como artefato posterior → Dívida técnica.

**Inverta a mentalidade:**

- Velho: Escreva código, depois documente
- DTF: Documente primeiro, implemente depois

---

## Hierarquia dos Princípios

1. **Contexto (P1)** — A fundação de tudo
2. **Decisões Explícitas (P2)** — A arquitetura sobrevive
3. **Artefato Derivado (P3)** — Código vem depois
4. **Engenharia para IA (P4)** — Potencialize ferramentas
5. **Evolução Preservadora (P5)** — Mantenha o contexto vivo
6. **Documentação como Produção (P6)** — Escreva para construir

---

> *"Princípios, não regras. Aplique conforme o contexto do seu projeto."*
