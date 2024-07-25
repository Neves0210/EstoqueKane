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
            st.session_state['user_type'] = None

        if not st.session_state['logged_in']:
            with st.container():
                action = st.radio("Você já tem uma conta?", ("Login", "Registrar"))

                if action == "Registrar":
                    username, password, confirm_password = self.view.display_registration()
                    if username and password and confirm_password:
                        if password != confirm_password:
                            self.view.display_error("As senhas não correspondem.")
                        elif self.model.user_exists(username):
                            self.view.display_error("Nome de usuário já existe.")
                        else:
                            self.model.register_user(username, password)
                            send_admin_email(username)
                            self.view.display_success("Registro feito com sucesso! Aguardando aprovação do administrador.")
                    return False
                
                elif action == "Login":
                    username, password = self.view.display_login()
                    if username and password:
                        authenticated, user_type = self.model.authenticate_user(username, password)
                        if authenticated:
                            st.session_state['logged_in'] = True
                            st.session_state['user_type'] = user_type
                            self.view.display_success(f"Bem-vindo, {username}!")
                            return True
                        else:
                            self.view.display_error("Nome de usuário ou senha incorretos, ou conta não aprovada.")
                    return False
        
        return True

    def admin_approve_users(self):
        pending_users = self.model.get_pending_users()
        user_to_approve, selected_type = self.view.display_pending_users_with_type(pending_users)
        if user_to_approve and selected_type:
            self.model.approve_user(user_to_approve, selected_type)
            self.view.display_success(f"Usuário {user_to_approve} aprovado como {selected_type}.")
