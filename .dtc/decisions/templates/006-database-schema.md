# Template ADR para Database Schema (Feature Específica)

---

## Contexto e Background

[C: **Motivação** — Por que precisamos de novo schema/modificação?]

[C: **Status Atual** — Como dados são armazenados hoje?]

[C: **Objetivo** — O que queremos alcançar com este schema?]

---

## Proposta Esquema

```yaml
Schema Name: [NOME_DO_SCHEMA]
Type: [New Table | Modify Existing | Drop & Recreate | Index Creation]
Priority: [High | Medium | Low]
Estimated Effort: [1-2 days | 3-5 days | 1-2 weeks]
Dependencies: [List dependencies if any]
Risk Level: [Low | Medium | High]
```

### Table Definition (se nova tabela)
```sql
-- [NOME_DA_TABELA]
CREATE TABLE [schema_name].[nome_tabela] (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    
    -- Campos obrigatórios
    [campo_1] [tipo_dado] NOT NULL,
    [campo_2] [tipo_dado] DEFAULT [valor_default],
    
    -- Campos opcionais com nullability explícita
    [campo_3] [tipo_dado] REFERENCES [schema].[outros_tabela]([id]),
    [campo_4] JSONB NULL,
    
    -- Constraints
    CONSTRAINT [nome_constraint] CHECK (condicao),
    UNIQUE ([uniqueness_fields])
);

CREATE INDEX idx_[tabela]_[campo] ON [schema].[tabela] ([campo]);
```

### Schema Migration Plan
```
1. Backup existing data
2. Create new table with migration script
3. Migrate data (if applicable)
4. Update application code
5. Run tests
6. Drop old table (se aplicável)
```

---

## Relational Diagram (ERD)

```mermaid
erDiagram
    [TABELA_1] {
        bigint id PK
        string nome
        timestamp created_at
    }
    
    [TABELA_2] {
        bigint id PK
        bigint tabela_1_id FK
        string data
    }
```

---

## Trade-offs

| Consideração | Otimização Ganhada | Compromisso Feito |
|-------------|-------------------|-------------------|
| **Normalização** | Redundância mínima, dados consistentes | Joins necessários para queries complexas |
| **Desnormalização** | Queries mais rápidas | Possibilidade de dados inconsistentes |
| **Indexação** | Performance em reads altos | Overhead de write e storage maior |

---

## Decisões Chave

1. **D: [NOME_DA_DECISAO]**
   - **Descrição:** [Explique a decisão]
   - **Motivo:** [Por que foi tomada]
   - **Alternativas Consideradas:** [O que NÃO escolhemos]

---

## Checklist de Implementação

- [ ] Migration script testado em staging
- [ ] Rollback plan documentado
- [ ] Application code atualizado
- [ ] Tests existentes passando
- [ ] Documentation atualizada
- [ ] Monitoring/alerts configurados para nova tabela

---

## Checklist de Decisão

- [ ] A solução atende aos objetivos principais
- [ ] Trade-offs foram bem compreendidos
- [ ] Alternativas foram consideradas e comparadas
- [ ] Impacto na arquitetura está documentado
- [ ] Planos de rollback estão definidos

---

## Referências

[C: **Links para documentação relevante]

---

## Conclusão

[C: Resumo das conclusões e próximos passos]
