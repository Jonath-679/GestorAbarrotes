from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QFrame
from PySide6.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form: QWidget):
        Form.setObjectName("VistaClientes")
        
        self.main_layout = QVBoxLayout(Form)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # --- Barra superior ---
        self.top_bar = QHBoxLayout()
        self.top_bar.setSpacing(10)
        
        self.line_buscar = QLineEdit()
        self.line_buscar.setPlaceholderText("🔍 Buscar cliente por nombre o teléfono...")
        self.line_buscar.setMinimumHeight(35)
        self.top_bar.addWidget(self.line_buscar)
        
        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.setMinimumHeight(35)
        self.top_bar.addWidget(self.btn_buscar)
        
        self.top_bar.addStretch()
        
        self.btn_actualizar = QPushButton("🔄 Actualizar")
        self.btn_actualizar.setMinimumHeight(35)
        self.btn_actualizar.setStyleSheet("text-align: center; padding: 0 15px;")
        self.top_bar.addWidget(self.btn_actualizar)
        
        self.top_bar.addStretch()
        
        self.btn_registrar = QPushButton("➕ Nuevo Cliente")
        self.btn_registrar.setStyleSheet("background-color: #007acc;")
        self.btn_registrar.setMinimumHeight(35)
        self.top_bar.addWidget(self.btn_registrar)
        
        self.main_layout.addLayout(self.top_bar)
        
        # --- Tabla de Clientes ---
        self.tabla_clientes = QTableWidget(0, 5)
        self.tabla_clientes.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Correo", "Acciones"])
        self.tabla_clientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_clientes.verticalHeader().setVisible(False)
        self.tabla_clientes.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_clientes.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.main_layout.addWidget(self.tabla_clientes)
