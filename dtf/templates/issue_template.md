# Template de Issue DTF

Para garantir a consistência e a qualidade técnica em todas as tarefas, cada issue deve seguir a estrutura abaixo.

## 📝 DTR (Detailed Task Request)
*Esta é a seção de detalhamento da requisição. Deve ser preenchida pelo Requerente/Product Owner.*

- **Problema Proposto:** Descreva o problema claramente. O que está acontecendo? Por que isso é um problema?
- **Contexto e Solicitação:** Descreva a solicitação de forma detalhada. Não aceite pedidos rasos (ex: "integrar pagamento"). Detalhe as regras de negócio, exceções e o fluxo desejado.
- **Lógicas e Regras:** Quais são as regras que regem essa tarefa? (Ex: Se o usuário fizer X, o sistema deve responder Y; Se o valor for > Z, aplicar regra W).
- **Critérios de Sucesso (Visão de Negócio):** O que o usuário final espera ver funcionando?

## 🛠️ DTI (Design Technical Implementation)
*Esta é a seção de análise técnica. Deve ser preenchida pelo Desenvolvedor/Engenheiro.*

- **Análise de Contexto:** Como essa tarefa se conecta ao DTC atual?
- **Impacto em ADRs:** Quais decisões arquiteturais foram afetadas ou precisam ser criadas?
- **Plano de Implementação:** Descreva as nuances técnicas, as tecnologias a serem usadas, as mudanças de banco de dados, APIs, etc.
- **Riscos Técnicos:** Identifique possíveis gargalos ou riscos de performance/segurança.

## ✅ DTA (Design Task Acceptance)
*Esta é a seção de validação e acordo. Deve ser revisada e aprovada por ambos (Requerente e Dev).*

- **Critérios de Aceitação Técnicos:** Como vamos testar que a implementação técnica está correta? (Ex: Teste unitário X, integração Y).
- **Critérios de Aceitação de Negócio:** Como o requerente validará que o problema foi resolvido?
- **Resultado Esperado:** Descreva o comportamento final esperado após a conclusão.

---
*Notas:*
- *Sempre consulte o **DTC** antes de iniciar o DTI.*
- *Decisões de arquitetura devem ser registradas como **ADRs**.*
