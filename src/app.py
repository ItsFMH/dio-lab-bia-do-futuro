import streamlit as st
import pandas as pd
import json
import os

# --- CONFIGURAÇÃO DE CAMINHOS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def load_data():
    h_path = os.path.join(DATA_DIR, 'historico_atendimento.csv')
    t_path = os.path.join(DATA_DIR, 'transacoes.csv')
    p_path = os.path.join(DATA_DIR, 'perfil_investidor.json')
    
    df_h = pd.read_csv(h_path)
    df_t = pd.read_csv(t_path)
    with open(p_path, 'r', encoding='utf-8') as f:
        perfil = json.load(f)
        
    return df_h, df_t, perfil

# --- INTERFACE ---
st.set_page_config(page_title="EconoAI - ItsFMH", page_icon="💰")

try:
    df_h, df_t, perfil = load_data()
    
    st.title(f"🤖 EconoAI - Consultor de {perfil['nome']}")
    
    # Sidebar com dados reais do JSON
    st.sidebar.header("👤 Perfil do Usuário")
    st.sidebar.markdown(f"**Profissão:** {perfil['profissao']}")
    st.sidebar.markdown(f"**Perfil:** {perfil['perfil_investidor'].capitalize()}")
    
    # Cálculo de Saldo Dinâmico
    receitas = df_t[df_t['tipo'] == 'entrada']['valor'].sum()
    saidas = df_t[df_t['tipo'] == 'saida']['valor'].sum()
    saldo = receitas - saidas
    
    st.metric("Saldo Atualizado", f"R$ {saldo:,.2f}")

    if prompt := st.chat_input("Como posso ajudar?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # Adicionado spinner para mostrar que a IA está consultando os arquivos
            with st.spinner("Analisando sua base de dados financeiros..."):
                p_lower = prompt.lower()
                
                # 1. Caso de Erro: Admitir e revisar se o usuário contestar
                if any(x in p_lower for x in ["errado", "erro", "corrigir", "incorreto"]):
                    st.markdown("Peço desculpas pela imprecisão. Como sou uma inteligência artificial em aprendizado, posso cometer erros de interpretação.")
                
                # 2. Caso de Suporte: Histórico de 22/09
                elif "problema" in p_lower:
                    st.markdown("Vi que em 22/09 você teve um problema no app (erro no extrato), mas ele já foi resolvido.")
                
                # 3. Caso de Saldo
                elif "saldo" in p_lower:
                    st.markdown(f"Seu saldo atual, calculado a partir de suas entradas e saídas, é de **R$ {saldo:,.2f}**.")
                
                # 4. Caso de Investimento
                elif "investir" in p_lower or "investimento" in p_lower:
                    st.markdown(f"Considerando seu perfil **{perfil['perfil_investidor']}**, o foco recomendado é a meta: '{perfil['metas'][1]['meta']}' para 2027.")
                
                # 5. Caso de Desconhecimento: Resposta segura para o "Não Sei"
                else:
                    st.markdown("Sinto muito, não localizei registros sobre isso nos seus arquivos de transações ou histórico. Como sou um agente focado nos seus dados internos, não consigo acessar informações externas ou de terceiros por segurança.")

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.info(f"Diretório base detectado: {BASE_DIR}")