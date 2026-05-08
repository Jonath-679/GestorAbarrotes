from src.database.connection import get_connection

def registrar_cliente(datos: dict):
    """
    Inserta un nuevo registro en la tabla clientes
    -- Deben estar todos los datos (excepto id_cliente)-(direccion es opcional)

    Args:
        datos (dict): Todos los datos a registrar (nombre, telefono, estado, direccion (opcional))
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "INSERT INTO clientes (nombre, telefono, estado, direccion) VALUES (?, ?, ?, ?)"
        values = (datos["nombre"], datos["telefono"], datos["estado"], datos.get("direccion"))
        cursor.execute(sql_prompt, values)
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def modificar_cliente(id_cliente: int, datos: dict):
    """
    Modifica valores de un registro en la tabla clientes
    -- el cliente debe existir en la DB

    Args:
        id_cliente:
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
        sql_prompt = "UPDATE clientes SET"
        values = []
        # Construir sql_prompt y sus valores
        for key, value in datos.items():
            sql_prompt += f" {key} = ?,"
            values.append(value)
        sql_prompt = sql_prompt[:-1] # Remueve la ultima coma ,
        sql_prompt += f" WHERE id_cliente = ?"
        values.append(id_cliente)
        # Ejecutar sql_prompt + guardar
        cursor.execute(sql_prompt, tuple(values))
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def buscar_cliente(criterio_busqueda: str):
    """
    Busca todos los registros en la tabla clientes que cumplan con el criterio de busqueda

    Args:
        criterio_busqueda: es lo que hay en la barra de busqueda
            si esta vacio retornara todos los registros de la tabla clientes
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
            sql_prompt = "SELECT * from clientes"
            cursor.execute(sql_prompt)
        else:
            sql_prompt = "SELECT * from clientes WHERE nombre LIKE '%' || ? || '%' COLLATE NOCASE OR telefono LIKE '%' || ? || '%' COLLATE NOCASE OR direccion LIKE '%' || ? || '%' COLLATE NOCASE"
            cursor.execute(sql_prompt, (criterio_busqueda, criterio_busqueda, criterio_busqueda))
        clientes = tuple(dict(row) for row in cursor.fetchall())
        return (True, clientes)
    except Exception as e:
        return (False, f"Error: {e}")

######################### PRUEVAS #########################

if __name__ == "__main__":

    # buscar_producto()
    criterio = input("Barra_busqueda: ")

    status, productos = buscar_cliente(criterio)

    if not status:
        print(productos)
    elif not productos:
        print("Sin resultados")
    else:
        for producto in productos:
            print(producto)
