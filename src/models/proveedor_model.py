from database.connection import get_connection

# Registra un proveedor | retorna (True, None) o (False, "mensaje")
def registrar_proveedor(datos: dict):
    pass

# Modifica los datos de un proveedor | retorna (True, None) o (False, "mensaje")
def modificar_proveedor(id_proveedor: int, datos: dict):
    pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
# criterio_busqueda es lo que hay en la barra de busqueda | nombre, telefono o direccion | si esta vacio retorna todo los proveedores
def buscar_proveedor(criterio_busqueda: str):
    pass
