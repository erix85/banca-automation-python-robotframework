*** Settings ***
Library    SeleniumLibrary
Library    ../../libraries/selenium_ext.py
Library    ../../libraries/reader_utils.py
Library    ../../config/driver_config.py    env_name=${ENV}    WITH NAME    ConfigManager

*** Variables ***
${ENV}    qa  # Valor por defecto

*** Keywords ***
Setup Del Proyecto
    [Documentation]    Inicializa driver, carga datos y configura logs.
    ${driver}=    ConfigManager.Get Driver Instance
    # Cargamos datos de prueba globales desde un JSON
    ${TEST_DATA}=    Read JSON Data    ${CURDIR}/../../resources/variables/test_data.json
    Set Global Variable    ${GLOBAL_DATA}    ${TEST_DATA}
    
    Log    Iniciando pruebas en entorno: ${ENV}    console=True

Teardown Del Proyecto
    Run Keyword If Test Failed    Capture Page Screenshot
    Close All Browsers