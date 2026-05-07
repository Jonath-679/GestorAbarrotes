from database.connection import get_connection

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
# fecha_inicio y fecha_fin deben tener el formato usado por SQLite (YYYY-MM-DD o YYYY-MM-DD HH:MM:SS)
def reporte_ventas_rango(fecha_inicio: str, fecha_fin: str):
    pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
def reporte_ventas_por_cajero(id_usuario: int, fecha_inicio: str, fecha_fin: str):
    pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
def reporte_top_productos(fecha_inicio: str, fecha_fin: str, limite: int = 10):
    pass

# Retorna (True, tupla_de_dicts) o (False, "mensaje")
def reporte_ventas_por_categoria(fecha_inicio: str, fecha_fin: str):
    pass

# Retorna (True, resumen) o (False, "mensaje")
def reporte_resumen_dia(fecha: str):
    pass
