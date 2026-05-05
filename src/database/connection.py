import sqlite3
from pathlib import Path

# Carpeta raíz del proyecto (…/src/database/connection.py -> raíz)
BASE_DIR = Path(__file__).resolve().parents[2]

# Ruta de la base de datos SQLite
DB_PATH = BASE_DIR / "data" / "abarrotes.sqlite3"


def get_connection() -> sqlite3.Connection:
    """
    Retorna una conexión a la base de datos con foreign keys activadas.
    Úsala así:
        with get_connection() as conn:
            ...
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acceder a columnas por nombre: row["nombre"]
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
