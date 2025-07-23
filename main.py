import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario

lista_usuarios = session.query(Usuario).all()

# Definir credenciais com os hashes
credenciais = {"usernames":
                 {
                    usuario.email: {"name": usuario.nome, "password": usuario.senha} for usuario in lista_usuarios
       
                        }
                }

authenticator = stauth.Authenticate(credenciais, "credenciais_hash_co", "f81rjwnsdskeijs", cookie_expiry_days=30)

def autenticar_usuario(authenticator):
    nome, authentication_status, username = authenticator.login()

    if authentication_status:
        return {"nome": nome, "username": username}
    elif authentication_status == False:
        st.error("Combinação de usuário e senha inválidas")
    else:
        st.error("Preencha o formulário para fazer login")

def logout():
    authenticator.logout()


# autenticar usuário
dados_usuario = autenticar_usuario(authenticator)

if dados_usuario:

    email_usuario = dados_usuario["username"] 
    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario.admin:
        pg = st.navigation(
            {
                "Home": [st.Page("homepage.py", title="Hash&Co")],
                "Dashboards": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicadores.py", title="Indicadores")],
                "Conta": [st.Page(logout, title="Sair"), st.Page("criar_conta.py", title="Criar Conta")]
             }
        )
    else:
         pg = st.navigation(
            {
                "Home": [st.Page("homepage.py", title="Hash&Co")],
                "Dashboards": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicadores.py", title="Indicadores")],
                "Conta": [st.Page(logout, title="Sair")]
             }
        )


    pg.run()
