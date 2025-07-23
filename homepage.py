import streamlit as st

coluna_esquerda, coluna_direita = st.columns([1, 1])



coluna_esquerda.title("Hash&Co")
coluna_esquerda.write("#### Bem vindo")

botao_dashboards = st.button("Dashboards Projetos")
botao_indicadores = st.button("Principais Indicadores")

if botao_dashboards:
    st.switch_page("dashboard.py")
if botao_indicadores:
    st.switch_page("indicadores.py")


container = coluna_direita.container(border=True)
container.image("imagens/time-comunidade.webp")