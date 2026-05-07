from database.connection import get_connection
from config import DB_EJEMPLO_PATH

DB_PATH = DB_EJEMPLO_PATH # La base de datos usada es la de ejemplo

# Registra un cliente | si faltan datos (obligatorios) retorna (false, "mensaje") else return true
def registrar_cliente(datos: dict):
    pass

# Modifica los datos de un cliente | si no existe en la DB retorna (false, "mensaje") else return true
def modificar_cliente(id_cliente: int, datos: dict):
    pass

# Retorna una tupla de diccionarios/mapas ({dict}, {dict}...) de todas las coincidencias de la busqueda
# criterio_busqueda es lo que hay en la barra de busqueda | nombre, telefono o direccion | si esta vacio retorna todo los clientes
def buscar_cliente(criterio_busqueda: str):
    pass
