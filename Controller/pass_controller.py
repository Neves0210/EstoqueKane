from Model.pass_model import UserModel
from View.pass_view import UserView
import streamlit as st

class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    def run(self):
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False

        if not st.session_state['logged_in']:
            action = st.radio("Você já tem uma conta?", ("Login", "Registrar"))

            if action == "Registrar":
                username, password, confirm_password = self.view.display_registration()
                if username and password and confirm_password:
                    if password != confirm_password:
                        self.view.display_error("As senhas não correspondem.")
                    elif self.model.authenticate_user(username, password):
                        self.view.display_error("Nome de usuário já existe.")
                    else:
                        self.model.register_user(username, password)
                        self.view.display_success("Registro bem-sucedido! Você pode fazer login agora.")
                return False
                
            elif action == "Login":
                username, password = self.view.display_login()
                if username and password:
                    if self.model.authenticate_user(username, password):
                        st.session_state['logged_in'] = True
                        self.view.display_success(f"Bem-vindo, {username}!")
                    else:
                        self.view.display_error("Nome de usuário ou senha incorretos.")
                return st.session_state['logged_in']
        
        return True
