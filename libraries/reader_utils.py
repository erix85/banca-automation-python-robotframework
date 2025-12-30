import json
import os
import yaml
from robot.api.deco import keyword

class ReaderUtils:
    """Librería para gestión de datos de prueba y configuraciones."""

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @keyword("Read JSON Data")
    def read_json_data(self, file_path: str) -> dict:
        """Lee un archivo JSON y lo retorna como un diccionario de Python."""
        file_path = self._resolve_path(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @keyword("Read YAML Data")
    def read_yaml_data(self, file_path: str) -> dict:
        """Lee un archivo YAML y lo retorna como un diccionario de Python."""
        file_path = self._resolve_path(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _resolve_path(self, path: str) -> str:
        """
        Resuelve rutas de archivos de forma robusta.
        Si la ruta directa falla, intenta resolverla relativa a la raíz del proyecto.
        """
        if os.path.exists(path):
            return path
            
        # Obtener la raíz del proyecto
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Estrategia de recuperación: Buscar el archivo en ubicaciones comunes
        filename = os.path.basename(path)
        candidates = [
            # 1. Intentar limpiar la ruta de '..' y buscar desde root
            os.path.join(root_dir, path.replace('../', '').replace('..\\', '').lstrip('\\').lstrip('/')),
            # 2. Buscar en resources/variables
            os.path.join(root_dir, 'resources', 'variables', filename),
            # 3. Buscar en resources/data
            os.path.join(root_dir, 'resources', 'data', filename),
            # 4. Buscar en la raíz
            os.path.join(root_dir, filename)
        ]
        
        for candidate in candidates:
            if os.path.exists(candidate):
                return candidate
                
        return path

    @keyword("Read Excel Row")
    def read_excel_row(self, file_path: str, sheet_name: str, row_index: int) -> dict:
        """Lee una fila específica de un Excel. Ideal para transferencias masivas."""
        import pandas as pd
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Retorna la fila como un diccionario
        return df.iloc[row_index].to_dict()

    @keyword("Get Environment Secret")
    def get_env_secret(self, key: str) -> str:
        """Obtiene variables de entorno, útil para contraseñas en CI/CD."""
        return os.getenv(key, "Secret_Not_Found")

# Alias para permitir la importación de Robot Framework (nombre de archivo = nombre de clase/variable)
reader_utils = ReaderUtils