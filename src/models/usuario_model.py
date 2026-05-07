from database.connection import get_connection
from config import DB_EJEMPLO_PATH

DB_PATH = DB_EJEMPLO_PATH # La base de datos usada es la de ejemplo

# Registra un usuario | si faltan datos (obligatorios) retorna (false, "mensaje") else return true
def registrar_usuario(datos: dict):
    pass

# Modifica los datos de un usuario | si no existe en la DB retorna (false, "mensaje") else return true
def modificar_usuario(id_usuario: int, datos: dict):
    pass

# Si el ussername y password son correctos (y existe en la DB) retorna true
# Si la contraseña es incorrecta o el usuario no existe retorna (false, "mensaje")
def validar_inicio_sesion(ussername: str, password: str):
    pass
