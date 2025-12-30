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

*** Keywords ***
El usuario tiene credenciales validas para el perfil "${perfil}"
    ${user}=    Set Variable    ${GLOBAL_DATA['users']['${perfil}']['username']}
    ${pass}=    Set Variable    ${GLOBAL_DATA['users']['${perfil}']['password']}
    Set Test Variable    ${USER}    ${user}
    Set Test Variable    ${PASS}    ${pass}

Intenta iniciar sesion
    # Esta keyword viene de orange_page.resource y usa selenium_ext internamente
    Autenticar Usuario    ${USER}    ${PASS}