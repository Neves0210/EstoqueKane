import streamlit as st

class ClientesView:
    def display_title(self):
        st.title("Pesquisa de Clientes")

    def display_column_names(self, column_names):
        allowed_columns = ['Nome', 'Sobrenome', 'CPF/CNPJ', 'Sexo', 'Cep', 'Telefone', 'E-mail']
        filtered_columns = [col for col in column_names if col in allowed_columns]
        st.write("### Nomes das Colunas Disponíveis")
        st.write(filtered_columns)

    def get_selected_columns(self, column_names):
        allowed_columns = ['Nome', 'Sobrenome', 'CPF/CNPJ', 'Sexo', 'Cep', 'Telefone', 'E-mail']
        filtered_columns = [col for col in column_names if col in allowed_columns]
        return st.multiselect(
            "Escolha as colunas para pesquisa",
            options=filtered_columns,
        )

    def get_search_value(self, column_name):
        if column_name in ['Nome', 'Sobrenome', 'Sexo', 'E-mail']:
            return st.text_input(f"Digite o valor para {column_name}")
        elif column_name in ['CPF/CNPJ', 'Cep', 'Telefone']:
            return st.text_input(f"Digite o valor para {column_name}", placeholder="Apenas números")
        elif column_name == 'Data de Nascimento':
            return st.date_input(f"Digite a data de nascimento")
        else:
            return st.text_input(f"Digite o valor para {column_name}")

    def display_filtered_data(self, filtered_data, search_value):
        if not filtered_data.empty:
            st.write(f"### Resultados da Pesquisa Contendo '{search_value}'")
            filtered_data = self.remove_hidden_columns(filtered_data)
            selected_client_id = st.selectbox("Escolha um cliente para detalhes", filtered_data.index)
            
            if selected_client_id:
                self.display_client_details(filtered_data.loc[selected_client_id])
            st.dataframe(filtered_data, height=800, width=1000)
        else:
            st.warning("Nenhuma coluna selecionada para pesquisa ou nenhum resultado encontrado.")

    def display_full_data(self, data):
        st.write("### Tabela Completa")
        data = self.remove_hidden_columns(data)
        st.dataframe(data, height=800, width=1000)

    def display_client_details(self, client_data):
        st.write("### Detalhes do Cliente")
        st.write(client_data)

    def display_error(self, message):
        st.error(message)

    def remove_hidden_columns(self, df):
        columns_to_remove = ['URL', 'URL DO CLIENTE']
        return df[[col for col in df.columns if col not in columns_to_remove]]

    def clear_search(self):
        st.empty()  # Limpa todos os elementos exibidos na tela
