import sqlite3
from config import DB_EJEMPLO_PATH

DB_PATH = DB_EJEMPLO_PATH # La base de datos usada es la de ejemplo
_conn = None # Conexion (unica) a la db

def get_connection() -> sqlite3.Connection:
    """Devuelve una conexión única (compartida) para toda la app."""
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(DB_PATH)
        _conn.row_factory = sqlite3.Row # permite acceder a columnas por nombre | row["nombre"] | en vez de indíce
        _conn.execute("PRAGMA foreign_keys = ON;")
    return _conn

def close_connection() -> None:
    """Cierra la conexión compartida (llamar al salir de la app)."""
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None
        