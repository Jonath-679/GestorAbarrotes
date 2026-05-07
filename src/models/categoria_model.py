from database.connection import get_connection

# Registra una categoria | retorna (True, None) o (False, "mensaje")
def registrar_categoria(datos: dict):
	pass

# Modifica los datos de una categoria | retorna (True, None) o (False, "mensaje")
def modificar_categoria(id_categoria: int, datos: dict):
	pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
# criterio_busqueda es lo que hay en la barra de busqueda | nombre o descripcion | si esta vacio retorna todas las categorias
def buscar_categoria(criterio_busqueda: str):
	pass
