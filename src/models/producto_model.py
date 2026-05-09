from src.database.connection import get_connection

def registrar_producto(datos: dict):
    """
    Inserta un nuevo registro en la tabla productos
    -- Deben estar todos los datos (excepto id_producto)-(descripcion es opcional)

    Args:
        datos (dict): Todos los datos a registrar (nombre, codigo, id_categoria, stock, precio, descripcion (opcional))
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "INSERT INTO productos (nombre, codigo, id_categoria, stock, precio, descripcion) VALUES (?, ?, ?, ?, ?, ?)"
        values = (datos["nombre"], datos["codigo"], datos["id_categoria"], datos["stock"], datos["precio"], datos.get("descripcion"))
        cursor.execute(sql_prompt, values)
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def modificar_producto(codigo: str, datos: dict):
    """
    Modifica valores de un registro en la tabla productos
    -- el producto debe existir en la DB

    Args:
        codigo: codigo del producto
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
        sql_prompt = "UPDATE productos SET"
        values = []
        # Construir sql_prompt y sus valores
        for key, value in datos.items():
            sql_prompt += f" {key} = ?,"
            values.append(value)
        sql_prompt = sql_prompt[:-1] # Remueve la ultima coma ,
        sql_prompt += f" WHERE codigo = ?"
        values.append(codigo)
        # Ejecutar sql_prompt + guardar
        cursor.execute(sql_prompt, tuple(values))
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def actualizar_stock(codigo: str, stock: int, commit: bool=True):
    """
    Actualiza el campo stock de un registro de la tabla productos
    -- esta funcion tambien la puede realizar modificar_producto,
        pero esta es una forma mas "directa" de modificar solo el stock
        ya que es una operacion recurrente
    --el producto debe existir en la DB

    Args:
        codigo: codigo del producto
        stock: nuevo valor para stock
        commit: si es True confirma la transaccion; si es False no hace commit
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "UPDATE productos SET stock = ? WHERE codigo = ?"
        cursor.execute(sql_prompt, (stock, codigo))
        if commit:
            conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def buscar_producto(criterio_busqueda: str):
    """
    Busca todos los registros en la tabla productos que cumplan con el criterio de busqueda

    Args:
        criterio_busqueda: es lo que hay en la barra de busqueda
            si esta vacio retornara todos los registros de la tabla productos
            si tiene contenido, se buscaran por nombre, id_categoria y codigo
    Returns:
        Si todo sale bien: (True, tupla_de_diccionarios)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = ""
        if not criterio_busqueda:
            sql_prompt = "SELECT * from productos"
            cursor.execute(sql_prompt)
        else:
            sql_prompt = "SELECT * from productos WHERE nombre LIKE '%' || ? || '%' COLLATE NOCASE OR codigo LIKE '%' || ? || '%' COLLATE NOCASE OR CAST(id_categoria AS TEXT) LIKE '%' || ? || '%' COLLATE NOCASE"
            cursor.execute(sql_prompt, (criterio_busqueda, criterio_busqueda, criterio_busqueda))
        productos = tuple(dict(row) for row in cursor.fetchall())
        return (True, productos)
    except Exception as e:
        return (False, f"Error: {e}")

def consultar_stock(codigo: str):
    """
    Retorna el stock de un producto
    --el producto debe existir en la DB

    Args:
        codigo: codigo del producto
    Returns:
        Si todo sale bien: (True, stock)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "SELECT stock FROM productos WHERE codigo = ?"
        cursor.execute(sql_prompt, (codigo,))
        row = cursor.fetchone()
        if row is None:
            return (False, "Error: el producto no existe en la db")
        return (True, row[0])
    except Exception as e:
        return (False, f"Error: {e}")

######################### PRUEVAS #########################

if __name__ == "__main__":

    # buscar_producto()
    criterio = input("Barra_busqueda: ")

    status, productos = buscar_producto(criterio)

    if not status:
        print(productos)
    elif not productos:
        print("Sin resultados")
    else:
        for producto in productos:
            print(producto)
