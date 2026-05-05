from pathlib import Path

# Carpeta raíz del proyecto
ROOT_DIR = Path(__file__).resolve().parents[1]
# Ruta de la base de datos
DB_PATH = ROOT_DIR / "data" / "abarrotes.sqlite3"
