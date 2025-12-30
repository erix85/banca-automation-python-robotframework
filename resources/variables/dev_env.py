# resources/variables/dev_env.py

def get_variables():
    """Retorna un diccionario de variables para el entorno de DEV."""
    variables = {
        "URL_LOGIN": "https://dev-banca.ejemplo.com/login",
        "API_TIMEOUT": 5000,
        "DB_CONFIG": {
            "host": "dev-db.internal",
            "port": 5432
        }
    }
    return variables