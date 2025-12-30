import yaml
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

class DataLoader:
    
    @keyword("Load Test Data")
    def load_test_data(self, file_path):
        """Lee un archivo YAML y lo carga en una variable global de la suite."""
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        BuiltIn().set_suite_variable('${GLOBAL_DATA}', data)
