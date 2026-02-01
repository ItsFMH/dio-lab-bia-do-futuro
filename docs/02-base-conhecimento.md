# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e evitar repetição de problemas já resolvidos. |
| `perfil_investidor.json` | JSON | Garantir que recomendações respeitem o apetite ao risco do cliente. |
| `produtos_financeiros.json` | JSON | Consultar o catálogo oficial de investimentos disponíveis. |
| `transacoes.csv` | CSV | Analisar o fluxo de caixa e gerar insights proativos de economia. |

## Estratégia de Integração
Os dados são carregados via **Pandas** no início da sessão do Streamlit. Para otimizar o processamento, o histórico de atendimento é filtrado para mostrar apenas os últimos temas tratados (ex: CDB, Problema no app), garantindo que a IA tenha "memória" do relacionamento com o cliente.

## Exemplo de Contexto Montado
```text
Dados do Cliente: ItsFMH (Perfil: Moderado)
Último Atendimento: 22/09/2025 - Tema: Problema no app (Resolvido: Sim)
Saldo Atual: R$ 2.511,10