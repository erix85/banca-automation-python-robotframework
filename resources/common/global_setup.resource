*** Settings ***
Library    SeleniumLibrary
Library    ../../libraries/selenium_ext.py
Library    ../../libraries/reader_utils.py
Library    ../../libraries/DataLoader.py
Library    ../../libraries/BrowserSetup.py

*** Variables ***
${ENV}    qa  # Valor por defecto

*** Keywords ***
Setup Del Proyecto
    [Documentation]    Inicializa driver, carga datos y configura logs.
    Open Configured Browser    ${ENV}
    # Cargamos datos de prueba globales desde el YAML
    Load Test Data    ${CURDIR}/../../resources/variables/test_data.yaml
    
    Log    Iniciando pruebas en entorno: ${ENV}    console=True

Teardown Del Proyecto
    Run Keyword If Test Failed    Capture Page Screenshot
    Close All Browsers