*** Settings ***
Resource          ../resources/common/global_setup.resource
Resource          ../resources/pages/orangehrm_page.resource
Test Setup        Setup Del Proyecto
Test Teardown     Teardown Del Proyecto

*** Test Cases ***
Login Exitoso Con Datos Desde JSON
    [Tags]    Smoke    Sprint1
    # Usamos los datos cargados por el Reader
    Given El usuario tiene credenciales validas para el perfil "Admin"
    When Intenta iniciar sesion
    Then El sistema le permite ver su saldo de cuenta

Crear Y Autenticar Nuevo Empleado
    [Tags]    Regression    Sprint2
    Given El administrador crea un nuevo empleado
    When El nuevo empleado inicia sesion
    Then El sistema le da la bienvenida
    And El nuevo empleado cierra sesion

Crear Y Buscar Nuevo Empleado
    [Tags]    Regression    Sprint3
    Given El administrador esta autenticado en el sistema
    When Crea un nuevo empleado con un nombre unico
    And Busca al empleado recien creado
    Then El empleado aparece en los resultados de busqueda
    And El administrador cierra sesion

*** Keywords ***
El usuario tiene credenciales validas para el perfil "${perfil}"
    ${user}=    Set Variable    ${GLOBAL_DATA['users']['${perfil}']['username']}
    ${pass}=    Set Variable    ${GLOBAL_DATA['users']['${perfil}']['password']}
    Set Test Variable    ${USER}    ${user}
    Set Test Variable    ${PASS}    ${pass}

Intenta iniciar sesion
    # Esta keyword viene de orange_page.resource y usa selenium_ext internamente
    Autenticar Usuario    ${USER}    ${PASS}

El sistema le permite ver su saldo de cuenta
    Wait Until Element Is Visible    ${dashboard.user_dropdown}    timeout=10s

El administrador crea un nuevo empleado
    ${admin_user}=    Set Variable    ${GLOBAL_DATA['users']['Admin']['username']}
    ${admin_pass}=    Set Variable    ${GLOBAL_DATA['users']['Admin']['password']}
    Autenticar Usuario    ${admin_user}    ${admin_pass}
    El sistema le permite ver su saldo de cuenta
    Navegar a la creacion de nuevo empleado
    ${new_username}=    Generar username unico
    ${new_password}=    Set Variable    TestPassword123!
    Set Test Variable    ${NEW_USER}    ${new_username}
    Set Test Variable    ${NEW_PASS}    ${new_password}
    Completar formulario de nuevo empleado    Test    Middle    User    ${NEW_USER}    ${NEW_PASS}
    Verificar creacion de nuevo usuario
    Cerrar Sesion

El nuevo empleado inicia sesion
    Autenticar Usuario    ${NEW_USER}    ${NEW_PASS}

El sistema le da la bienvenida
    El sistema le permite ver su saldo de cuenta

El nuevo empleado cierra sesion
    Cerrar Sesion

El administrador esta autenticado en el sistema
    ${admin_user}=    Set Variable    ${GLOBAL_DATA['users']['Admin']['username']}
    ${admin_pass}=    Set Variable    ${GLOBAL_DATA['users']['Admin']['password']}
    Autenticar Usuario    ${admin_user}    ${admin_pass}
    El sistema le permite ver su saldo de cuenta

Crea un nuevo empleado con un nombre unico
    Navegar a la creacion de nuevo empleado
    ${random_string}=    Generate Random String    5    [LOWER]
    ${first_name}=    Set Variable    TestName_${random_string}
    ${middle_name}=    Set Variable    TestMiddle
    ${last_name}=    Set Variable    TestLastName
    ${new_username}=    Generar username unico
    ${new_password}=    Set Variable    TestPassword123!
    Set Test Variable    ${EMP_FIRST_NAME}    ${first_name}
    Completar formulario de nuevo empleado    ${first_name}    ${middle_name}    ${last_name}    ${new_username}    ${new_password}
    Verificar creacion de nuevo usuario

Busca al empleado recien creado
    Navegar a la lista de empleados
    Buscar empleado por nombre    ${EMP_FIRST_NAME}

El empleado aparece en los resultados de busqueda
    Verificar que el empleado aparece en los resultados    ${EMP_FIRST_NAME}

El administrador cierra sesion
    Cerrar Sesion