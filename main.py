import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Pesquisa de Estoque")

    # Carregar arquivo CSV diretamente
    try:
        data = pd.read_csv('estoque_kanemoto.csv')
    except FileNotFoundError:
        st.error("Arquivo 'estoque_kanemoto.csv' não encontrado no diretório atual.")
        return

    # Mostrar nomes das colunas
    column_names = data.columns.tolist()
    st.write("### Nomes das Colunas Disponíveis")
    st.write(column_names)

    # Seleção de colunas para pesquisa
    selected_cols = st.multiselect(
        "Escolha as colunas para pesquisa",
        options=column_names,
    )

    # Pesquisa por valor nas colunas selecionadas
    st.write("### Pesquisa por Valor")
    search_value = st.text_input("Digite o valor a ser pesquisado")

    # Nomes das colunas que devem sempre permanecer visíveis
    always_visible_cols = ['Preço de Custo', 'Preço de Tabela']  # Ajuste os nomes conforme necessário

    # Filtrar dados com base na pesquisa
    if search_value:
        # Verificar se as colunas selecionadas existem nos dados
        selected_cols = [col for col in selected_cols if col in data.columns]
        
        if selected_cols:
            # Criar filtro para múltiplas colunas
            mask = data[selected_cols].astype(str).apply(lambda row: row.str.contains(search_value, case=False).any(), axis=1)
            filtered_data = data[mask]

            # Filtrar colunas vazias ou com apenas zeros, mantendo as colunas sempre visíveis
            non_empty_cols = [col for col in selected_cols if not filtered_data[col].isna().all() and not (filtered_data[col] == 0).all()]

            # Garantir que as colunas sempre visíveis sejam sempre incluídas nos resultados
            for col in always_visible_cols:
                if col in data.columns:
                    non_empty_cols = list(set(non_empty_cols) | {col})

            filtered_data = filtered_data[non_empty_cols]

            # Exibir resultados
            st.write(f"### Resultados da Pesquisa Contendo '{search_value}'")
            st.dataframe(filtered_data, height=800, width=1000)  # Ajustar altura e largura da tabela

        else:
            st.warning("Nenhuma coluna selecionada para pesquisa.")

    else:
        # Mostrar tabela completa quando não há valor de pesquisa
        st.write("### Tabela Completa")
        st.dataframe(data, height=800, width=1000)

    # Se necessário, você pode reativar a visualização gráfica com o código abaixo
    # # Selecionar colunas para visualização
    # x_col = st.selectbox("Escolha a coluna para o eixo X", column_names)
    # y_col = st.selectbox("Escolha a coluna para o eixo Y", column_names)

    # # Atualizar visualização para dados filtrados
    # if search_value and not filtered_data.empty and x_col in filtered_data.columns and y_col in filtered_data.columns:
    #     fig = px.line(filtered_data, x=x_col, y=y_col, title=f'Visualização de {y_col} por {x_col} (Filtrado)')
    #     fig.update_xaxes(tickangle=45)
    #     st.plotly_chart(fig)
    # elif not search_value:
    #     # Criar gráfico com Plotly para dados não filtrados
    #     fig = px.line(data, x=x_col, y=y_col, title=f'Visualização de {y_col} por {x_col}')
    #     fig.update_xaxes(tickangle=45)
    #     st.plotly_chart(fig)
    # else:
    #     st.warning("Nenhum dado corresponde ao filtro aplicado ou colunas de visualização inválidas.")

if __name__ == "__main__":
    main()
