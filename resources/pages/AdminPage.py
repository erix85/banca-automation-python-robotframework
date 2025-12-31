from robot.api.deco import keyword
from BasePage import BasePage

class AdminPage(BasePage):
    """Page Object para funciones administrativas."""

    # Localizadores
    MENU_EMPLOYEES = "id=menu_employees"
    BTN_ADD_NEW_EMPLOYEE = "id=btn_add_new_employee"
    EMP_NAME = "id=emp_name"
    EMP_EMAIL = "id=emp_email"
    EMP_ROLE = "id=emp_role"
    EMP_PASSWORD = "id=emp_password"
    BTN_SAVE_EMPLOYEE = "id=btn_save_employee"

    @keyword
    def register_new_employee(self, name, email, role, password):
        """Diligencia el formulario de registro de nuevo empleado."""
        # Navegación al formulario (ajusta según tu menú)
        self.sel_lib.click_element(self.MENU_EMPLOYEES)
        self.sel_lib.click_element(self.BTN_ADD_NEW_EMPLOYEE)
        
        # Llenado de campos
        self.sel_lib.wait_until_element_is_visible(self.EMP_NAME)
        self.sel_lib.input_text(self.EMP_NAME, name)
        self.sel_lib.input_text(self.EMP_EMAIL, email)
        
        # Asumiendo un dropdown para el rol
        self.sel_lib.select_from_list_by_label(self.EMP_ROLE, role)
        self.sel_lib.input_text(self.EMP_PASSWORD, password)
        
        # Guardar y validar
        self.sel_lib.click_button(self.BTN_SAVE_EMPLOYEE)
        self.sel_lib.wait_until_page_contains("Empleado registrado exitosamente")