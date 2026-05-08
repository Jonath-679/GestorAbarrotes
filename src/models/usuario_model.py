from src.database.connection import get_connection

def registrar_usuario(datos: dict):
    """
    Inserta un nuevo registro en la tabla usuarios
    -- Deben estar todos los datos (excepto id_usuario)-(ninguno es opcional)

    Args:
        datos (dict): Todos los datos a registrar (nombre, username, password, rol, estado)
    Returns:
        Si todo sale bien: (True, None)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "INSERT INTO usuarios (nombre, username, password, rol, estado) VALUES (?, ?, ?, ?, ?)"
        values = (datos["nombre"], datos["username"], datos["password"], datos["rol"], datos["estado"])
        cursor.execute(sql_prompt, values)
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)
     
def modificar_usuario(username: str, datos: dict):
    """
    Modifica valores de un registro en la tabla usuarios
    -- el usuario debe existir en la DB

    Args:
        username: nombre de usuario
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
        sql_prompt = "UPDATE usuarios SET"
        values = []
        # Construir sql_prompt y sus valores
        for key, value in datos.items():
            sql_prompt += f" {key} = ?,"
            values.append(value)
        sql_prompt = sql_prompt[:-1] # Remueve la ultima coma ,
        sql_prompt += f" WHERE username = ?"
        values.append(username)
        # Ejecutar sql_prompt + guardar
        cursor.execute(sql_prompt, tuple(values))
        conexion.commit()
    except Exception as e:
        return (False, f"Error: {e}")
    else:
        return (True, None)

def validar_inicio_sesion(username: str, password: str):
    """
    Valida que la contraseña corresponde a la del username
    -- el usuario debe existir en la DB

    Args:
        username: nombre de usuario
        password: contraseña
    Returns:
        Si todo sale bien y el password es correcto: (True, True)
        Si todo sale bien y el password es incorrecto: (True, False)
        Si username no existe: (False, "Error: el username no existe en la db")
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "SELECT password FROM usuarios WHERE username = ?"
        cursor.execute(sql_prompt, (username,))
        row = cursor.fetchone()
        if row is None: # Usuario inexistente
            return (False, "Error: el username no existe en la db")
        real_password = row[0]
        if real_password == password:
            return (True, True)
        else:
            return (True, False)
    except Exception as e:
        return (False, f"Error: {e}")
    
def validar_usuario(username: str):
    """
    Valida si el username existe en la DB
    
    Args:
        username: nombre de usuario
    Returns:
        Si existe: (True, True)
        Si no existe: (True, False)
        Si algo falla: (False, "mensaje")
    """
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql_prompt = "SELECT username FROM usuarios WHERE username = ?"
        cursor.execute(sql_prompt, (username,))
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

    # registrar_usuario()
    """
    datos = {}
    nombre = input("Nombre: ")
    datos["nombre"] = nombre
    username = input("Username: ")
    datos["username"] = username
    password = input("Password: ")
    datos["password"] = password
    rol = input("ROL(ADMIN, CAJERO): ")
    datos["rol"] = rol
    estado = int(input("Estado(1 or 0): "))
    datos["estado"] = estado
    status, value = registrar_usuario(datos)
    if not status:
        print(value)
    else:
        print("Registro exitoso")
    """

    # modificar_usuario()
    """
    datos = {}
    username = input("Username: ")
    datos["username"] = username
    password = input("Password: ")
    datos["password"] = password
    rol = input("ROL(ADMIN, CAJERO): ")
    datos["rol"] = rol
    estado = int(input("Estado(1 or 0): "))
    datos["estado"] = estado
    status, value = modificar_usuario(username, datos)
    if not status:
        print(value)
    else:
        print("Edicion exitosa")
    """

    # validar_inicio_sesion()
    """
    username = input("Username: ")
    password = input("Password: ")
    status, value = validar_inicio_sesion(username, password)
    if not status:
        print(value)
    elif value == True:
        print("Contraseña correcta carnal")
    else:
        print("Contraseña incorrecta carnal")
    """

    # validar_usuario()
    username = input("Username: ")
    status, value = validar_usuario(username)
    if not status:
        print(value)
    elif value:
        print("Si existe xd")
    else:
        print("No existe")
