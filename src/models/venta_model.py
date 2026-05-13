# venta_model && detalle_venta_model
from database.connection import get_connection
from models.producto_model import actualizar_stock

def registrar_venta(datos: dict):
    """
    Inserta un nuevo registro en la tabla ventas

    Args:
        datos (dict): datos a registrar (id_usuario, id_cliente, total)
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "INSERT INTO ventas (id_usuario, id_cliente, total) VALUES (?, ?, ?)"
        values = (datos["id_usuario"], datos.get("id_cliente"), datos["total"])
        cursor.execute(sql_prompt, values)
        id_venta = cursor.lastrowid
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, id_venta)

def registrar_venta_transaccional(id_venta: int, detalles: list[dict]):
    """
    Registra los detalles de una venta y actualiza el total en una transaccion

    Args:
        id_venta: id de la venta ya creada
        detalles (list[dict]): lista de detalles (id_producto, cantidad, precio_unitario)
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        conexion.execute("BEGIN")
        total = 0.0
        for detalle in detalles:
            id_producto = detalle["id_producto"]
            cantidad = detalle["cantidad"]
            precio_unitario = detalle["precio_unitario"]
            subtotal = float(cantidad) * float(precio_unitario)
            cursor.execute(
                "SELECT codigo, stock FROM productos WHERE id_producto = ?",
                (id_producto,),
            )
            row = cursor.fetchone()
            codigo = row["codigo"]
            stock_actual = row["stock"]
            cursor.execute(
                """
                INSERT INTO detalle_ventas (
                    id_venta, id_producto, cantidad, precio_unitario, subtotal
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (id_venta, id_producto, cantidad, precio_unitario, subtotal),
            )
            status, msg = actualizar_stock(codigo, stock_actual - cantidad, commit=False)
            if not status:
                raise RuntimeError(msg)
            total += subtotal
        cursor.execute(
            "UPDATE ventas SET total = ? WHERE id_venta = ?",
            (round(total, 2), id_venta),
        )
        conexion.commit()
    except Exception as e:
        if conexion is not None:
            try:
                conexion.rollback()
            except Exception:
                pass
        return (False, f"Error: {e}")
    else:
        return (True, None)

def listar_ventas():
    """
    Retorna todos los registros de la tabla ventas

    Args:
        N/A
    Returns:
        Si todo sale bien: (True, tupla_de_diccionarios)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ventas ORDER BY fecha_hora DESC")
        ventas = tuple(dict(row) for row in cursor.fetchall())
        return (True, ventas)
    except Exception as e:
        return (False, f"Error: {e}")

def validar_venta(id_venta: int):
    """
    Valida si el id_venta existe en la DB
    
    Args:
        id_venta:
    Returns:
        Si existe: (True, True)
        Si no existe: (True, False)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "SELECT id_venta FROM ventas WHERE id_venta = ?"
        cursor.execute(sql_prompt, (id_venta,))
        row = cursor.fetchone()
        # Validacion
        if row: # Existe
            return (True, True)
        else: # No existe
            return (True, False) 
    except Exception as e:
        return (False, f"Error: {e}")
    