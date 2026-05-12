from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from views.mainwindow import Ui_MainWindow
from views.vista_tienda import Ui_Form as Ui_VistaTienda
from views.vista_clientes_b import Ui_Form as Ui_VistaClientesB
from views.vista_administracion_reportes import Ui_Form as Ui_VistaAdministracionReportes

# Importar dialogos
from views.dialogos import DialogCategoria, DialogProducto, DialogEmpleado, DialogProveedor, DialogCliente

# Importar modelos
from models.categoria_model import registrar_categoria, buscar_categoria
from models.producto_model import registrar_producto
from models.usuario_model import registrar_usuario
from models.proveedor_model import registrar_proveedor
from models.cliente_model import registrar_cliente

class MainController:
    def __init__(self, main_window: QtWidgets.QMainWindow):
        self.main_window = main_window
        self.login_controller = None # Referencia al LoginController
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.user_role = "CAJERO" # Rol por defecto
        
        self.load_views()
        self.connect_signals()

    def set_user_role(self, role: str):
        """Asigna el rol del usuario actualmente autenticado y bloquea la UI si es necesario."""
        self.user_role = role
        if self.user_role == "CAJERO":
            # Deshabilitar botones de administración
            self.ui.b_administracion_mainwindow.setEnabled(False)
            self.ui.b_clientes_mainwindow.setEnabled(False) # Asumiendo que cajeros no manejan clientes
            # Ocultarlos o dejarlos grises visualmente
        else:
            self.ui.b_administracion_mainwindow.setEnabled(True)
            self.ui.b_clientes_mainwindow.setEnabled(True)
        
    def load_views(self):
        """Carga e instancia las sub-vistas dentro del QStackedWidget principal."""
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
        # self._apply_layout_to_view(self.widget_tienda, self.ui_tienda)
        self.ui.stackedWidget.addWidget(self.widget_tienda)

        # 2. Vista Clientes (Búsqueda)
        self.widget_clientes_b = QtWidgets.QWidget()
        self.ui_clientes_b = Ui_VistaClientesB()
        self.ui_clientes_b.setupUi(self.widget_clientes_b)
        # self._apply_layout_to_view(self.widget_clientes_b, self.ui_clientes_b)
        self.ui.stackedWidget.addWidget(self.widget_clientes_b)
        
        # 3. Vista Administración/Reportes
        self.widget_admin = QtWidgets.QWidget()
        self.ui_admin = Ui_VistaAdministracionReportes()
        self.ui_admin.setupUi(self.widget_admin)
        # self._apply_layout_to_view(self.widget_admin, self.ui_admin)
        self.ui.stackedWidget.addWidget(self.widget_admin)
        
        # Inicialmente mostrar la tienda
        self.ui.stackedWidget.setCurrentWidget(self.widget_tienda)

    def _apply_layout_to_view(self, widget: QtWidgets.QWidget, ui_form):
        """Aplica un layout básico al contenedor de la sub-vista para que se expanda."""
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        children = widget.findChildren(QtWidgets.QWidget, options=Qt.FindChildOption.FindDirectChildrenOnly)
        for child in children:
            if child is not widget:
                layout.addWidget(child)
                child.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def connect_signals(self):
        """Conecta los botones de la interfaz."""
        # Botones menú lateral principal
        self.ui.b_tienda_mainwindow.clicked.connect(self.show_tienda)
        self.ui.b_clientes_mainwindow.clicked.connect(self.show_clientes)
        self.ui.b_administracion_mainwindow.clicked.connect(self.show_administracion)
        self.ui.b_cerrar_sesion_mainwindow.clicked.connect(self.cerrar_sesion)

        # Botones de Nuevas Entidades (Popups)
        self.ui_admin.btn_nueva_categoria.clicked.connect(self.mostrar_dialogo_categoria)
        self.ui_admin.btn_nuevo_producto.clicked.connect(self.mostrar_dialogo_producto)
        self.ui_admin.btn_nuevo_empleado.clicked.connect(self.mostrar_dialogo_empleado)
        self.ui_admin.btn_nuevo_proveedor.clicked.connect(self.mostrar_dialogo_proveedor)
        self.ui_clientes_b.btn_registrar.clicked.connect(self.mostrar_dialogo_cliente)

    # --- Slots de Navegación ---
    def show_tienda(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_tienda)
        self.ui.label_seccion_actual.setText("Punto de Venta")
        self._limpiar_botones_menu()
        self.ui.b_tienda_mainwindow.setChecked(True)

    def show_clientes(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_clientes_b)
        self.ui.label_seccion_actual.setText("Gestión de Clientes")
        self._limpiar_botones_menu()
        self.ui.b_clientes_mainwindow.setChecked(True)

    def show_administracion(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_admin)
        self.ui.label_seccion_actual.setText("Panel de Administración")
        self._limpiar_botones_menu()
        self.ui.b_administracion_mainwindow.setChecked(True)

    def _limpiar_botones_menu(self):
        self.ui.b_tienda_mainwindow.setChecked(False)
        self.ui.b_clientes_mainwindow.setChecked(False)
        self.ui.b_administracion_mainwindow.setChecked(False)

    def cerrar_sesion(self):
        """Cierra la ventana principal y vuelve a mostrar el login, limpiando las entradas."""
        self.main_window.close()
        if self.login_controller:
            self.login_controller.ui.line_usuario_login.clear()
            self.login_controller.ui.line_contrasea_login.clear()
            self.login_controller.show()

    # --- Slots de Popups (Dialogs) ---
    def mostrar_dialogo_categoria(self):
        dialog = DialogCategoria(self.main_window)
        if dialog.exec():
            nombre = dialog.line_nombre.text().strip()
            desc = dialog.line_desc.text().strip()
            
            if not nombre:
                QtWidgets.QMessageBox.warning(self.main_window, "Validación", "El nombre de la categoría es obligatorio.")
                return
            
            # Guardamos a BD
            datos = {"nombre": nombre, "descripcion": desc, "estado": 1}
            status, msg = registrar_categoria(datos)
            if status:
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Categoría registrada correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self.main_window, "Error", str(msg))

    def mostrar_dialogo_producto(self):
        # Para el producto necesitamos cargar las categorías
        status, categorias = buscar_categoria("")
        if not status or not categorias:
            QtWidgets.QMessageBox.warning(self.main_window, "Aviso", "Primero debe registrar al menos una categoría.")
            return

        dialog = DialogProducto(list(categorias), self.main_window)
        if dialog.exec():
            codigo = dialog.line_codigo.text().strip()
            nombre = dialog.line_nombre.text().strip()
            precio = dialog.line_precio.text().strip()
            stock = dialog.line_stock.text().strip()
            desc = dialog.line_desc.text().strip()
            id_categoria = dialog.combo_categoria.currentData()

            if not all([codigo, nombre, precio, stock]):
                QtWidgets.QMessageBox.warning(self.main_window, "Validación", "Todos los campos con asterisco son obligatorios.")
                return
            
            try:
                precio = float(precio)
                stock = int(stock)
            except ValueError:
                QtWidgets.QMessageBox.warning(self.main_window, "Validación", "Precios deben ser numéricos y stock entero.")
                return

            datos = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "stock": stock,
                "descripcion": desc,
                "id_categoria": id_categoria
            }
            status_reg, msg = registrar_producto(datos)
            if status_reg:
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Producto registrado correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self.main_window, "Error", str(msg))

    def mostrar_dialogo_empleado(self):
        dialog = DialogEmpleado(self.main_window)
        if dialog.exec():
            nombre = dialog.line_nombre.text().strip()
            username = dialog.line_username.text().strip()
            password = dialog.line_password.text().strip()
            rol = dialog.combo_rol.currentText()

            if not all([nombre, username, password]):
                QtWidgets.QMessageBox.warning(self.main_window, "Validación", "Todos los campos obligatorios deben ser llenados.")
                return

            datos = {
                "nombre": nombre,
                "username": username,
                "password": password,
                "rol": rol,
                "estado": 1
            }
            status, msg = registrar_usuario(datos)
            if status:
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Empleado registrado correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self.main_window, "Error", str(msg))

    def mostrar_dialogo_proveedor(self):
        dialog = DialogProveedor(self.main_window)
        if dialog.exec():
            nombre = dialog.line_nombre.text().strip()
            telefono = dialog.line_telefono.text().strip()
            direccion = dialog.line_direccion.text().strip()

            if not nombre or not telefono:
                QtWidgets.QMessageBox.warning(self.main_window, "Validación", "Nombre social y teléfono son obligatorios.")
                return

            datos = {
                "nombre": nombre,
                "telefono": telefono,
                "direccion": direccion,
                "estado": 1
            }
            status, msg = registrar_proveedor(datos)
            if status:
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Proveedor registrado correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self.main_window, "Error", str(msg))

    def mostrar_dialogo_cliente(self):
        dialog = DialogCliente(self.main_window)
        if dialog.exec():
            nombre = dialog.line_nombre.text().strip()
            telefono = dialog.line_telefono.text().strip()
            direccion = dialog.line_direccion.text().strip()

            if not nombre or not telefono:
                QtWidgets.QMessageBox.warning(self.main_window, "Validación", "El Nombre y Teléfono son obligatorios.")
                return

            datos = {
                "nombre": nombre,
                "telefono": telefono,
                "direccion": direccion,
                "estado": 1
            }
            status, msg = registrar_cliente(datos)
            if status:
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Cliente registrado correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self.main_window, "Error", str(msg))
