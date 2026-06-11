# Agente DTF — Uso de IA no DTF

Este documento descreve como utilizar ferramentas de IA generativa de forma eficaz dentro da metodologia DTF.

---

## Premissa Fundamental

**IA consome engenharia, não apenas prompts.**

Ferramentas de IA são poderosas quando alimentadas com contexto estruturado. O DTF fornece esse contexto através de:

- `.dtc/context.md` — Visão geral do projeto
- `.dtc/architecture.md` — Arquitetura detalhada
- `.dtc/decisions/*.md` — Decisões arquiteturais registradas

**Sem esses documentos, a IA gera código genérico.**

---

## Fluxo com IA no DTF

### 1. Forneça Contexto Completo

Antes de pedir geração de código:

```
✅ LEIA .dtc/context.md primeiro
✅ ENTENDA .dtc/architecture.md  
✅ REVISIE as decisões em .dtc/decisions/
```

**Errado:** *"Crie uma API REST para login"*
**Correto:** 
```markdown
Contexto do Projeto (.dtc/context.md)
- Domínio: E-commerce de moda feminina
- Stack: Python 3.11+, FastAPI v0.109, PostgreSQL, JWT authentication
- Arquitetura: Domain-driven design com bounded contexts
- Requisitos: Implementar endpoint POST /auth/login conforme DTR-feature-001
```

---

### 2. Use Templates do DTF

Para documentação técnica, **use os templates**:

```bash
# Criar DTC usando template
cat ../templates/DTC-template.md > .dtc/context.md

# Copiar para IA como contexto de referência
echo "Ref: ../templates/DTC-template.md" >> .dtc/CONTEXT_REF.txt
```

**A IA pode usar templates como referência:** *"Siga o formato do DTC-template.md"*

---

### 3. Valide com a Arquitetura

Quando IA gerar código, verifique:

- ✅ Alinha com `.dtc/architecture.md`?
- ✅ Segue padrões em `.dtc/context.md`?
- ✅ Respeita decisões registradas?
- ✅ Implementa o requisito do DTR?

**IA é ferramenta, não oráculo. Validação humana é essencial.**

---

## Melhores Práticas com IA

### ✅ FAÇA
- Leia `.dtc/context.md` antes de usar IA para um novo feature
- Use templates como ponto de partida
- Peça para IA revisar código contra `.dtc/architecture.md`
- Documente decisões da IA em `.dtc/decisions/`
- Atualize `.dtc/context.md` após grandes mudanças

### ❌ NÃO FAÇA
- Dependente 100% da IA sem leitura de documentação
- Usar prompts vagos sem contexto do projeto
- Aceitar código gerado sem validar contra arquitetura
- Deixar IA "alucinar" APIs externas sem verificar contra `.dtc/context.md`

---

## Conclusão

O DTF transforma a relação com IA generativa:

- **Sem DTF:** IA = martelo (uso aleatório, resultados imprevisíveis)
- **Com DTF:** IA = faca de precisão (contexto estruturado, resultados alinhados)

**A IA é um acelerador de documentação técnica, não substituto dela.**

---

## Contexto e Referências Técnicas

- **DTC (Design Thinking Context):** O "cérebro" do projeto. Contém a visão geral, stack tecnológica, convenções, regras de negócio e estado do sistema. É a fonte de verdade para a IA e para os desenvolvedores.
- **ADRs (Architecture Decision Records):** Registros permanentes de decisões arquiteturais. Devem ser consultados para entender o 'porquê' das decisões passadas e garantir consistência técnica no futuro.
