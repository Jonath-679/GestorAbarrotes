# 🛒 Gestor de Inventario para Tienda de Abarrotes

Aplicación de escritorio para **digitalizar y simplificar** la administración de una tienda de abarrotes o negocio pequeño.

---

## ✨ ¿Por qué este proyecto?
En muchos negocios pequeños la gestión administrativa sigue siendo manual (hojas de cuentas, ventas e inventarios).  
Este proyecto busca reemplazar esos métodos tradicionales por una solución **digital, simple, rápida y fácil de usar**.

---

## 🧰 Tecnologías
- **Python 3.12+**
- **PySide6** (GUI)
- **SQLite3** (base de datos local en archivo)
- Paradigma: **POO**
- Patrón: **MVC (Modelo / Vista / Controlador)**

---

## ✅ Requerimientos funcionales (resumen)
1) Autenticación y gestión de usuarios (admin/cajero)  
2) Gestión de productos y categorías  
3) Gestión de clientes  
4) Gestión de proveedores  
5) Proceso de venta (PuntoDeVenta)  
6) Inventario y consultas  
7) Reportes generados con excel + sistema básico de logs  
8) Restricciones por rol + validaciones

> El detalle completo está en `docs/PropuestaProyecto.pdf`.

---

## 📁 Estructura general del proyecto
```
|─ .venv/                           # Entorno virtual python
|─ .gitignore                       # Cosas que no se van a subir
|─ README.md                        # Este documento
|─ requirements.txt                 # Dependencias python
|─ docs/                            # Documentacion y archivos complementarios
|─ data/                            # Base de datos y reportes_exel
|─ src/                             # Codigo del proyecto
|  |─ main.py                       # Punto de entrada de la app
|  |─ config.py                     # Configuraciones/Rutas etc..
|  |─ models/                       # MODELO (Acceso a los datos de las entidades)
|  |─ controllers/                  # CONTROLADOR (lógica de la app)
|  |─ views/                        # VISTA (UI interfaz grafica)
|  |─ database/                     # Conexion a la base de datos
|  |─ pyqt_designer/                # Archivos de pyqt_designer
```

---

## 📦 Instalación

### 1) Clonar el repositorio
```bash
git clone https://github.com/Jonath-679/GestorAbarrotes.git
cd GestorAbarrotes
```

### 2) Crear y activar entorno virtual

**Windows (PowerShell)**
```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

**Linux / macOS (Bash)**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la aplicación 

```bash
python src/main.py
```

---

## 👥 Equipo
- Integrante 1: Jonathan Rafael Arreola Ramírez
- Integrante 2: Luis Ángel Caamal Rivera
- Integrante 3: Saul Jared Rivera Basulto
