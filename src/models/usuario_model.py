from database.connection import get_connection

# Registra un usuario | retorna (True, None) o (False, "mensaje")
def registrar_usuario(datos: dict):
    pass

# Modifica los datos de un usuario | retorna (True, None) o (False, "mensaje")
def modificar_usuario(id_usuario: int, datos: dict):
    pass

# Retorna (True, datos_usuario) o (False, "mensaje")
def validar_inicio_sesion(username: str, password: str):
    pass
