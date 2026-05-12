import sqlite3
import os
from config import DB_EJEMPLO_PATH, DB_PATH as DB_REAL_PATH, SCHEMA_PATH

DB_PATH = DB_EJEMPLO_PATH # La base de datos usada es la de ejemplo
_conn = None # Conexion (unica) a la db

def set_database(use_ejemplo: bool):
    """Cambia la ruta de la base de datos y cierra la conexión actual si existiera para forzar la reconexión."""
    global DB_PATH, _conn
    if use_ejemplo:
        DB_PATH = DB_EJEMPLO_PATH
    else:
        DB_PATH = DB_REAL_PATH
    close_connection()

def _inicializar_esquema(conexion: sqlite3.Connection):
    """Lee el esquema y lo aplica a la bd si hace falta, y asegura un usuario admin initial."""
    try:
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            esquema = f.read()
        conexion.executescript(esquema)
        
        # Verificar y agregar admin default si no existe
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE username = 'admin'")
        if not cursor.fetchone():
            cursor.execute('''
                INSERT INTO usuarios (nombre, username, password, rol, estado) 
                VALUES ('Administrador', 'admin', 'contraseña', 'ADMIN', 1)
            ''')
            conexion.commit()
    except Exception as e:
        print(f"Error inicializando esquema: {e}")

def get_connection() -> sqlite3.Connection:
    """Devuelve una conexión única (compartida) para toda la app."""
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(DB_PATH)
        _conn.row_factory = sqlite3.Row # permite acceder a columnas por nombre | row["nombre"] | en vez de indíce
        _conn.execute("PRAGMA foreign_keys = ON;")
        _inicializar_esquema(_conn)
    return _conn

def close_connection() -> None:
    """Cierra la conexión compartida (llamar al salir de la app)."""
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None
        