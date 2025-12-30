from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.chrome.options import Options as ChromeOptions

class BrowserSetup:
    """
    Configuración robusta del navegador sin dependencias externas complejas.
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    @keyword("Open Configured Browser")
    def open_configured_browser(self, url_or_env="local", browser="chrome", headless=False):
        """
        Abre el navegador configurado.
        Acepta una URL directa o un nombre de entorno ('local', 'qa').
        """
        # Mapeo simple de entornos a URLs para evitar KeyError
        urls = {
            "local": "https://opensource-demo.orangehrmlive.com/",
            "qa": "https://opensource-demo.orangehrmlive.com/",
            "dev": "https://opensource-demo.orangehrmlive.com/"
        }
        
        # Determinar la URL: si es una clave conocida usa el mapa, si no, usa el valor como URL
        target_url = urls.get(url_or_env, url_or_env)

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