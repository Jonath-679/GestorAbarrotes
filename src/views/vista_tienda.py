from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QFrame, QSizePolicy
from PySide6.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form: QWidget):
        Form.setObjectName("VistaTienda")
        
        # Layout principal
        self.main_layout = QVBoxLayout(Form)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # --- Barra superior (Búsqueda y Acciones) ---
        self.top_bar = QHBoxLayout()
        self.top_bar.setSpacing(10)
        
        self.line_buscar_producto = QLineEdit()
        self.line_buscar_producto.setPlaceholderText("🔍 Buscar producto por código o nombre...")
        self.line_buscar_producto.setMinimumHeight(35)
        self.top_bar.addWidget(self.line_buscar_producto)
        
        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.setMinimumHeight(35)
        self.top_bar.addWidget(self.btn_buscar)
        
        self.btn_agregar = QPushButton("Añadir al Carrito")
        self.btn_agregar.setProperty("class", "DangerButton") # Solo diferente color
        self.btn_agregar.setStyleSheet("background-color: #2b6a43;") # Verde success
        self.btn_agregar.setMinimumHeight(35)
        self.top_bar.addWidget(self.btn_agregar)
        
        self.main_layout.addLayout(self.top_bar)
        
        # --- Tabla del Carrito ---
        self.tabla_carrito = QTableWidget(0, 5)
        self.tabla_carrito.setHorizontalHeaderLabels(["Código", "Producto", "Cant.", "Precio Unit.", "Subtotal"])
        self.tabla_carrito.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_carrito.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        self.tabla_carrito.verticalHeader().setVisible(False)
        self.tabla_carrito.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_carrito.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla_carrito.setStyleSheet("background-color: #1e1e1e; border: 1px solid #333333; gridline-color: #333333;")
        self.main_layout.addWidget(self.tabla_carrito)
        
        # --- Panel inferior (Totales y Cobro) ---
        self.bottom_panel = QFrame()
        self.bottom_panel.setProperty("class", "HeaderFrame")
        self.bottom_panel.setStyleSheet("background-color: #252526; border-radius: 8px;")
        self.bottom_layout = QHBoxLayout(self.bottom_panel)
        self.bottom_layout.setContentsMargins(20, 15, 20, 15)
        
        self.btn_eliminar_item = QPushButton("🗑️ Quitar Item")
        self.btn_eliminar_item.setProperty("class", "DangerButton")
        self.btn_eliminar_item.setMinimumWidth(120)
        self.btn_eliminar_item.setMinimumHeight(40)
        self.bottom_layout.addWidget(self.btn_eliminar_item)
        
        self.btn_cancelar_venta = QPushButton("❌ Cancelar Venta")
        self.btn_cancelar_venta.setProperty("class", "DangerButton")
        self.btn_cancelar_venta.setMinimumWidth(140)
        self.btn_cancelar_venta.setMinimumHeight(40)
        self.bottom_layout.addWidget(self.btn_cancelar_venta)
        
        self.bottom_layout.addStretch()
        
        self.label_total_texto = QLabel("TOTAL:")
        self.label_total_texto.setStyleSheet("color: #a0a0a0; font-size: 18px; font-weight: bold;")
        self.bottom_layout.addWidget(self.label_total_texto)
        
        self.label_total_valor = QLabel("$ 0.00")
        self.label_total_valor.setStyleSheet("color: #4ade80; font-size: 24px; font-weight: bold;")
        self.bottom_layout.addWidget(self.label_total_valor)
        
        self.bottom_layout.addSpacing(20)
        
        self.btn_cobrar = QPushButton("💵 COBRAR")
        self.btn_cobrar.setStyleSheet("""
            QPushButton {
                background-color: #166534; 
                color: white; 
                font-size: 14px; 
                font-weight: bold; 
                border-radius: 4px;
            }
            QPushButton:hover { background-color: #1c7a40; }
        """)
        self.btn_cobrar.setMinimumWidth(120)
        self.btn_cobrar.setMinimumHeight(40)
        self.bottom_layout.addWidget(self.btn_cobrar)
        
        self.main_layout.addWidget(self.bottom_panel)
