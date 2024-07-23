from Model.estoque_model import EstoqueModel
from View.estoque_view import EstoqueView

class EstoqueController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.display_title()

        try:
            # Carregar dados
            data = self.model.data

            # Mostrar nomes das colunas
            column_names = data.columns.tolist()
            self.view.display_column_names(column_names)

            # Seleção de colunas para pesquisa
            selected_cols = self.view.get_selected_columns(column_names)

            # Pesquisa por valor nas colunas selecionadas
            search_value = self.view.get_search_value()

            # Nomes das colunas que devem sempre permanecer visíveis
            always_visible_cols = ['Preço de Custo', 'Preço de Tabela']

            if search_value:
                # Filtrar dados com base na pesquisa
                filtered_data = self.model.filter_data(selected_cols, search_value, always_visible_cols)
                self.view.display_filtered_data(filtered_data, search_value)
            else:
                # Mostrar tabela completa quando não há valor de pesquisa
                self.view.display_full_data(data)

        except FileNotFoundError as e:
            self.view.display_error(str(e))
