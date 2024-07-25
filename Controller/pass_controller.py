from Model.pass_model import UserModel
from View.pass_view import UserView
import streamlit as st
from Utils.email_utils import send_admin_email  # Assumindo que está no mesmo diretório

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
                        send_admin_email(username)
                        self.view.display_success("Registro feito com sucesso! Aguardando aprovação do administrador.")
                return False
                
            elif action == "Login":
                username, password = self.view.display_login()
                if username and password:
                    if self.model.authenticate_user(username, password):
                        st.session_state['logged_in'] = True
                        self.view.display_success(f"Bem-vindo, {username}!")
                    else:
                        self.view.display_error("Nome de usuário ou senha incorretos, ou conta não aprovada.")
                return st.session_state['logged_in']
        
        return True

    def admin_approve_users(self):
        pending_users = self.model.get_pending_users()
        username_to_approve = self.view.display_pending_users(pending_users)
        if username_to_approve:
            self.model.approve_user(username_to_approve)
            self.view.display_success(f"Usuário {username_to_approve} aprovado.")
