# venta_model && detalle_venta_model
from database.connection import get_connection

# Registra una venta | retorna (True, None) o (False, "mensaje")
def registrar_venta(datos: dict):
    pass

# Registra una venta y sus detalles en una sola transaccion
# Inserta en ventas, detalle_ventas y actualiza stock | retorna (True, None) o (False, "mensaje")
def registrar_venta_transaccional(datos_venta: dict, detalles: list[dict]):
    pass

# Retorna (True, datos_venta) o (False, "mensaje")
def listar_venta(id_venta: int):
    pass
