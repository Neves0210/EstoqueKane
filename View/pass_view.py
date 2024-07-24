import streamlit as st

class UserView:
    def display_login(self):
        st.subheader("Login")
        username = st.text_input("Nome de Usuário")
        password = st.text_input("Senha", type='password')
        if st.button("Logar"):
            return username, password
        return None, None

    def display_registration(self):
        st.subheader("Registrar Novo Usuário")
        username = st.text_input("Nome de Usuário")
        password = st.text_input("Senha", type='password')
        confirm_password = st.text_input("Confirme a Senha", type='password')
        if st.button("Registrar"):
            return username, password, confirm_password
        return None, None, None

    def display_error(self, message):
        st.error(message)

    def display_success(self, message):
        st.success(message)
    