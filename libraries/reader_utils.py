import json
import yaml
import pandas as pd
from robot.api.deco import keyword

class reader_utils:
    """Librería para gestión de datos de prueba y configuraciones."""

    @keyword("Read JSON Data")
    def read_json_data(self, file_path):
        """Lee un archivo JSON y lo retorna como un diccionario de Python."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @keyword("Read Excel Row")
    def read_excel_row(self, file_path, sheet_name, row_index):
        """Lee una fila específica de un Excel. Ideal para transferencias masivas."""
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Retorna la fila como un diccionario
        return df.iloc[int(row_index)].to_dict()

    @keyword("Get Environment Secret")
    def get_env_secret(self, key):
        """Obtiene variables de entorno, útil para contraseñas en CI/CD."""
        import os
        return os.getenv(key, "Secret_Not_Found")