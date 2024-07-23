from Model.clientes_model import ClientesModel
from View.clientes_view import ClientesView

class ClientesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.display_title()
        self.view.clear_search()  # Limpa a área de pesquisa

        try:
            data = self.model.data
            column_names = data.columns.tolist()
            self.view.display_column_names(column_names)

            selected_cols = self.view.get_selected_columns(column_names)
            search_values = {}

            for col in selected_cols:
                search_values[col] = self.view.get_search_value(col)

            filtered_data = self.model.filter_data(selected_cols, search_values)
            
            if search_values:
                self.view.display_filtered_data(filtered_data, search_values)
            else:
                self.view.display_full_data(data)

        except FileNotFoundError as e:
            self.view.display_error(str(e))
        except ValueError as e:
            self.view.display_error(str(e))
