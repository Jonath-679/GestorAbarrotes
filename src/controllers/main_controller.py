from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from views.mainwindow import Ui_MainWindow
from views.vista_tienda import Ui_Form as Ui_VistaTienda
from views.vista_clientes_b import Ui_Form as Ui_VistaClientesB
from views.vista_administracion_reportes import Ui_Form as Ui_VistaAdministracionReportes

class MainController:
    def __init__(self, main_window: QtWidgets.QMainWindow):
        self.main_window = main_window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        
        self.setup_responsive_layout()
        self.load_views()
        self.connect_signals()
        
    def setup_responsive_layout(self):
        """Aplica layouts en tiempo de ejecución para ajustar la ventana."""
        central = self.ui.centralwidget

        main_layout = QtWidgets.QHBoxLayout(central)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        left_container = QtWidgets.QWidget(central)
        left_layout = QtWidgets.QVBoxLayout(left_container)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)
        left_layout.addWidget(self.ui.label_bienvenido_mainwindow)
        left_layout.addWidget(self.ui.frame, 1)
        left_layout.addWidget(self.ui.b_cerrar_sesion_mainwindow)
        left_container.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding
        )
        left_container.setMinimumWidth(211)

        right_container = QtWidgets.QWidget(central)
        right_layout = QtWidgets.QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)
        right_layout.addWidget(self.ui.frame_barra)
        right_layout.addWidget(self.ui.stackedWidget, 1)
        right_container.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )

        self.ui.frame_barra.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.ui.stackedWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )

        main_layout.addWidget(left_container)
        main_layout.addWidget(right_container, 1)

        self.main_window.setMinimumSize(self.main_window.sizeHint())

    def load_views(self):
        """Carga e instancia las sub-vistas dentro del QStackedWidget principal."""
        # Limpiar el stackedWidget de las paginas generadas por defecto (page, page_2)
        while self.ui.stackedWidget.count() > 0:
            widget = self.ui.stackedWidget.widget(0)
            if widget is not None:
                self.ui.stackedWidget.removeWidget(widget)
                widget.deleteLater()
            else:
                break

        # 1. Vista Tienda
        self.widget_tienda = QtWidgets.QWidget()
        self.ui_tienda = Ui_VistaTienda()
        self.ui_tienda.setupUi(self.widget_tienda)
        self._apply_layout_to_view(self.widget_tienda, self.ui_tienda)
        self.ui.stackedWidget.addWidget(self.widget_tienda)

        # 2. Vista Clientes (Búsqueda)
        self.widget_clientes_b = QtWidgets.QWidget()
        self.ui_clientes_b = Ui_VistaClientesB()
        self.ui_clientes_b.setupUi(self.widget_clientes_b)
        self._apply_layout_to_view(self.widget_clientes_b, self.ui_clientes_b)
        self.ui.stackedWidget.addWidget(self.widget_clientes_b)
        
        # 3. Vista Administración/Reportes
        self.widget_admin = QtWidgets.QWidget()
        self.ui_admin = Ui_VistaAdministracionReportes()
        self.ui_admin.setupUi(self.widget_admin)
        self._apply_layout_to_view(self.widget_admin, self.ui_admin)
        self.ui.stackedWidget.addWidget(self.widget_admin)
        
        # Inicialmente mostrar la tienda
        self.ui.stackedWidget.setCurrentWidget(self.widget_tienda)

    def _apply_layout_to_view(self, widget: QtWidgets.QWidget, ui_form):
        """Aplica un layout básico al contenedor de la sub-vista para que se expanda."""
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Como los .ui generan widgets estáticos, buscaremos los elementos raíz (Frames, Tablas, etc.)
        # y los agregaremos al layout para que Qt los expanda.
        children = widget.findChildren(QtWidgets.QWidget, options=Qt.FindChildOption.FindDirectChildrenOnly)
        for child in children:
            if child is not widget:
                layout.addWidget(child)
                child.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def connect_signals(self):
        """Conecta los botones del menú lateral (MainWindow) con sus acciones respectivas."""
        self.ui.b_tienda_mainwindow.clicked.connect(self.show_tienda)
        self.ui.b_clientes_mainwindow.clicked.connect(self.show_clientes)
        self.ui.b_administracion_mainwindow.clicked.connect(self.show_administracion)
        # TODO: Implementar cierre de sesión con self.ui.b_cerrar_sesion_mainwindow

    # --- Slots de Navegación ---
    def show_tienda(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_tienda)

    def show_clientes(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_clientes_b)

    def show_administracion(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_admin)
