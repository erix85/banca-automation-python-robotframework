import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.chrome.options import Options as ChromeOptions
from libraries.reader_utils import ReaderUtils

class BrowserSetup:
    """
    Configuración robusta del navegador sin dependencias externas complejas.
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self):
        """Carga la configuración al inicializar la librería."""
        self.config = ReaderUtils().read_yaml_data("config/settings.yaml")
        self.default_url = self.config.get("default", {}).get("base_url", "about:blank")
        self.environments = self.config.get("environments", {})

    @keyword("Open Configured Browser")
    def open_configured_browser(self, url_or_env="local", browser="chrome", headless=False):
        """
        Abre el navegador configurado.
        Acepta una URL directa o un nombre de entorno (ej: 'local', 'qa_grid').
        """
        env_settings = self.environments.get(url_or_env)
        
        if env_settings:
            # Si es un entorno conocido, usa su base_url o el por defecto.
            target_url = env_settings.get("base_url", self.default_url)
        else:
            # Si no, se asume que es una URL directa.
            target_url = url_or_env

        # Obtener instancia de SeleniumLibrary
        sel_lib = BuiltIn().get_library_instance('SeleniumLibrary')
        
        # Configuración de opciones para Chrome
        if browser.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-notifications')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            if str(headless).lower() == 'true':
                options.add_argument('--headless')
            
            sel_lib.open_browser(target_url, browser, options=options)
        else:
            sel_lib.open_browser(target_url, browser)
            sel_lib.maximize_browser_window()