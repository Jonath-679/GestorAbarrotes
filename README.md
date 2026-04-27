# 🛒 Gestor de Inventario para Tienda de Abarrotes

Aplicación de escritorio para **digitalizar y simplificar** la administración de una tienda de abarrotes o negocio pequeño.

---

## ✨ ¿Por qué este proyecto?
En muchos negocios pequeños la gestión administrativa sigue siendo manual (hojas de cuentas, ventas e inventarios).  
Este proyecto busca reemplazar esos métodos tradicionales por una solución **digital, simple, rápida y fácil de usar**.

---

## 🧰 Tecnologías
- **Python**
- **PyQt6/PySide6** (GUI)
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
7) Reportes + sistema básico de logs  
8) Restricciones por rol + validación de campos

> El detalle completo está en `docs/PropuestaProyecto.pdf`.

---

## 📁 Estructura general del proyecto
```
abarrotes-pos/
├─ .venv                            # Entorno virtual python
├─ .gitignore                       # Cosas que no se van a subir
├─ README.md                        # Este documento
├─ requirements.txt                 # Dependencias python
├─ docs/                            # Archivos complementarios
├─ data/                            # Base de datos
├─ src/                             # Codigo del proyecto
│  ├─ main.py                       # Punto de entrada de la app
│  ├─ config.py                     # Configuraciones/Rutas etc..
│  ├─ database/                     # Conexion a la db
│  ├─ models/                       # MODELO (clases y consultas SQL)
│  ├─ controllers/                  # CONTROLADOR (lógica de la app)
│  └─ views/                        # VISTA (UI interfaz grafica)
```

---

## 📦 Instalación

### 1) Clonar el repositorio
```bash
git clone https://github.com/Jonath-679/GestorAbarrotes.git
cd GestorAbarrotes
```

### 2) Configurar Git para evitar conflictos (LF/CRLF)
Esto ayuda a trabajar desde diferentes sistemas operativos sin problemas por saltos de línea.

```bash
git config --global core.autocrlf input
```

---

### 3) Crear y activar entorno virtual

**Windows (PowerShell)**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS (Bash)**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4) Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la aplicación 
** Esto funcionara mas adelante, ya que se defina mejor la app.

```bash
python src/main.py
```

---

## 🤝 Flujo de trabajo en Git (equipo)

### Descargar cambios antes de trabajar
```bash
git pull
```

### Guardar cambios (commit)
```bash
git status
git add .
git commit -m "Descripcion del commit, claro y conciso"
```

### Subir cambios al repositorio (push)
```bash
git push
```

---

## 🧾 Primer commit + push (si estás empezando)
Configurar Git (solo una vez):
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

---

## 👥 Equipo
- Integrante 1: Jonathan Rafael Arreola Ramírez
- Integrante 2: Luis Ángel Caamal Rivera
- Integrante 3: Saul Jared Rivera Basulto
