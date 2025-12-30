import allure
from allure_commons.types import AttachmentType
from robot.libraries.BuiltIn import BuiltIn

class AllureManager:
    """Gestiona adjuntos avanzados para Allure Report."""

    def attach_screenshot_on_failure(self):
        """Adjunta captura de pantalla al reporte de Allure si el test falla."""
        sel_lib = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = sel_lib.driver
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot_Error",
            attachment_type=AttachmentType.PNG
        )

    def log_test_metadata(self, env, browser):
        """Añade información del entorno al reporte."""
        allure.dynamic.parameter("Environment", env)
        allure.dynamic.parameter("Browser", browser)