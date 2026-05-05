PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario  INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre      TEXT NOT NULL,
  username    TEXT NOT NULL UNIQUE,
  password    TEXT NOT NULL,
  rol         TEXT NOT NULL CHECK (rol IN ('ADMIN', 'CAJERO')),
  estado      INTEGER NOT NULL DEFAULT 1 CHECK (estado IN (0, 1))
);

CREATE TABLE IF NOT EXISTS logs (
  id_log      INTEGER PRIMARY KEY AUTOINCREMENT,
  id_usuario  INTEGER NOT NULL,
  accion      TEXT NOT NULL,
  modulo      TEXT,
  descripcion TEXT,
  fecha_hora  TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS categorias (
  id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre       TEXT NOT NULL UNIQUE,
  descripcion  TEXT,
  estado       INTEGER NOT NULL DEFAULT 1 CHECK (estado IN (0, 1))
);

CREATE TABLE IF NOT EXISTS productos (
  id_producto   INTEGER PRIMARY KEY AUTOINCREMENT,
  id_categoria  INTEGER NOT NULL,
  codigo        TEXT NOT NULL UNIQUE,
  nombre        TEXT NOT NULL,
  descripcion   TEXT,
  stock         INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
  stock_minimo  INTEGER NOT NULL DEFAULT 0 CHECK (stock_minimo >= 0),
  estado        INTEGER NOT NULL DEFAULT 1 CHECK (estado IN (0, 1)),
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS clientes (
  id_cliente  INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre      TEXT NOT NULL,
  direccion   TEXT,
  telefono    TEXT,
  estado      INTEGER NOT NULL DEFAULT 1 CHECK (estado IN (0, 1))
);

CREATE TABLE IF NOT EXISTS proveedores (
  id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre       TEXT NOT NULL,
  direccion    TEXT,
  telefono     TEXT,
  estado       INTEGER NOT NULL DEFAULT 1 CHECK (estado IN (0, 1))
);

CREATE TABLE IF NOT EXISTS ventas (
  id_venta    INTEGER PRIMARY KEY AUTOINCREMENT,
  id_usuario  INTEGER NOT NULL,
  id_cliente  INTEGER,
  fecha_hora  TEXT NOT NULL DEFAULT (datetime('now')),
  total       REAL NOT NULL DEFAULT 0 CHECK (total >= 0),
  estado      INTEGER NOT NULL DEFAULT 1 CHECK (estado IN (0, 1)),
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
    ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS detalle_ventas (
  id_detalle_ventas INTEGER PRIMARY KEY AUTOINCREMENT,
  id_venta          INTEGER NOT NULL,
  id_producto       INTEGER NOT NULL,
  cantidad          INTEGER NOT NULL CHECK (cantidad > 0),
  precio_unitario   REAL NOT NULL CHECK (precio_unitario >= 0),
  subtotal          REAL NOT NULL CHECK (subtotal >= 0),
  FOREIGN KEY (id_venta) REFERENCES ventas(id_venta)
    ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_logs_id_usuario ON logs(id_usuario);
CREATE INDEX IF NOT EXISTS idx_ventas_fecha_hora ON ventas(fecha_hora);
CREATE INDEX IF NOT EXISTS idx_detalle_ventas_id_venta ON detalle_ventas(id_venta);
