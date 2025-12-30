from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class SeleniumExt:
    """
    Extensión de Selenium para flujos complejos.
    """

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        # Accedemos a la instancia activa de SeleniumLibrary en Robot
        self.sel_lib = BuiltIn().get_library_instance('SeleniumLibrary')

    @property
    def driver(self):
        return self.sel_lib.driver

    @keyword("Safe JS Click")
    def safe_js_click(self, locator):
        """
        Hace un click vía JavaScript si el click normal de Selenium falla
        por estar cubierto por otro elemento (como un loading spinner).
        """
        element = self.sel_lib.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @keyword("Wait And Click")
    def wait_and_click(self, locator, timeout=15):
        """
        Combina la espera explícita y el click en un solo paso robusto.
        """
        # Primero aseguramos que el elemento sea visible usando el manejo de locators de Robot
        self.sel_lib.wait_until_element_is_visible(locator, timeout)
        
        # Luego obtenemos el elemento y esperamos a que sea "clickeable" (no oscurecido)
        element = self.sel_lib.find_element(locator)
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(element)
        )
        element.click()

    @keyword("Scroll To Element")
    def scroll_to_element(self, locator):
        """Mueve la pantalla hasta que el elemento sea visible."""
        element = self.sel_lib.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @keyword("Get Element Value Via JS")
    def get_value_js(self, locator):
        """Útil para campos de texto protegidos o con formatos especiales."""
        element = self.sel_lib.find_element(locator)
        return self.driver.execute_script("return arguments[0].value;", element)

# Alias para cumplir con el requerimiento de importación de Robot Framework sin renombrar la clase
selenium_ext = SeleniumExt