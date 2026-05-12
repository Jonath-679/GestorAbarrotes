from PySide6 import QtWidgets
from views.vistan_login import Ui_Form as Ui_Login
from models.usuario_model import validar_inicio_sesion, validar_usuario, registrar_usuario, buscar_usuarios

class LoginController:
    def __init__(self, main_controller):
        """
        Inicializa el controlador de login. Recibe referencias al MainController para interactuar con él.
        """
        self.main_controller = main_controller  # Para mostrar la ventana principal al triunfar
        self.main_controller.login_controller = self # Inyectarse a main_controller para que pueda cerrar sesion
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle("Inicio de Sesión")

        self.ensure_default_admin()
        self.connect_signals()

    def show(self):
        self.window.show()

    def connect_signals(self):
        """Conecta eventos como enter o botones (si hubieran sido añadidos en el .ui).
        Puesto que vistan_login.ui parece no tener un QPushButton generado directamente 
        para Login, usamos el trigger del LineEdit (enter) para intentar acceder.
        """
        self.ui.line_contrasea_login.returnPressed.connect(self.attempt_login)
        self.ui.line_usuario_login.returnPressed.connect(self.attempt_login)
        self.ui.btn_ingresar.clicked.connect(self.attempt_login)
        self.ui.btn_toggle_pwd.clicked.connect(self.toggle_password_visibility)

    def toggle_password_visibility(self):
        if self.ui.line_contrasea_login.echoMode() == QtWidgets.QLineEdit.EchoMode.Password:
            self.ui.line_contrasea_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.ui.line_contrasea_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
    def ensure_default_admin(self):
        """Crea un usuario administrador por defecto si no existe."""
        status_val, exists = validar_usuario("admin")
        if status_val and not exists:
            datos_admin = {
                "nombre": "Administrador",
                "username": "admin",
                "password": "contraseña",
                "rol": "ADMIN",
                "estado": 1
            }
            registrar_usuario(datos_admin)

    def attempt_login(self):
        """Lógica para intentar loguearse y transicionar al main app si es exitoso."""
        username = self.ui.line_usuario_login.text().strip()
        password = self.ui.line_contrasea_login.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self.window, "Campos Vacíos", "Ingrese ambos campos.")
            return

        status, correct = validar_inicio_sesion(username, password)
        
        if not status:
            # Significa que 'correct' trae el msj de error (ej: usuario no existe en DB)
            QtWidgets.QMessageBox.warning(self.window, "Error de Ingreso", str(correct))
            return
        
        if correct:
            # Obtener el rol del usuario para aplicarlo a la ventana principal
            status_busq, usuarios = buscar_usuarios(username)
            user_role = "CAJERO"  # Por defecto
            if status_busq and usuarios:
                for registro in usuarios:
                    u = dict(registro)  # Forzar resolución de tipo a dict para Pylance
                    if u.get('username') == username:
                        user_role = str(u.get('rol', 'CAJERO')).upper()
                        break
            
            # Asignamos el rol al main_controller y mostramos la ventana
            self.main_controller.set_user_role(user_role)
            
            # Login Exitoso
            self.window.close()
            # Muestra el main window delegando al controllador central
            self.main_controller.main_window.show()
        else:
            QtWidgets.QMessageBox.warning(self.window, "Login Fallido", "Contraseña incorrecta.")
