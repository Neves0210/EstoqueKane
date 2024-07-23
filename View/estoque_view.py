import streamlit as st

class EstoqueView:
    def display_title(self):
        st.title("Pesquisa de Estoque")

    def display_column_names(self, column_names):
        st.write("### Nomes das Colunas Disponíveis")
        st.write(column_names)

    def get_selected_columns(self, column_names):
        return st.multiselect(
            "Escolha as colunas para pesquisa",
            options=column_names,
        )

    def get_search_value(self):
        return st.text_input("Digite o valor a ser pesquisado")

    def display_filtered_data(self, filtered_data, search_value):
        if not filtered_data.empty:
            st.write(f"### Resultados da Pesquisa Contendo '{search_value}'")
            st.dataframe(filtered_data, height=800, width=1000)
        else:
            st.warning("Nenhuma coluna selecionada para pesquisa ou nenhum resultado encontrado.")

    def display_full_data(self, data):
        st.write("### Tabela Completa")
        st.dataframe(data, height=800, width=1000)

    def display_error(self, message):
        st.error(message)
