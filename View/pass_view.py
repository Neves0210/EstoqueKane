import streamlit as st

class UserView:
    def display_login(self):
        with st.form("login_form"):
            st.subheader("Login")
            username = st.text_input("Nome de Usuário", key="login_username")
            password = st.text_input("Senha", type='password', key="login_password")
            login_button = st.form_submit_button("Logar")
            if login_button:
                return username, password
        return None, None

    def display_registration(self):
        with st.form("registration_form"):
            st.subheader("Registrar Novo Usuário")
            username = st.text_input("Nome de Usuário", key="register_username")
            password = st.text_input("Senha", type='password', key="register_password")
            confirm_password = st.text_input("Confirme a Senha", type='password', key="register_confirm_password")
            register_button = st.form_submit_button("Registrar")
            if register_button:
                return username, password, confirm_password
        return None, None, None

    def display_error(self, message):
        st.error(message)

    def display_success(self, message):
        st.success(message)

    def display_pending_users_with_type(self, pending_users):
        st.subheader("Aprovar Usuários Pendentes")
        user_to_approve = None
        selected_type = None

        for username in pending_users:
            st.write(f"Usuário: {username}")
            selected_type = st.selectbox(
                f"Selecione o tipo de usuário para {username}",
                options=["user", "admin"],
                key=f"type_select_{username}"
            )
            if st.button(f"Aprovar {username}"):
                user_to_approve = username
                break
        
        return user_to_approve, selected_type

