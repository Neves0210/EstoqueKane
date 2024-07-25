import streamlit as st
from Model.estoque_model import EstoqueModel
from View.estoque_view import EstoqueView
from Controller.estoque_controller import EstoqueController
from Model.clientes_model import ClientesModel
from View.clientes_view import ClientesView
from Controller.clientes_controller import ClientesController
from Controller.pass_controller import UserController

def admin_interface():
    st.title("Painel do Administrador")
    user_controller = UserController()
    user_controller.admin_approve_users()

def main():
    st.title("Aplicação de Pesquisa")

    # Inicializar o controlador de usuário
    user_controller = UserController()

    # Verificar login antes de continuar
    if user_controller.run():
        # Verifica se o modo administrador foi selecionado
        if st.sidebar.checkbox("Modo Administrador"):
            admin_interface()
        else:
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
    else:
        st.error("Por favor, faça login para continuar.")

if __name__ == "__main__":
    main()
