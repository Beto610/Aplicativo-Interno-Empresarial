from models import session, Usuario
import streamlit_authenticator as stauth


senha_criptografada = stauth.Hasher(["123123"]).generate()[0]
usuario = Usuario(nome="Ozzy", senha=senha_criptografada, email="ozzy@gmail.com", admin=False)
session.add(usuario)
session.commit()