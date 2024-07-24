import streamlit as st
from Model.estoque_model import EstoqueModel
from View.estoque_view import EstoqueView
from Controller.estoque_controller import EstoqueController
from Model.clientes_model import ClientesModel
from View.clientes_view import ClientesView
from Controller.clientes_controller import ClientesController
from Controller.pass_controller import UserController

def main():
    st.title("Aplicação de Pesquisa")

    # Inicializar o controlador de usuário
    user_controller = UserController()
    
    # Verificar login antes de continuar
    if user_controller.run():
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

if __name__ == "__main__":
    main()
