*** Settings ***
Library      SeleniumLibrary
Library      String
Library      ../../libraries/selenium_ext.py
Variables    ../locators/orangehrm_locators.yaml

*** Keywords ***
Autenticar Usuario
    [Arguments]    ${user}    ${pass}
    [Documentation]    Realiza el login usando los locators del YAML.
    Wait Until Element Is Visible    ${login.username}
    Input Text    ${login.username}    ${user}
    Input Text    ${login.password}    ${pass}
    Wait And Click    ${login.submit_btn}

El sistema le permite ver su saldo de cuenta
    [Documentation]    Valida que el login fue exitoso verificando el dropdown de usuario.
    Wait Until Element Is Visible    ${dashboard.user_dropdown}    timeout=10s

Navegar a la creacion de nuevo empleado
    [Documentation]    Navega a PIM -> Add Employee.
    Wait And Click    ${pim.menu_item}
    Wait And Click    ${pim.add_employee_link}

Generar username unico
    [Documentation]    Crea un nombre de usuario unico para el nuevo empleado.
    ${random_string}=    Generate Random String    8    [LOWER]
    ${unique_username}=    Set Variable    testuser_${random_string}
    RETURN    ${unique_username}

Completar formulario de nuevo empleado
    [Arguments]    ${first_name}    ${middle_name}    ${last_name}    ${new_username}    ${new_password}
    [Documentation]    Rellena el formulario para crear un nuevo empleado con credenciales, incluyendo el segundo nombre.
    Wait And Input Text    ${pim.first_name_input}    ${first_name}
    Wait And Input Text    ${pim.middle_name_input}    ${middle_name}
    Wait And Input Text    ${pim.last_name_input}    ${last_name}
    Wait And Click    ${pim.create_login_switch}
    Wait And Input Text    ${pim.username_input}    ${new_username}
    Wait And Input Text    ${pim.password_input}    ${new_password}
    Wait And Input Text    ${pim.confirm_password_input}    ${new_password}
    Wait And Click    ${pim.save_btn}

Verificar creacion de nuevo usuario
    [Documentation]    Verifica que el toast de exito aparezca.
    Wait Until Element Is Visible    ${pim.success_toast}    timeout=10s

Cerrar Sesion
    [Documentation]    Cierra la sesion del usuario actual.
    Wait And Click    ${logout.user_dropdown}
    Wait And Click    ${logout.logout_link}
    Wait Until Element Is Visible    ${login.username}

Navegar a la lista de empleados
    [Documentation]    Navega a PIM -> Employee List.
    Wait And Click    ${pim.menu_item}
    Wait And Click    ${pim_search.employee_list_link}

Buscar empleado por nombre
    [Arguments]    ${nombre_empleado}
    [Documentation]    Busca un empleado por su nombre en la lista de empleados.
    Wait Until Element Is Visible    ${pim_search.employee_name_input}
    Input Text    ${pim_search.employee_name_input}    ${nombre_empleado}
    # Esperar a que las sugerencias de autocompletado aparezcan y seleccionar la primera
    Wait Until Element Is Visible    xpath=//div[@role="listbox"]
    Click Element    xpath=(//div[@role="option"])[1]
    Wait And Click    ${pim_search.search_btn}

Verificar que el empleado aparece en los resultados
    [Arguments]    ${nombre_empleado}
    [Documentation]    Verifica que el nombre del empleado está presente en la tabla de resultados.
    Wait Until Element Is Visible    ${pim_search.records_table}
    ${nombre_visible}=    Is Element Visible    xpath=//div[@class="oxd-table-body"]//div[contains(text(),'${nombre_empleado}')]
    Should Be True    ${nombre_visible}    msg=El empleado '${nombre_empleado}' no fue encontrado en los resultados.