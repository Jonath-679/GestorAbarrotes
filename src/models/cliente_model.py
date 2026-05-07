from database.connection import get_connection

# Registra un cliente | retorna (True, None) o (False, "mensaje")
def registrar_cliente(datos: dict):
    pass

# Modifica los datos de un cliente | retorna (True, None) o (False, "mensaje")
def modificar_cliente(id_cliente: int, datos: dict):
    pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
# criterio_busqueda es lo que hay en la barra de busqueda | nombre, telefono o direccion | si esta vacio retorna todo los clientes
def buscar_cliente(criterio_busqueda: str):
    pass
