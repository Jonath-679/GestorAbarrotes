from pathlib import Path

# Carpeta raíz del proyecto + Rutas importantes
ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "data" / "abarrotes.sqlite3"
DB_EJEMPLO_PATH = ROOT_DIR / "data" / "abarrotes_ejemplo.sqlite3"
SCHEMA_PATH = ROOT_DIR / "src" / "database" / "schema.sql"
