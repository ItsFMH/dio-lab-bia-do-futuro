# 💰 EconoAI - Mentor Financeiro Inteligente com Gen AI
O EconoAI é um agente de Inteligência Artificial Generativa projetado para transformar dados bancários estáticos em uma consultoria financeira proativa e humanizada. Utilizando a arquitetura RAG (Retrieval-Augmented Generation), o agente consome dados locais para oferecer insights personalizados ao usuário ItsFMH.

## 🎯 Caso de Uso
Diferente dos chatbots tradicionais, o EconoAI foca na contextualização do cliente:

Memória de Relacionamento: Identifica problemas técnicos passados, como o erro no extrato relatado em 22/09/2025, para validar a satisfação atual do usuário.

Personalização via Perfil de Risco: Cruza o perfil Moderado do cliente com metas reais (ex: R$ 50.000 para entrada de imóvel em 2027) antes de sugerir produtos.

Precisão nos Dados: Calcula dinamicamente o saldo disponível (R$ 2.511,10) a partir do processamento de entradas e saídas do arquivo de transações.

## 🛠️ Tecnologias Utilizadas
Python: Lógica de back-end e processamento de dados.

Streamlit: Interface de usuário e dashboard interativo.

Pandas: Manipulação de DataFrames para cálculos financeiros.

Gen AI / RAG: Engenharia de prompts para grounding e controle de alucinações.

## 🧠 Arquitetura de Prompts e Segurança
O agente foi configurado com Guardrails (trilhos de segurança) rigorosos:

Grounding Estrito: A IA responde apenas com base nos arquivos fornecidos. Se a informação não existe na base, ela admite o desconhecimento de forma profissional.

Admissão de Erro: O sistema possui um fluxo de feedback onde, se contestado pelo usuário, admite a possibilidade de falha e convida à revisão dos cálculos brutos.

Bloqueio de Risco: Filtros automáticos impedem a sugestão de ativos de risco 'Alto' para perfis que não comportam essa volatilidade.

## 🚀 Testes

### Teste 1
<img width="1365" height="616" alt="image" src="https://github.com/user-attachments/assets/57b47081-df29-48cf-b989-5a12e02f2ad8" />

### Teste 2
<img width="1365" height="628" alt="image" src="https://github.com/user-attachments/assets/6dd144a9-5149-4695-b090-a47eb2a08f0e" />

### Teste 3
<img width="1365" height="620" alt="image" src="https://github.com/user-attachments/assets/5857fb4a-fe0d-457e-9601-97a27d05052b" />

### Teste 4
<img width="1365" height="618" alt="image" src="https://github.com/user-attachments/assets/2fed12e5-0cd0-4b02-8479-59f8bdf38b2e" />

### Teste 5
<img width="1365" height="624" alt="image" src="https://github.com/user-attachments/assets/20372f2d-2c58-41a1-a8c7-db2d9d2e30c8" />

