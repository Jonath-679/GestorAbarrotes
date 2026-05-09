from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence, cast
from openpyxl import Workbook

from src.config import REPORTS_DIR

from src.database.connection import get_connection
from src.models.cliente_model import buscar_cliente
from src.models.producto_model import buscar_producto
from src.models.usuario_model import buscar_usuarios
from src.models.venta_model import listar_ventas

def _write_excel(headers: list[str], rows: Sequence[Mapping[str, Any]], file_path: Path) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    if ws is None:
        ws = wb.create_sheet()
    ws.append(["Fecha de creacion", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    ws.append(["Generado por", "App de abarrotes"])
    ws.append([])
    ws.append(headers)
    for row in rows:
        values = []
        for header in headers:
            value = row.get(header)
            if header == "estado":
                if value == 1:
                    value = "Activado"
                elif value == 0:
                    value = "Desactivado"
            if header == "rol" and isinstance(value, str):
                if value.upper() == "ADMIN":
                    value = "Administrador"
                elif value.upper() == "CAJERO":
                    value = "Cajero"
            values.append(value)
        ws.append(values)
    wb.save(file_path)

def reporte_inventario():
    """
    Genera un reporte de inventario (productos)

    Returns:
        Si todo sale bien: (True, ruta_archivo)
        Si algo falla: (False, "mensaje")
    """
    try:
        status, productos = buscar_producto("")
        if not status:
            return (False, productos)
        headers = [
            "id_producto",
            "codigo",
            "nombre",
            "id_categoria",
            "descripcion",
            "precio",
            "stock",
        ]
        file_path = REPORTS_DIR / "reporte_inventario.xlsx"
        productos_rows = cast(Sequence[Mapping[str, Any]], productos)
        _write_excel(headers, productos_rows, file_path)
        return (True, str(file_path))
    except Exception as e:
        return (False, f"Error: {e}")

def reporte_clientes():
    """
    Genera un reporte de clientes

    Returns:
        Si todo sale bien: (True, ruta_archivo)
        Si algo falla: (False, "mensaje")
    """
    try:
        status, clientes = buscar_cliente("")
        if not status:
            return (False, clientes)
        headers = [
            "id_cliente",
            "nombre",
            "telefono",
            "direccion",
            "estado",
        ]
        file_path = REPORTS_DIR / "reporte_clientes.xlsx"
        clientes_rows = cast(Sequence[Mapping[str, Any]], clientes)
        _write_excel(headers, clientes_rows, file_path)
        return (True, str(file_path))
    except Exception as e:
        return (False, f"Error: {e}")

def reporte_usuarios():
    """
    Genera un reporte de usuarios

    Returns:
        Si todo sale bien: (True, ruta_archivo)
        Si algo falla: (False, "mensaje")
    """
    try:
        status, usuarios = buscar_usuarios("")
        if not status:
            return (False, usuarios)
        headers = [
            "id_usuario",
            "nombre",
            "username",
            "rol",
            "estado",
        ]
        file_path = REPORTS_DIR / "reporte_usuarios.xlsx"
        usuarios_rows = cast(Sequence[Mapping[str, Any]], usuarios)
        _write_excel(headers, usuarios_rows, file_path)
        return (True, str(file_path))
    except Exception as e:
        return (False, f"Error: {e}")

def reporte_ventas():
    """
    Genera un reporte de ventas con detalles y datos de cliente/usuario

    Returns:
        Si todo sale bien: (True, ruta_archivo)
        Si algo falla: (False, "mensaje")
    """
    try:
        status, ventas = listar_ventas()
        if not status:
            return (False, ventas)

        status, clientes = buscar_cliente("")
        if not status:
            return (False, clientes)

        status, usuarios = buscar_usuarios("")
        if not status:
            return (False, usuarios)

        ventas_rows = cast(Sequence[Mapping[str, Any]], ventas)
        clientes_rows = cast(Sequence[Mapping[str, Any]], clientes)
        usuarios_rows = cast(Sequence[Mapping[str, Any]], usuarios)

        clientes_por_id = {c.get("id_cliente"): c.get("nombre") for c in clientes_rows}
        usuarios_por_id = {u.get("id_usuario"): u.get("nombre") for u in usuarios_rows}

        headers = [
            "id_venta",
            "fecha_hora",
            "total",
            "id_usuario",
            "usuario",
            "id_cliente",
            "cliente",
            "id_producto",
            "codigo_producto",
            "nombre_producto",
            "cantidad",
            "precio_unitario",
            "subtotal",
        ]

        conexion = get_connection()
        cursor = conexion.cursor()
        rows: list[dict] = []

        for venta in ventas_rows:
            id_venta = venta.get("id_venta")
            cursor.execute(
                """
                SELECT
                    dv.id_producto,
                    p.codigo AS codigo_producto,
                    p.nombre AS nombre_producto,
                    dv.cantidad,
                    dv.precio_unitario,
                    dv.subtotal
                FROM detalle_ventas dv
                JOIN productos p ON p.id_producto = dv.id_producto
                WHERE dv.id_venta = ?
                """,
                (id_venta,),
            )
            detalles = cursor.fetchall()
            if not detalles:
                rows.append(
                    {
                        "id_venta": id_venta,
                        "fecha_hora": venta.get("fecha_hora"),
                        "total": venta.get("total"),
                        "id_usuario": venta.get("id_usuario"),
                        "usuario": usuarios_por_id.get(venta.get("id_usuario")),
                        "id_cliente": venta.get("id_cliente"),
                        "cliente": clientes_por_id.get(venta.get("id_cliente")),
                        "id_producto": None,
                        "codigo_producto": None,
                        "nombre_producto": None,
                        "cantidad": None,
                        "precio_unitario": None,
                        "subtotal": None,
                    }
                )
                continue

            for detalle in detalles:
                rows.append(
                    {
                        "id_venta": id_venta,
                        "fecha_hora": venta.get("fecha_hora"),
                        "total": venta.get("total"),
                        "id_usuario": venta.get("id_usuario"),
                        "usuario": usuarios_por_id.get(venta.get("id_usuario")),
                        "id_cliente": venta.get("id_cliente"),
                        "cliente": clientes_por_id.get(venta.get("id_cliente")),
                        "id_producto": detalle["id_producto"],
                        "codigo_producto": detalle["codigo_producto"],
                        "nombre_producto": detalle["nombre_producto"],
                        "cantidad": detalle["cantidad"],
                        "precio_unitario": detalle["precio_unitario"],
                        "subtotal": detalle["subtotal"],
                    }
                )

        file_path = REPORTS_DIR / "reporte_ventas.xlsx"
        _write_excel(headers, rows, file_path)
        return (True, str(file_path))
    except Exception as e:
        return (False, f"Error: {e}")

def reporte_logs():
    pass

######################### PRUEVAS #########################

if __name__ == "__main__":
    reporte_inventario()
    reporte_clientes()
    reporte_usuarios()
    reporte_ventas()
