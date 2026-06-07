# Agente DTF — Uso de IA no DTF

Este documento descreve como utilizar ferramentas de IA generativa de forma eficaz dentro da metodologia DTF.

---

## Premissa Fundamental

**IA consome engenharia, não apenas prompts.**

Ferramentas de IA são poderosas quando alimentadas com contexto estruturado. O DTF fornece esse contexto através de:

- `.dtc/context.md` — Visão geral do projeto
- `.dtc/architecture.md` — Arquitetura do sistema  
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
Contexto: E-commerce de moda (veja .dtc/context.md)
Stack: Python/FastAPI, PostgreSQL, JWT authentication
Arquitetura: Domain-driven design com bounded contexts
Requisito: Implementar endpoint POST /auth/login conforme DTR-feature-001
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

### 4. Itere com Contexto Atualizado

Após primeira implementação:

```
1. Revisão de código → Feedback para IA
2. Atualize .dtc/context.md se necessário
3. Novos requisitos → Novo DTR no .dtc/tasks/
4. Continue o ciclo
```

---

## Prompts Efetivos com DTF

### Ruim (Sem Contexto)

```
"Crie uma classe de usuário"
"Crie uma API para produtos"
"Crie testes para login"
```

**Resultado:** Código genérico, não alinhado ao projeto.

---

### Bom (Com Contexto DTF)

```markdown
# Contexto do Projeto (.dtc/context.md)
- Domínio: E-commerce de moda feminina
- Stack: Python 3.11+, FastAPI v0.109, SQLAlchemy 2.0, PostgreSQL
- Autenticação: JWT com refresh tokens, OAuth2 password flow
- Principais entidades: User, Product, Order, CartItem, Review
- DB Schema: /src/database/schemas.py
- API Spec: Swagger/OpenAPI conforme .dtc/context.md seção 4

# Tarefa
Implementar classe User conforme arquitetura em .dtc/architecture.md
Considerações do DTR-user-feature-001:
- Suporte a múltiplos emails por usuário
- Campos required: id, email, password_hash, created_at
- Métodos: create(), authenticate(), refresh_token()
```

**Resultado:** Código alinhado ao projeto.

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

## Exemplo de Sessão com IA

### Setup

```bash
# Ler o projeto antes de interagir com IA
cat .dtc/context.md
cat .dtc/architecture.md
ls .dtc/decisions/  # Ver decisões existentes
```

### Prompt para IA

```
Sou desenvolvedor iniciando nova feature no projeto DTF.

Contexto do sistema (de .dtc/context.md):
[RESUMO DE context.md]

Arquitetura relevante (de .dtc/architecture.md):
- Componente X: faz Y
- Interface entre X e Z: usa protocolo ABC

Decisões anteriores (de .dtc/decisions/):
- Decisão 1: Escolhemos FastAPI porque...
- Decisão 2: Padrão de autenticação é JWT porque...

Requisito da nova feature (do novo DTR):
[RESUMO do DTR]

Peço ajuda para:
1. Sugerir estrutura de código para esta feature
2. Verificar se alinha com a arquitetura existente
3. Sugerir testes unitários baseados em .dtc/context.md

Referências obrigatórias:
- DTF guidelines: ../templates/DTC-template.md
- Project architecture: ../.dtc/architecture.md
```

---

## Ferramentas Recomendadas

### Para Documentação Técnica

1. **GitHub Copilot / Cursor** — Autocompletar baseado em context `.dtc/`
2. **Codeium / Amazon Q** — IA com suporte a documentação local
3. **Custom LLM** — Fine-tuned sobre templates DTF e projetos anteriores

### Para Revisão

1. **Commitizen / Commitlint** — Padronizar commits conforme `.dtc/context.md`
2. **ESLint/Prettier + AI suggestions** — Code quality com IA
3. **Test generation tools** — Gerar testes baseados em DTA

---

## Limitações e Cuidados

### O que a IA NÃO substitui

- ✅ **IA não substitui**: Leitura de `.dtc/context.md`
- ✅ **IA não substitui**: Entendimento da arquitetura
- ✅ **IA não substitui**: Decisão técnica final (humano decide)
- ✅ **IA não substitui**: Contexto de negócio (só humanos têm)

### Quando IA falha sem DTF

Sem `.dtc/context.md`:

- Alucina APIs externas inexistentes
- Ignora padrões do projeto
- Replica código legado com bugs
- Esquece decisões arquiteturais importantes

**DTC é essencial para que IA não falhe.**

---

## Conclusão

O DTF transforma a relação com IA generativa:

- **Sem DTF:** IA = martelo (uso aleatório, resultados imprevisíveis)
- **Com DTF:** IA = faca de precisão (contexto estruturado, resultados alinhados)

**A IA é um acelerador de documentação técnica, não substituto dela.**

---

> *"Documente primeiro, peça ajuda depois."*
