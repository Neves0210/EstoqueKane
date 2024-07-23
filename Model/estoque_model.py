import pandas as pd
import os

class EstoqueModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo 'estoque_kanemoto.csv' não encontrado no diretório atual.")

    def filter_data(self, selected_cols, search_value, always_visible_cols):
        # Filtrar os dados com base na pesquisa
        selected_cols = [col for col in selected_cols if col in self.data.columns]
        if selected_cols:
            mask = self.data[selected_cols].astype(str).apply(lambda row: row.str.contains(search_value, case=False).any(), axis=1)
            filtered_data = self.data[mask]

            non_empty_cols = [col for col in selected_cols if not filtered_data[col].isna().all() and not (filtered_data[col] == 0).all()]
            for col in always_visible_cols:
                if col in self.data.columns:
                    non_empty_cols = list(set(non_empty_cols) | {col})

            return filtered_data[non_empty_cols]
        return pd.DataFrame()
