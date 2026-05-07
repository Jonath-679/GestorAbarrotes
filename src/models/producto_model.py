from database.connection import get_connection
from config import DB_EJEMPLO_PATH

DB_PATH = DB_EJEMPLO_PATH # La base de datos usada es la de ejemplo

# Registra un producto | si faltan datos (obligatorios) retorna (false, "mensaje") else return true
def registrar_producto(datos: dict):
    pass

# Modifica los datos de un producto | si no existe en la DB retorna (false, "mensaje") else return true
def modificar_producto(id_producto: int, datos: dict):
    pass

# Actualiza el stock de un producto | si no existe en la DB retorna (false, "mensaje") else return true
def actualizar_stock(id_producto: int):
    pass

# Retorna una tupla de diccionarios/mapas ({dict}, {dict}...) de todas las coincidencias de la busqueda
# criterio_busqueda es lo que hay en la barra de busqueda | nombre, codigo, o categoria | si esta vacio retorna todo los productos
def buscar_producto(criterio_busqueda: str):
    pass

# Retorna el stock de un producto | si no existe en la DB retorna (false, "mensaje")
def consultar_stock(id_producto: int):
    pass
