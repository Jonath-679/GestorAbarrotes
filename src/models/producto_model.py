from database.connection import get_connection

# Registra un producto | retorna (True, None) o (False, "mensaje")
def registrar_producto(datos: dict):
    pass

# Modifica los datos de un producto | retorna (True, None) o (False, "mensaje")
def modificar_producto(id_producto: int, datos: dict):
    pass

# Actualiza el stock de un producto | retorna (True, None) o (False, "mensaje")
def actualizar_stock(id_producto: int):
    pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
# criterio_busqueda es lo que hay en la barra de busqueda | nombre, codigo, o categoria | si esta vacio retorna todo los productos
def buscar_producto(criterio_busqueda: str):
    pass

# Retorna (True, stock) o (False, "mensaje")
def consultar_stock(id_producto: int):
    pass
