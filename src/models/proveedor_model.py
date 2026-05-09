from src.database.connection import get_connection

def registrar_proveedor(datos: dict):
    """
    Inserta un nuevo registro en la tabla proveedores

    Args:
        datos (dict): Todos los datos a registrar (nombre, telefono, estado, direccion (opcional))
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "INSERT INTO proveedores (nombre, telefono, estado, direccion) VALUES (?, ?, ?, ?)"
        values = (datos["nombre"], datos["telefono"], datos["estado"], datos.get("direccion"))
        cursor.execute(sql_prompt, values)
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def modificar_proveedor(id_proveedor: int, datos: dict):
    """
    Modifica valores de un registro en la tabla proveedores
    -- el proveedor debe existir en la DB

    Args:
        id_proveedor:
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
        sql_prompt = "UPDATE proveedores SET"
        values = []
        # Construir sql_prompt y sus valores
        for key, value in datos.items():
            sql_prompt += f" {key} = ?,"
            values.append(value)
        sql_prompt = sql_prompt[:-1] # Remueve la ultima coma ,
        sql_prompt += f" WHERE id_proveedor = ?"
        values.append(id_proveedor)
        # Ejecutar sql_prompt + guardar
        cursor.execute(sql_prompt, tuple(values))
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None) 

def buscar_proveedor(criterio_busqueda: str):
    """
    Busca todos los registros en la tabla proveedores que cumplan con el criterio de busqueda

    Args:
        criterio_busqueda: es lo que hay en la barra de busqueda
            si esta vacio retornara todos los registros de la tabla proveedores
            si tiene contenido, se buscaran por nombre, telefono y direccion
    Returns:
        Si todo sale bien: (True, tupla_de_diccionarios)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = ""
        if not criterio_busqueda:
            sql_prompt = "SELECT * from proveedores"
            cursor.execute(sql_prompt)
        else:
            sql_prompt = "SELECT * from proveedores WHERE nombre LIKE '%' || ? || '%' COLLATE NOCASE OR telefono LIKE '%' || ? || '%' COLLATE NOCASE OR direccion LIKE '%' || ? || '%' COLLATE NOCASE"
            cursor.execute(sql_prompt, (criterio_busqueda, criterio_busqueda, criterio_busqueda))
        proveedores = tuple(dict(row) for row in cursor.fetchall())
        return (True, proveedores)
    except Exception as e:
        return (False, f"Error: {e}")

def validar_proveedor(id_proveedor: int):
    """
    Valida si el id_proveedor existe en la DB
    
    Args:
        id_proveedor:
    Returns:
        Si existe: (True, True)
        Si no existe: (True, False)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "SELECT id_proveedor FROM proveedores WHERE id_proveedor = ?"
        cursor.execute(sql_prompt, (id_proveedor,))
        row = cursor.fetchone()
        # Validacion
        if row: # Existe
            return (True, True)
        else: # No existe
            return (True, False) 
    except Exception as e:
        return (False, f"Error: {e}")
    