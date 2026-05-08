"""Modulo generado 100% con IA | Crea y llena la base de datos de ejemplo con datos de prueba."""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
	sys.path.insert(0, str(ROOT_DIR))

from config import DB_EJEMPLO_PATH, SCHEMA_PATH


def _load_schema(conn: sqlite3.Connection) -> None:
	schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
	conn.executescript(schema_sql)


def _seed_data(conn: sqlite3.Connection) -> None:
	cur = conn.cursor()

	usuarios = [
		("Admin Principal", "admin", "admin123", "ADMIN", 1),
		("Cajero Uno", "cajero1", "cajero123", "CAJERO", 1),
		("Admin Secundario", "admin2", "admin123", "ADMIN", 1),
		("Cajero Inactivo", "cajero2", "cajero123", "CAJERO", 0),
	]
	cur.executemany(
		"""
		INSERT INTO usuarios (nombre, username, password, rol, estado)
		VALUES (?, ?, ?, ?, ?)
		""",
		usuarios,
	)

	categorias = [
		("Abarrotes", "Productos basicos", 1),
		("Bebidas", "Bebidas y refrescos", 1),
		("Limpieza", "Productos de limpieza", 1),
		("Lacteos", "Lacteos y derivados", 1),
		("Dulces", "Dulces y botanas", 1),
	]
	cur.executemany(
		"""
		INSERT INTO categorias (nombre, descripcion, estado)
		VALUES (?, ?, ?)
		""",
		categorias,
	)

	cur.execute("SELECT id_categoria, nombre FROM categorias")
	categoria_id = {row[1]: row[0] for row in cur.fetchall()}

	productos = [
		("Abarrotes", "P-001", "Arroz 1kg", "Arroz extra", 28.0, 80),
		("Abarrotes", "P-002", "Frijol 1kg", "Frijol bayo", 30.0, 60),
		("Abarrotes", "P-003", "Azucar 1kg", "Azucar refinada", 25.0, 90),
		("Abarrotes", "P-004", "Aceite 1L", "Aceite vegetal", 42.0, 45),
		("Bebidas", "P-005", "Refresco Cola 600ml", "Cola", 15.0, 120),
		("Bebidas", "P-006", "Agua 1L", "Agua purificada", 12.0, 150),
		("Limpieza", "P-007", "Detergente 1kg", "Detergente polvo", 38.0, 40),
		("Limpieza", "P-008", "Jabon barra", "Jabon multiusos", 10.0, 70),
		("Lacteos", "P-009", "Leche entera 1L", "Leche pasteurizada", 26.0, 110),
		("Lacteos", "P-010", "Queso 250g", "Queso fresco", 10.0, 35),
		("Dulces", "P-011", "Galletas", "Galletas surtidas", 20.0, 55),
		("Dulces", "P-012", "Chocolate", "Chocolate barra", 10.0, 0),
	]
	cur.executemany(
		"""
		INSERT INTO productos (
			id_categoria, codigo, nombre, descripcion, precio, stock
		)
		VALUES (?, ?, ?, ?, ?, ?)
		""",
		[
			(
				categoria_id[p[0]],
				p[1],
				p[2],
				p[3],
				p[4],
				p[5],
			)
			for p in productos
		],
	)

	clientes = [
		("Publico General", "", "0000000000", 1),
		("Juan Perez", "Calle Norte 10", "3322001100", 1),
		("Maria Lopez", "Calle Sur 22", "3322001101", 1),
		("Carlos Diaz", "Av. Centro 15", "3322001102", 1),
		("Ana Torres", "Av. Lopez 120", "3322001103", 1),
		("Cliente Inactivo", "", "3322001104", 0),
	]
	cur.executemany(
		"""
		INSERT INTO clientes (nombre, direccion, telefono, estado)
		VALUES (?, ?, ?, ?)
		""",
		clientes,
	)

	proveedores = [
		("Distribuidora Norte", "Parque Industrial", "3311002200", 1),
		("Suministros Centro", "Col. Centro", "3311002201", 1),
		("Lacteos del Valle", "Carretera 5", "3311002202", 1),
		("Provee Limpio", "Av. Limpia 99", "3311002203", 1),
	]
	cur.executemany(
		"""
		INSERT INTO proveedores (nombre, direccion, telefono, estado)
		VALUES (?, ?, ?, ?)
		""",
		proveedores,
	)

	cur.execute("SELECT id_usuario, username FROM usuarios")
	usuario_id = {row[1]: row[0] for row in cur.fetchall()}
	cur.execute("SELECT id_cliente, nombre FROM clientes")
	cliente_id = {row[1]: row[0] for row in cur.fetchall()}
	cur.execute("SELECT id_producto, codigo FROM productos")
	producto_id = {row[1]: row[0] for row in cur.fetchall()}

	ventas_base = [
		("admin", "Juan Perez"),
		("cajero1", "Maria Lopez"),
		("cajero1", "Publico General"),
		("admin", "Carlos Diaz"),
		("cajero1", "Ana Torres"),
	]

	venta_ids: List[int] = []
	for username, cliente in ventas_base:
		cur.execute(
			"""
			INSERT INTO ventas (id_usuario, id_cliente, total)
			VALUES (?, ?, 0)
			""",
			(usuario_id[username], cliente_id[cliente]),
		)
		last_id = cur.lastrowid
		if last_id is None:
			raise RuntimeError("No se pudo obtener id_venta insertado.")
		venta_ids.append(last_id)

	detalles: Dict[int, List[Tuple[str, int, float]]] = {
		venta_ids[0]: [
			("P-001", 2, 28.0),
			("P-005", 3, 15.0),
		],
		venta_ids[1]: [
			("P-009", 2, 26.0),
			("P-011", 1, 20.0),
		],
		venta_ids[2]: [
			("P-002", 1, 30.0),
			("P-006", 2, 12.0),
		],
		venta_ids[3]: [
			("P-003", 1, 25.0),
			("P-004", 1, 42.0),
			("P-007", 1, 38.0),
		],
		venta_ids[4]: [
			("P-005", 2, 15.0),
			("P-008", 3, 10.0),
		],
	}

	total_por_venta: Dict[int, float] = {vid: 0.0 for vid in venta_ids}
	for id_venta, items in detalles.items():
		for codigo, cantidad, precio in items:
			subtotal = float(cantidad) * float(precio)
			total_por_venta[id_venta] += subtotal
			cur.execute(
				"""
				INSERT INTO detalle_ventas (
					id_venta, id_producto, cantidad, precio_unitario, subtotal
				)
				VALUES (?, ?, ?, ?, ?)
				""",
				(id_venta, producto_id[codigo], cantidad, precio, subtotal),
			)
			cur.execute(
				"""
				UPDATE productos
				SET stock = stock - ?
				WHERE id_producto = ?
				""",
				(cantidad, producto_id[codigo]),
			)

	for id_venta, total in total_por_venta.items():
		cur.execute(
			"UPDATE ventas SET total = ? WHERE id_venta = ?",
			(round(total, 2), id_venta),
		)

	logs = [
		(usuario_id["admin"], "CREAR", "USUARIOS", "Alta de usuario cajero1"),
		(usuario_id["admin"], "CREAR", "PRODUCTOS", "Carga inicial de productos"),
		(usuario_id["cajero1"], "VENTA", "PUNTO_VENTA", "Venta registrada"),
		(usuario_id["admin"], "REPORTE", "VENTAS", "Consulta de ventas"),
	]
	cur.executemany(
		"""
		INSERT INTO logs (id_usuario, accion, modulo, descripcion)
		VALUES (?, ?, ?, ?)
		""",
		logs,
	)


def create_example_db(reset: bool = True) -> None:
	if reset and DB_EJEMPLO_PATH.exists():
		DB_EJEMPLO_PATH.unlink()

	conn = sqlite3.connect(DB_EJEMPLO_PATH)
	conn.execute("PRAGMA foreign_keys = ON;")
	try:
		_load_schema(conn)
		_seed_data(conn)
		conn.commit()
	finally:
		conn.close()


if __name__ == "__main__":
	create_example_db()
