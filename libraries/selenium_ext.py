from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException
)
import time

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
        try:
            element = self.sel_lib.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except StaleElementReferenceException:
            # Reintenta encontrar el elemento si se vuelve stale
            time.sleep(0.5)
            element = self.sel_lib.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    @keyword("Wait And Click")
    def wait_and_click(self, locator, timeout=15):
        """
        Combina la espera explícita y el click en un solo paso robusto.
        Reintenta la búsqueda del elemento si se produce una StaleElementReferenceException.
        """
        self.sel_lib.wait_until_element_is_visible(locator, timeout)
        end_time = time.time() + timeout
        while True:
            try:
                element = self.sel_lib.find_element(locator)
                element.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException) as e:
                if time.time() > end_time:
                    raise e
                time.sleep(0.5)

    @keyword("Wait And Input Text")
    def wait_and_input_text(self, locator, text, timeout=15):
        """
        Combina la espera explícita y la escritura de texto, con reintentos para elementos stale.
        """
        self.sel_lib.wait_until_element_is_visible(locator, timeout)
        end_time = time.time() + timeout
        while True:
            try:
                element = self.sel_lib.find_element(locator)
                element.clear()
                element.send_keys(text)
                return
            except (StaleElementReferenceException, ElementNotInteractableException) as e:
                if time.time() > end_time:
                    raise e
                time.sleep(0.5)

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

    @keyword("Is Element Visible")
    def is_element_visible(self, locator):
        """
        Verifica si un elemento es visible en la página.
        Devuelve True si el elemento es visible, False en caso contrario.
        """
        try:
            return self.sel_lib.element_should_be_visible(locator)
        except Exception:
            return False

# Alias para cumplir con el requerimiento de importación de Robot Framework sin renombrar la clase
selenium_ext = SeleniumExt