import os

# Rutas absolutas de los archivos que NO deben estar en tests
# Ajustadas a tu estructura de carpetas
files_to_remove = [
    r"C:\portafolio_profesional\banca-automation-python-robotframework\tests\orangehrm_locators.yaml",
    r"C:\portafolio_profesional\banca-automation-python-robotframework\tests\test_data.yaml",
    r"C:\portafolio_profesional\banca-automation-python-robotframework\tests\global_setup.resource",
    r"C:\portafolio_profesional\banca-automation-python-robotframework\tests\orangehrm_page.resource",
    r"C:\portafolio_profesional\banca-automation-python-robotframework\tests\DataLoader.py"
]

print("--- Iniciando limpieza de carpeta tests ---")

for file_path in files_to_remove:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"[ELIMINADO] {file_path}")
        else:
            print(f"[OK - NO EXISTE] {file_path}")
    except Exception as e:
        print(f"[ERROR] No se pudo eliminar {file_path}: {e}")

print("--- Limpieza completada ---")
