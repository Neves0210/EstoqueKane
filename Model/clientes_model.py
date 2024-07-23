import pandas as pd

class ClientesModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv(f"Data/{self.file_path}")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{self.file_path}' não encontrado no diretório 'Data'.")

    def filter_data(self, selected_cols, search_values):
        filtered_data = self.data
        
        for col in selected_cols:
            if col in search_values and search_values[col]:
                value = search_values[col]
                if col in ['CPF/CNPJ', 'Cep', 'Telefone']:
                    # Filtrar por valores numéricos
                    filtered_data = filtered_data[filtered_data[col].astype(str).str.contains(value, na=False)]
                elif col == 'Data de Nascimento':
                    # Filtrar por data
                    filtered_data = filtered_data[filtered_data[col] == value]
                else:
                    # Filtrar por texto
                    filtered_data = filtered_data[filtered_data[col].str.contains(value, case=False, na=False)]
        
        return filtered_data
