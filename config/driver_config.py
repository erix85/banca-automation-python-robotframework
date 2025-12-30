import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager

class DriverConfig:
    def __init__(self, env_name="local"):
        with open('config/settings.yaml', 'r') as f:
            full_config = yaml.safe_load(f)
        self.config = full_config['environments'][env_name]
        self.defaults = full_config['default']

    def get_driver_instance(self):
        exec_type = self.config.get('execution_type', 'local').lower()
        browser = self.config.get('browser', 'chrome').lower()
        
        options = self._get_options(browser)

        if exec_type == "grid":
            return webdriver.Remote(
                command_executor=self.config['grid_url'],
                options=options
            )
        
        if exec_type == "manual":
            service = ChromeService(executable_path=self.config['driver_path'])
            return webdriver.Chrome(service=service, options=options)

        # Por defecto: Local Automático con WebDriver Manager
        if browser in ["chrome", "brave", "opera"]:
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif browser == "ie":
            return webdriver.Ie(service=IEService(IEDriverManager().install()), options=options)
        elif browser == "safari":
            return webdriver.Safari(options=options)

    def _get_options(self, browser):
        if browser in ["chrome", "brave", "opera"]:
            opt = webdriver.ChromeOptions()
            # Para Brave y Opera es obligatorio indicar la ruta del ejecutable
            if browser in ["brave", "opera"]:
                binary_path = self.config.get('binary_path')
                if binary_path:
                    opt.binary_location = binary_path
            if self.config.get('headless'):
                opt.add_argument("--headless=new")
            opt.add_argument("--start-maximized")
            opt.add_argument("--ignore-certificate-errors")
            return opt
        elif browser == "firefox":
            opt = webdriver.FirefoxOptions()
            if self.config.get('headless'):
                opt.add_argument("-headless")
            return opt
        elif browser == "edge":
            opt = webdriver.EdgeOptions()
            if self.config.get('headless'):
                opt.add_argument("--headless=new")
            return opt
        elif browser == "ie":
            opt = webdriver.IeOptions()
            # IE requiere configuraciones de zona de seguridad y zoom al 100%
            opt.ignore_zoom_level = True
            return opt
        elif browser == "safari":
            opt = webdriver.SafariOptions()
            return opt
        else:
            # Retorno seguro para navegadores no listados (ej. Opera)
            return None