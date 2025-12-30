*** Settings ***
Library      SeleniumLibrary
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
    [Documentation]    Valida que el login fue exitoso verificando el dashboard.
    Wait Until Element Is Visible    ${dashboard.header}    timeout=10s