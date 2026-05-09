from src.database.connection import get_connection

def registrar_categoria(datos: dict):
	"""
	Inserta un nuevo registro en la tabla categorias
	-- Deben estar nombre y estado (descripcion es opcional)

	Args:
		datos (dict): Todos los datos a registrar (nombre, estado, descripcion (opcional))
	Returns:
		Si todo sale bien: (True, None)
		Si algo falla: (False, "mensaje")
	"""
	try:
		conexion = get_connection()
		cursor = conexion.cursor()
		sql_prompt = "INSERT INTO categorias (nombre, estado, descripcion) VALUES (?, ?, ?)"
		values = (datos["nombre"], datos["estado"], datos.get("descripcion"))
		cursor.execute(sql_prompt, values)
		conexion.commit()
	except Exception as e:
		return (False, f"Error: {e}")
	else:
		return (True, None)

def modificar_categoria(nombre: str, datos: dict):
	"""
	Modifica valores de un registro en la tabla categorias
	-- la categoria debe existir en la DB

	Args:
		nombre: nombre de la categoria (unique)
		datos (dict): Todos los datos a modificar (debe haber al menos un campo)
	Returns:
		Si todo sale bien: (True, None)
		Si algo falla: (False, "mensaje")
	"""
	try:
		if not datos: # Validacion de contenido en datos: dict
			return (False, "Error: no hay ningun campo a modificar")
		conexion = get_connection()
		cursor = conexion.cursor()
		sql_prompt = "UPDATE categorias SET"
		values = []
		# Construir sql_prompt y sus valores
		for key, value in datos.items():
			sql_prompt += f" {key} = ?,"
			values.append(value)
		sql_prompt = sql_prompt[:-1] # Remueve la ultima coma ,
		sql_prompt += f" WHERE nombre = ?"
		values.append(nombre)
		# Ejecutar sql_prompt + guardar
		cursor.execute(sql_prompt, tuple(values))
		conexion.commit()
	except Exception as e:
		return (False, f"Error: {e}")
	else:
		return (True, None)

def buscar_categoria(criterio_busqueda: str):
    """
    Busca todos los registros en la tabla categorias que cumplan con el criterio de busqueda
	
    Args:
        criterio_busqueda: es lo que hay en la barra de busqueda
            si esta vacio retornara todos los registros de la tabla categorias
            si tiene contenido, se buscaran por nombre y descripcion
    Returns:
        Si todo sale bien: (True, tupla_de_diccionarios)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = ""
        if not criterio_busqueda:
            sql_prompt = "SELECT * from categorias ORDER BY estado DESC"
            cursor.execute(sql_prompt)
        else:
            sql_prompt = "SELECT * from categorias WHERE nombre LIKE '%' || ? || '%' COLLATE NOCASE OR descripcion LIKE '%' || ? || '%' COLLATE NOCASE ORDER BY estado DESC"
            cursor.execute(sql_prompt, (criterio_busqueda, criterio_busqueda))
        categorias = tuple(dict(row) for row in cursor.fetchall())
        return (True, categorias)
    except Exception as e:
        return (False, f"Error: {e}")

def validar_categoria(nombre: str):
    """
    Valida si el nombre de categoria existe en la DB
    
    Args:
        nombre: nombre de categoria
    Returns:
        Si existe: (True, True)
        Si no existe: (True, False)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "SELECT nombre FROM categorias WHERE nombre = ?"
        cursor.execute(sql_prompt, (nombre,))
        row = cursor.fetchone()
        # Validacion
        if row: # Existe
            return (True, True)
        else: # No existe
            return (True, False) 
    except Exception as e:
        return (False, f"Error: {e}")
	
######################### PRUEVAS #########################

if __name__ == "__main__":

	# buscar_categoria()
	criterio = input("Barra_busqueda: ")

	status, categorias = buscar_categoria(criterio)

	if not status:
		print(categorias)
	elif not categorias:
		print("Sin resultados")
	else:
		for categoria in categorias:
			print(categoria)
	