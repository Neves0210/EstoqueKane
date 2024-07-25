import streamlit as st
from Model.estoque_model import EstoqueModel
from View.estoque_view import EstoqueView
from Controller.estoque_controller import EstoqueController
from Model.clientes_model import ClientesModel
from View.clientes_view import ClientesView
from Controller.clientes_controller import ClientesController
from Controller.pass_controller import UserController  # Atualize o caminho do import, se necessário

def admin_interface(user_controller):
    st.title("Painel do Administrador")
    user_controller.admin_approve_users()

def pesquisa_interface():
    st.title("Área de Pesquisa")
    # Escolher entre Estoque e Clientes
    option = st.selectbox(
        "Escolha a área para pesquisa",
        ["Estoque", "Clientes"]
    )

    if option == "Estoque":
        # Configurar e rodar a pesquisa de estoque
        model = EstoqueModel('estoque_kanemoto.csv')
        view = EstoqueView()
        controller = EstoqueController(model, view)
        controller.run()
    
    elif option == "Clientes":
        # Configurar e rodar a pesquisa de clientes
        model = ClientesModel('clientes_kanemoto.csv')
        view = ClientesView()
        controller = ClientesController(model, view)
        controller.run()

def main():
    # Configura a página para layout centralizado padrão
    st.set_page_config(page_title="Aplicação de Pesquisa", layout="centered")
    
    # Inicializar o controlador de usuário
    user_controller = UserController()

    # Verificar login antes de continuar
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['user_type'] = None

    if st.session_state['logged_in']:
        # Criar um cabeçalho com título e botão de logout no topo
        st.container()  # Usar container para manter layout centralizado
        with st.container():
            col1, col2 = st.columns([9, 1])
            with col1:
                st.title("Aplicação de Pesquisa")
            with col2:
                if st.button("Exit"):
                    st.session_state['logged_in'] = False
                    st.session_state['user_type'] = None
                    st.rerun()

        # Verifica se o usuário é admin antes de mostrar o modo administrador
        if st.session_state['user_type'] == 'admin':
            if st.sidebar.checkbox("Modo Administrador"):
                admin_interface(user_controller)
            else:
                pesquisa_interface()
        else:
            pesquisa_interface()
    else:
        if user_controller.run():
            st.rerun()  # Rerun the app to update state

if __name__ == "__main__":
    main()
