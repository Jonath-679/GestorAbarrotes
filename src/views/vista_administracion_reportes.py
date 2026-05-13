from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QLabel, QFrame, QHBoxLayout, QPushButton, QTableWidget, QHeaderView
from PySide6.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form: QWidget):
        Form.setObjectName("VistaAdmin")
        
        self.main_layout = QVBoxLayout(Form)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #333; background: #1e1e1e; border-radius: 4px; }
            QTabBar::tab { background: #252526; color: #a0a0a0; padding: 10px 20px; border-top-left-radius: 4px; border-top-right-radius: 4px; margin-right: 2px; }
            QTabBar::tab:selected { background: #1e1e1e; color: #ffffff; border-bottom: 2px solid #007acc; }
            QTabBar::tab:hover:!selected { background: #2d2d2d; }
        """)
        
        # --- TAB: INVENTARIO (Productos) ---
        self.tab_inventario = QWidget()
        self.layout_inv = QVBoxLayout(self.tab_inventario)
        self.header_inv = QHBoxLayout()
        
        self.btn_actualizar_inv = QPushButton("🔄 Actualizar")
        self.btn_actualizar_inv.setMinimumHeight(35)
        self.header_inv.addWidget(self.btn_actualizar_inv)
        
        self.btn_nuevo_producto = QPushButton("➕ Nuevo Producto")
        self.btn_nuevo_producto.setMinimumHeight(35)
        self.header_inv.addWidget(self.btn_nuevo_producto)
        
        self.header_inv.addStretch()
        self.layout_inv.addLayout(self.header_inv)
        
        self.tabla_productos = QTableWidget(0, 6)
        self.tabla_productos.setHorizontalHeaderLabels(["Código", "Nombre", "Precio Compra", "Precio Venta", "Stock", "Categoría"])
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_productos.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_productos.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layout_inv.addWidget(self.tabla_productos)
        self.tab_widget.addTab(self.tab_inventario, "📦 Inventario")
        
        # --- TAB: CATEGORÍAS ---
        self.tab_categorias = QWidget()
        self.layout_cat = QVBoxLayout(self.tab_categorias)
        self.header_cat = QHBoxLayout()
        
        self.btn_actualizar_cat = QPushButton("🔄 Actualizar")
        self.btn_actualizar_cat.setMinimumHeight(35)
        self.header_cat.addWidget(self.btn_actualizar_cat)
        
        self.btn_nueva_categoria = QPushButton("➕ Nueva Categoría")
        self.btn_nueva_categoria.setMinimumHeight(35)
        self.header_cat.addWidget(self.btn_nueva_categoria)
        
        self.header_cat.addStretch()
        self.layout_cat.addLayout(self.header_cat)
        
        self.tabla_categorias = QTableWidget(0, 3)
        self.tabla_categorias.setHorizontalHeaderLabels(["ID", "Nombre", "Estado"])
        self.tabla_categorias.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_categorias.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_categorias.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layout_cat.addWidget(self.tabla_categorias)
        self.tab_widget.addTab(self.tab_categorias, "🏷️ Categorías")
        
        # --- TAB: EMPLEADOS ---
        self.tab_empleados = QWidget()
        self.layout_emp = QVBoxLayout(self.tab_empleados)
        self.header_emp = QHBoxLayout()
        
        self.btn_actualizar_emp = QPushButton("🔄 Actualizar")
        self.btn_actualizar_emp.setMinimumHeight(35)
        self.header_emp.addWidget(self.btn_actualizar_emp)
        
        self.btn_nuevo_empleado = QPushButton("➕ Nuevo Empleado")
        self.btn_nuevo_empleado.setMinimumHeight(35)
        self.header_emp.addWidget(self.btn_nuevo_empleado)
        
        self.header_emp.addStretch()
        self.layout_emp.addLayout(self.header_emp)
        
        self.tabla_empleados = QTableWidget(0, 5)
        self.tabla_empleados.setHorizontalHeaderLabels(["ID", "Nombre", "Usuario", "Rol", "Estado"])
        self.tabla_empleados.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_empleados.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_empleados.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layout_emp.addWidget(self.tabla_empleados)
        self.tab_widget.addTab(self.tab_empleados, "🧑‍💼 Empleados")
        
        # --- TAB: PROVEEDORES ---
        self.tab_proveedores = QWidget()
        self.layout_prov = QVBoxLayout(self.tab_proveedores)
        self.header_prov = QHBoxLayout()
        
        self.btn_actualizar_prov = QPushButton("🔄 Actualizar")
        self.btn_actualizar_prov.setMinimumHeight(35)
        self.header_prov.addWidget(self.btn_actualizar_prov)
        
        self.btn_nuevo_proveedor = QPushButton("➕ Nuevo Proveedor")
        self.btn_nuevo_proveedor.setMinimumHeight(35)
        self.header_prov.addWidget(self.btn_nuevo_proveedor)
        
        self.header_prov.addStretch()
        self.layout_prov.addLayout(self.header_prov)
        
        self.tabla_proveedores = QTableWidget(0, 4)
        self.tabla_proveedores.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email"])
        self.tabla_proveedores.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_proveedores.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_proveedores.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layout_prov.addWidget(self.tabla_proveedores)
        self.tab_widget.addTab(self.tab_proveedores, "🏢 Proveedores")

        # --- TAB: REPORTES / HISTORIAL ---
        self.tab_reportes = QWidget()
        self.layout_rep = QVBoxLayout(self.tab_reportes)
        
        self.header_rep = QHBoxLayout()
        self.label_historial = QLabel("Historial de Ventas Recientes")
        self.label_historial.setProperty("class", "Subtitle")
        self.header_rep.addWidget(self.label_historial)
        self.header_rep.addStretch()
        
        self.btn_actualizar_rep = QPushButton("🔄 Actualizar")
        self.btn_actualizar_rep.setMinimumHeight(35)
        self.header_rep.addWidget(self.btn_actualizar_rep)
        
        self.layout_rep.addLayout(self.header_rep)
        
        self.tabla_historial_ventas = QTableWidget(0, 6)
        self.tabla_historial_ventas.setHorizontalHeaderLabels(["ID Venta", "Fecha", "Total", "Cajero", "Cliente", "Productos"])
        self.tabla_historial_ventas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_historial_ventas.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_historial_ventas.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layout_rep.addWidget(self.tabla_historial_ventas)
        
        self.label_rep = QLabel("Exportar Reportes (Excel)")
        self.label_rep.setProperty("class", "Subtitle")
        self.layout_rep.addWidget(self.label_rep)
        
        self.grid_rep = QHBoxLayout()
        self.grid_rep.setSpacing(10)
        self.btn_rep_ventas = QPushButton("📊 Ventas")
        self.grid_rep.addWidget(self.btn_rep_ventas)
        self.btn_rep_inventario = QPushButton("📋 Inventario")
        self.grid_rep.addWidget(self.btn_rep_inventario)
        self.btn_rep_clientes = QPushButton("👥 Clientes")
        self.grid_rep.addWidget(self.btn_rep_clientes)
        self.btn_rep_empleados = QPushButton("👔 Empleados")
        self.grid_rep.addWidget(self.btn_rep_empleados)
        self.btn_rep_logs = QPushButton("📝 Logs")
        self.grid_rep.addWidget(self.btn_rep_logs)
        
        self.layout_rep.addLayout(self.grid_rep)
        
        # Opciones Avanzadas
        self.label_sistema = QLabel("Opciones de Sistema")
        self.label_sistema.setProperty("class", "Subtitle")
        self.layout_rep.addWidget(self.label_sistema)
        
        self.btn_toggle_db = QPushButton("🔄 Cambiar Base de Datos (Actual: Ejemplo)")
        self.btn_toggle_db.setProperty("class", "DangerButton")
        self.layout_rep.addWidget(self.btn_toggle_db)
        
        self.tab_widget.addTab(self.tab_reportes, "📈 Reportes e Historial")

        self.main_layout.addWidget(self.tab_widget)
