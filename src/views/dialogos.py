from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QFormLayout
from PySide6.QtCore import Qt

class BaseDialog(QDialog):
    def __init__(self, titulo: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.setMinimumWidth(350)
        self.setModal(True)
        # Quitar boton de ayuda nativo
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)
        
        self.main_layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()
        self.form_layout.setSpacing(10)
        self.main_layout.addLayout(self.form_layout)
        
        # Botones inferiores
        self.buttons_layout = QHBoxLayout()
        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.setProperty("class", "SuccessButton")
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.setProperty("class", "DangerButton")
        
        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_guardar.clicked.connect(self.accept)
        
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.btn_cancelar)
        self.buttons_layout.addWidget(self.btn_guardar)
        self.main_layout.addLayout(self.buttons_layout)

    def required_label(self, text: str) -> QLabel:
        """Devuelve un QLabel estilizado indicando que es obligatorio."""
        lbl = QLabel(f"{text} <span style='color:red;'>*</span>")
        return lbl

class DialogCategoria(BaseDialog):
    def __init__(self, parent=None):
        super().__init__("Nueva Categoría", parent)
        self.line_nombre = QLineEdit()
        self.line_nombre.setPlaceholderText("Nombre de la categoría")
        self.line_desc = QLineEdit()
        self.form_layout.addRow(self.required_label("Nombre"), self.line_nombre)
        self.form_layout.addRow(QLabel("Descripción"), self.line_desc)

class DialogProducto(BaseDialog):
    def __init__(self, categorias: list, parent=None):
        super().__init__("Nuevo Producto", parent)
        self.line_codigo = QLineEdit()
        self.line_nombre = QLineEdit()
        self.line_precio = QLineEdit()
        self.line_stock = QLineEdit()
        self.line_desc = QLineEdit()
        
        self.combo_categoria = QComboBox()
        for cat in categorias:
            self.combo_categoria.addItem(cat["nombre"], userData=cat["id_categoria"])
            
        self.form_layout.addRow(self.required_label("Código"), self.line_codigo)
        self.form_layout.addRow(self.required_label("Nombre"), self.line_nombre)
        self.form_layout.addRow(self.required_label("Categoría"), self.combo_categoria)
        self.form_layout.addRow(self.required_label("Precio"), self.line_precio)
        self.form_layout.addRow(self.required_label("Stock Inicial"), self.line_stock)
        self.form_layout.addRow(QLabel("Descripción"), self.line_desc)

class DialogEmpleado(BaseDialog):
    def __init__(self, parent=None):
        super().__init__("Nuevo Empleado", parent)
        self.line_nombre = QLineEdit()
        self.line_username = QLineEdit()
        self.line_password = QLineEdit()
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.combo_rol = QComboBox()
        self.combo_rol.addItems(["CAJERO", "ADMIN"])
        
        self.form_layout.addRow(self.required_label("Nombre"), self.line_nombre)
        self.form_layout.addRow(self.required_label("Nombre de Usuario"), self.line_username)
        self.form_layout.addRow(self.required_label("Contraseña"), self.line_password)
        self.form_layout.addRow(self.required_label("Rol"), self.combo_rol)

class DialogCliente(BaseDialog):
    def __init__(self, parent=None):
        super().__init__("Nuevo Cliente", parent)
        self.line_nombre = QLineEdit()
        self.line_telefono = QLineEdit()
        self.line_direccion = QLineEdit()
        
        self.form_layout.addRow(self.required_label("Nombre Completo"), self.line_nombre)
        self.form_layout.addRow(self.required_label("Teléfono"), self.line_telefono)
        self.form_layout.addRow(QLabel("Dirección"), self.line_direccion)

class DialogProveedor(BaseDialog):
    def __init__(self, parent=None):
        super().__init__("Nuevo Proveedor", parent)
        self.line_nombre = QLineEdit()
        self.line_telefono = QLineEdit()
        self.line_direccion = QLineEdit()
        
        self.form_layout.addRow(self.required_label("Nombre"), self.line_nombre)
        self.form_layout.addRow(self.required_label("Teléfono"), self.line_telefono)
        self.form_layout.addRow(QLabel("Dirección"), self.line_direccion)
