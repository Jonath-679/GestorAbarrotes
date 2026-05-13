from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form: QWidget):
        Form.setObjectName("LoginForm")
        Form.resize(500, 400)
        Form.setMinimumSize(400, 350)
        
        self.main_layout = QVBoxLayout(Form)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.card = QWidget(Form)
        self.card.setMinimumWidth(350)
        self.card.setMaximumWidth(400)
        self.card.setStyleSheet("background-color: #252526; border-radius: 8px;")
        
        self.card_layout = QVBoxLayout(self.card)
        self.card_layout.setContentsMargins(40, 40, 40, 40)
        self.card_layout.setSpacing(20)
        
        self.label_titulo = QLabel("Inicio de Sesión")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setProperty("class", "Title")
        self.label_titulo.setStyleSheet("background: transparent;")
        self.card_layout.addWidget(self.label_titulo)
        
        self.layout_user = QVBoxLayout()
        self.layout_user.setSpacing(5)
        self.label_usuario_login = QLabel("Usuario")
        self.label_usuario_login.setStyleSheet("background: transparent;")
        self.line_usuario_login = QLineEdit()
        self.line_usuario_login.setPlaceholderText("Ingresa tu username")
        self.layout_user.addWidget(self.label_usuario_login)
        self.layout_user.addWidget(self.line_usuario_login)
        self.card_layout.addLayout(self.layout_user)
        
        self.layout_pass = QVBoxLayout()
        self.layout_pass.setSpacing(5)
        self.label_contrasea_login = QLabel("Contraseña")
        self.label_contrasea_login.setStyleSheet("background: transparent;")
        
        self.layout_pass_input = QHBoxLayout()
        self.layout_pass_input.setSpacing(5)
        self.line_contrasea_login = QLineEdit()
        self.line_contrasea_login.setPlaceholderText("Ingresa tu contraseña")
        self.line_contrasea_login.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.btn_toggle_pwd = QPushButton("👁️")
        self.btn_toggle_pwd.setFixedSize(35, 30)
        self.btn_toggle_pwd.setStyleSheet("background: #444444; border-radius: 4px; font-size: 14px;")
        self.btn_toggle_pwd.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.layout_pass_input.addWidget(self.line_contrasea_login)
        self.layout_pass_input.addWidget(self.btn_toggle_pwd)
        
        self.layout_pass.addWidget(self.label_contrasea_login)
        self.layout_pass.addLayout(self.layout_pass_input)
        self.card_layout.addLayout(self.layout_pass)
        
        self.card_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        self.btn_ingresar = QPushButton("Ingresar")
        self.btn_ingresar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_ingresar.setStyleSheet("""
            QPushButton {
                background-color: #007acc; 
                color: white; 
                border-radius: 4px; 
                padding: 10px; 
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0098ff;
            }
        """)
        self.card_layout.addWidget(self.btn_ingresar)
        
        self.main_layout.addWidget(self.card)
