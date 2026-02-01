# Documentação do Agente: EconoAI

## Caso de Uso
O **EconoAI** resolve a falta de proatividade no setor financeiro. Ele atua como um mentor que analisa o histórico de gastos (`transacoes.csv`) e o histórico de suporte (`historico_atendimento.csv`) para oferecer recomendações que respeitam o perfil de risco do cliente (`perfil_investidor.json`).

## Persona e Tom de Voz
- **Persona:** Mentor Financeiro.
- **Tom de Voz:** Seguro, direto, empático e focado em dados. Ele evita termos excessivamente técnicos, mas mantém o profissionalismo bancário.

## Arquitetura
O agente utiliza uma arquitetura **RAG (Retrieval-Augmented Generation)**:
1. O usuário faz uma pergunta.
2. O sistema filtra os CSVs e JSONs locais.
3. Os dados são injetados no context window da LLM.
4. O agente gera uma resposta personalizada e proativa.

## Segurança e Anti-alucinação
- **Grounding:** O agente é instruído via System Prompt a responder apenas com base nos arquivos fornecidos.
- **Guardrails de Risco:** Bloqueio de sugestões de Renda Variável para usuários com perfil identificado como "Conservador".