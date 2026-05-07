# venta_model && detalle_venta_model
from database.connection import get_connection
from config import DB_EJEMPLO_PATH

DB_PATH = DB_EJEMPLO_PATH # La base de datos usada es la de ejemplo

# Registra una venta | si faltan datos (obligatorios) retorna (false, "mensaje") else return true
def registrar_venta(datos: dict):
    pass

# Retorna todos los datos (incluyendo venta_detalles) de una venta si no existe en la DB retorna (false, "mensaje")
def listar_venta(id_venta: int):
    pass
