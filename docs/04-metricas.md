# Avaliação e Métricas

## Cenários de Teste Realizados

### Teste 1: Memória de Atendimento
- **Pergunta:** "Qual foi meu último problema relatado?"
- **Resposta esperada:** "Seu último registro foi em 22/09 sobre um erro ao visualizar o extrato, que já consta como resolvido."
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 2: Segurança de Perfil
- **Pergunta:** "Posso investir em ações?"
- **Resposta esperada:** O agente deve alertar que o perfil do cliente é Conservador e sugerir Renda Fixa em vez de ações.
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 3: Cálculo
- **Pergunta:** "Qual meu saldo disponível?"
- **Resposta esperada:** R$ 2.511,10.
- **Resultado:** [x] Correto [ ] Incorreto

## Resultados
- **O que funcionou bem:** A leitura das colunas `tema` e `resumo` do CSV de histórico permitiu uma saudação muito mais personalizada.