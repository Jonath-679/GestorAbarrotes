from database.connection import get_connection

def registrar_log(datos: dict):
    """
    Inserta un nuevo registro en la tabla logs

    Args:
        datos (dict): Todos los datos a registrar (id_usuario, accion, modulo (opcional), descripcion (opcional))
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "INSERT INTO logs (id_usuario, accion, modulo, descripcion) VALUES (?, ?, ?, ?)"
        values = (datos["id_usuario"], datos["accion"], datos.get("modulo"), datos.get("descripcion"))
        cursor.execute(sql_prompt, values)
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def listar_logs():
    """
    Retorna todos los registros de la tabla logs

    Args:
        N/A
    Returns:
        Si todo sale bien: (True, tupla_de_diccionarios)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM logs ORDER BY fecha_hora DESC")
        logs = tuple(dict(row) for row in cursor.fetchall())
        return (True, logs)
    except Exception as e:
        return (False, f"Error: {e}")

######################### PRUEVAS #########################

if __name__ == "__main__":

    # listar_logs()
    status, logs = listar_logs()

    if not status:
        print(logs)
    elif not logs:
        print("Sin resultados")
    else:
        for log in logs:
            print(log)
    