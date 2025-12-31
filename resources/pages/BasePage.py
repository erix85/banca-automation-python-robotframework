from robot.libraries.BuiltIn import BuiltIn

class BasePage:
    """Clase base para todos los Page Objects. Maneja la instancia de Selenium."""

    def __init__(self):
        # Inicializa la librería de Selenium una sola vez para todas las páginas
        self.sel_lib = BuiltIn().get_library_instance('SeleniumLibrary')