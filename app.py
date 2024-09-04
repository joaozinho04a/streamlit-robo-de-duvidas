Gere uma tela streamlit em python com as seguintes características:

Uma paleta de cores com laranja, cinza, azul e preto. Seguindo a identifidade visual do banco brasileiro Itau
Um sidebar contendo input para os seguintes campos:
RACF do usuário (palavra de 8 caracteres que é chave única na empresa que trabalho)
CNPJ - Código Nacional de pessoa jurídica, indicando qual o CNPJ o usuário deseja pesquisar
Referência de uso - Data no formato YYYYMM que indica a data que deseja informações daquele CNPJ. Seu valão padrão será o yyyymm da data atual.
Um botão de busca, que iniciará a pesquisa
No centro, criei as seguintes tabs Variaveis, Historico, Override, Socio, Grupo, Default, Atrasos, Endividamento, Arvores


import streamlit as st
from datetime import datetime

# Definir a paleta de cores
st.markdown("""
    <style>
    .main {
        background-color: #F5F5F5;
    }
    .sidebar .sidebar-content {
        background-color: #FF6F00;
    }
    .stButton>button {
        background-color: #FF6F00;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# Barra lateral
st.sidebar.header("Parâmetros de Pesquisa")
racf = st.sidebar.text_input("RACF do usuário", max_chars=8)
cnpj = st.sidebar.text_input("CNPJ")
referencia_uso = st.sidebar.text_input("Referência de uso (YYYYMM)", value=datetime.now().strftime("%Y%m"))
buscar = st.sidebar.button("Buscar")

# Tabs no centro da tela
tabs = ["Variáveis", "Histórico", "Override", "Sócio", "Grupo", "Default", "Atrasos", "Endividamento", "Árvores"]
tab = st.tabs(tabs)

# Conteúdo das abas
with tab[0]:
    st.header("Variáveis")
    st.write("Conteúdo da aba Variáveis")

with tab[1]:
    st.header("Histórico")
    st.write("Conteúdo da aba Histórico")

with tab[2]:
    st.header("Override")
    st.write("Conteúdo da aba Override")

with tab[3]:
    st.header("Sócio")
    st.write("Conteúdo da aba Sócio")

with tab[4]:
    st.header("Grupo")
    st.write("Conteúdo da aba Grupo")

with tab[5]:
    st.header("Default")
    st.write("Conteúdo da aba Default")

with tab[6]:
    st.header("Atrasos")
    st.write("Conteúdo da aba Atrasos")

with tab[7]:
    st.header("Endividamento")
    st.write("Conteúdo da aba Endividamento")

with tab[8]:
    st.header("Árvores")
    st.write("Conteúdo da aba Árvores")
