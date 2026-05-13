"""Modulo generado 100% con IA | Crea y llena la base de datos de ejemplo con datos de prueba."""

from __future__ import annotations

import sqlite3
import sys
import random
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

    # Usuarios
    usuarios = [
        ("Cajero Principal", "cajerap", "cajero123", "CAJERO", 1),
        ("Cajero Dos", "cajero2", "cajero123", "CAJERO", 1),
        ("Cajero Inactivo", "cajero3", "cajero123", "CAJERO", 0),
        ("Gerente de Tienda", "gerente1", "gerente123", "ADMIN", 1),
        ("Gerente Secundario", "gerente2", "gerente123", "ADMIN", 1),
    ]
    for i in range(15):
        usuarios.append((f"Cajero Auto {i}", f"cajero_auto_{i}", "pas123", "CAJERO", random.choice([0,1])))
        
    cur.executemany(
        """
        INSERT INTO usuarios (nombre, username, password, rol, estado)
        VALUES (?, ?, ?, ?, ?)
        """,
        usuarios,
    )

    # Categorías
    categorias = [
        ("Abarrotes", "Productos básicos", 1),
        ("Bebidas", "Bebidas y refrescos", 1),
        ("Limpieza", "Productos de limpieza", 1),
        ("Lácteos", "Lácteos y derivados", 1),
        ("Dulces", "Dulces y botanas", 1),
        ("Carnes", "Carnes frías", 1),
        ("Herramientas", "Herramientas de casa", 1),
        ("Electrónica", "Cables y focos", 1),
        ("Papelería", "Cuadernos y plumas", 1),
        ("Farmacia", "Medicamentos básicos", 1),
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

    # Productos
    productos_base = [
        ("Abarrotes", "P-001", "Arroz 1kg", "Arroz extra", 28.0, 800),
        ("Abarrotes", "P-002", "Frijol 1kg", "Frijol bayo", 30.0, 600),
        ("Abarrotes", "P-003", "Azúcar 1kg", "Azúcar refinada", 25.0, 900),
        ("Abarrotes", "P-004", "Aceite 1L", "Aceite vegetal", 42.0, 450),
        ("Bebidas", "P-005", "Refresco Cola 600ml", "Cola", 15.0, 1200),
        ("Bebidas", "P-006", "Agua 1L", "Agua purificada", 12.0, 1500),
        ("Limpieza", "P-007", "Detergente 1kg", "Detergente polvo", 38.0, 400),
        ("Limpieza", "P-008", "Jabón barra", "Jabón multiusos", 10.0, 700),
        ("Lácteos", "P-009", "Leche entera 1L", "Leche pasteurizada", 26.0, 1100),
        ("Lácteos", "P-010", "Queso 250g", "Queso fresco", 10.0, 350),
        ("Dulces", "P-011", "Galletas", "Galletas surtidas", 20.0, 550),
        ("Dulces", "P-012", "Chocolate", "Chocolate barra", 10.0, 100),
    ]
    
    # Generate tons of items
    cat_names = list(categoria_id.keys())
    for i in range(13, 200):
        cat = random.choice(cat_names)
        codigo = f"P-{i:03d}"
        nombre = f"Producto Generico {i}"
        desc = f"Descripción del producto {i}"
        precio = round(random.uniform(5.0, 500.0), 2)
        stock = random.randint(500, 10000)  # High stock so we don't hit 0 in test
        productos_base.append((cat, codigo, nombre, desc, precio, stock))

    cur.executemany(
        """
        INSERT INTO productos (
            id_categoria, codigo, nombre, descripcion, precio, stock
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (
                categoria_id[p[0]], p[1], p[2], p[3], p[4], p[5],
            )
            for p in productos_base
        ],
    )

    # Clientes
    clientes = [
        ("Público General", "", "0000000000", 1),
        ("Juan Perez", "Calle Norte 10", "3322001100", 1),
        ("Maria Lopez", "Calle Sur 22", "3322001101", 1),
        ("Carlos Diaz", "Av. Centro 15", "3322001102", 1),
        ("Ana Torres", "Av. Lopez 120", "3322001103", 1),
        ("Cliente Inactivo", "", "3322001104", 0),
    ]
    for i in range(50):
        clientes.append((f"Cliente Leal {i}", f"Direccion falsa {i}", f"330000{i:04d}", random.choice([1, 1, 1, 0])))
        
    cur.executemany(
        """
        INSERT INTO clientes (nombre, direccion, telefono, estado)
        VALUES (?, ?, ?, ?)
        """,
        clientes,
    )

    # Proveedores
    proveedores = [
        ("Distribuidora Norte", "Parque Industrial", "3311002200", 1),
        ("Suministros Centro", "Col. Centro", "3311002201", 1),
        ("Lácteos del Valle", "Carretera 5", "3311002202", 1),
        ("Provee Limpio", "Av. Limpia 99", "3311002203", 1),
    ]
    for i in range(20):
        proveedores.append((f"Proveedor Mega {i}", f"Carretera local {i}", f"334400{i:04d}", 1))

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

    # Massive Sales
    user_names = list(usuario_id.keys())
    cliente_names = list(cliente_id.keys())
    prod_codes = list(producto_id.keys())

    venta_ids = []
    
    # Generate 150 sales
    for i in range(150):
        u = random.choice(user_names)
        c = random.choice(cliente_names)
        
        cur.execute(
            """
            INSERT INTO ventas (id_usuario, id_cliente, total)
            VALUES (?, ?, 0)
            """,
            (usuario_id[u], cliente_id[c]),
        )
        venta_ids.append(cur.lastrowid)

    # Set up detail for each sale
    for id_venta in venta_ids:
        num_items = random.randint(1, 10)
        selected_prods = random.sample(prod_codes, min(num_items, len(prod_codes)))
        
        total_venta = 0.0
        for pid in selected_prods:
            cantidad = random.randint(1, 8)
            
            # get current price to save in detail
            cur.execute("SELECT precio FROM productos WHERE codigo = ?", (pid,))
            precio_row = cur.fetchone()
            if not precio_row: continue
            precio = float(precio_row[0])
            
            subtotal = float(cantidad) * precio
            total_venta += subtotal
            
            cur.execute(
                """
                INSERT INTO detalle_ventas (
                    id_venta, id_producto, cantidad, precio_unitario, subtotal
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (id_venta, producto_id[pid], cantidad, precio, subtotal),
            )
            cur.execute(
                """
                UPDATE productos
                SET stock = stock - ?
                WHERE id_producto = ?
                """,
                (cantidad, producto_id[pid]),
            )
            
        cur.execute(
            "UPDATE ventas SET total = ? WHERE id_venta = ?",
            (round(total_venta, 2), id_venta),
        )

    # Some logs
    logs = []
    for _ in range(300):
        logs.append((
            random.choice(list(usuario_id.values())),
            random.choice(["CREAR", "VENTA", "REPORTE", "LOGIN", "LOGOUT"]),
            random.choice(["USUARIOS", "PRODUCTOS", "PUNTO_VENTA", "VENTAS", "SISTEMA"]),
            "Accion masiva generada"
        ))
        
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
