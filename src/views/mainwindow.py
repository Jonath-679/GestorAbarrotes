from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QPushButton, QStackedWidget, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(800, 500)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.main_layout = QHBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # --- SIDEBAR IZQUIERDO ---
        self.frame_sidebar = QFrame(self.centralwidget)
        self.frame_sidebar.setProperty("class", "HeaderFrame") 
        self.frame_sidebar.setFixedWidth(220)
        self.sidebar_layout = QVBoxLayout(self.frame_sidebar)
        self.sidebar_layout.setContentsMargins(0, 20, 0, 20)
        self.sidebar_layout.setSpacing(10)
        
        # Logo o Titulo
        self.label_bienvenido_mainwindow = QLabel("Abarrotesv v1.0")
        self.label_bienvenido_mainwindow.setProperty("class", "Title")
        self.label_bienvenido_mainwindow.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.label_bienvenido_mainwindow)
        
        # Spacer
        self.sidebar_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        
        # Botones de navegación
        self.b_tienda_mainwindow = QPushButton("💳  Punto de Venta")
        self.b_tienda_mainwindow.setProperty("class", "MenuButton")
        self.b_tienda_mainwindow.setCheckable(True)
        self.sidebar_layout.addWidget(self.b_tienda_mainwindow)
        
        self.b_clientes_mainwindow = QPushButton("👥  Clientes")
        self.b_clientes_mainwindow.setProperty("class", "MenuButton")
        self.b_clientes_mainwindow.setCheckable(True)
        self.sidebar_layout.addWidget(self.b_clientes_mainwindow)
        
        self.b_administracion_mainwindow = QPushButton("⚙️  Administración")
        self.b_administracion_mainwindow.setProperty("class", "MenuButton")
        self.b_administracion_mainwindow.setCheckable(True)
        self.sidebar_layout.addWidget(self.b_administracion_mainwindow)
        
        # Spacer al fondo
        self.sidebar_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        # Cerrar Sesion
        self.b_cerrar_sesion_mainwindow = QPushButton("Cerrar Sesión")
        self.b_cerrar_sesion_mainwindow.setProperty("class", "DangerButton")
        self.b_cerrar_sesion_mainwindow.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sidebar_layout.addWidget(self.b_cerrar_sesion_mainwindow)
        
        # --- PANEL PRINCIPAL (DERECHA) ---
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.main_panel_layout = QVBoxLayout(self.frame_main)
        self.main_panel_layout.setContentsMargins(0, 0, 0, 0)
        self.main_panel_layout.setSpacing(0)
        
        # Barra superior (Header info)
        self.frame_barra = QFrame(self.frame_main)
        self.frame_barra.setProperty("class", "HeaderFrame")
        self.frame_barra.setFixedHeight(60)
        self.top_bar_layout = QHBoxLayout(self.frame_barra)
        self.top_bar_layout.setContentsMargins(20, 0, 20, 0)
        
        self.label_seccion_actual = QLabel("Sección")
        self.label_seccion_actual.setProperty("class", "Subtitle")
        self.top_bar_layout.addWidget(self.label_seccion_actual)
        self.top_bar_layout.addStretch()
        
        self.label_usuario_activo = QLabel("Usuario: Admin")
        self.top_bar_layout.addWidget(self.label_usuario_activo)
        
        # Stacked Widget
        self.stackedWidget = QStackedWidget(self.frame_main)
        
        # Ensamblar panel principal
        self.main_panel_layout.addWidget(self.frame_barra)
        self.main_panel_layout.addWidget(self.stackedWidget)
        
        # Ensamblar todo
        self.main_layout.addWidget(self.frame_sidebar)
        self.main_layout.addWidget(self.frame_main)
