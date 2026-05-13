from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from views.mainwindow import Ui_MainWindow
from views.vista_tienda import Ui_Form as Ui_VistaTienda
from views.vista_clientes_b import Ui_Form as Ui_VistaClientesB
from views.vista_administracion_reportes import Ui_Form as Ui_VistaAdministracionReportes

# Importar dialogos
from views.dialogos import DialogCategoria, DialogProducto, DialogEmpleado, DialogProveedor, DialogCliente, DialogSeleccionarProducto

# Importar modelos
from models.categoria_model import registrar_categoria, buscar_categoria
from models.producto_model import registrar_producto, buscar_producto
from models.usuario_model import registrar_usuario, buscar_usuarios
from models.proveedor_model import registrar_proveedor, buscar_proveedor
from models.cliente_model import registrar_cliente, buscar_cliente
from models.venta_model import registrar_venta, registrar_venta_transaccional, listar_ventas
from models.reportes_model import reporte_inventario, reporte_clientes, reporte_usuarios, reporte_ventas, reporte_logs
from models.log_model import registrar_log
import database.connection as db_conn
from config import DB_PATH, DB_EJEMPLO_PATH

class MainController:
    def __init__(self, main_window: QtWidgets.QMainWindow):
        self.main_window = main_window
        self.login_controller = None # Referencia al LoginController
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.user_role = "CAJERO" # Rol por defecto
        self.current_user_id = 1 # Usuario actual en sesión
        self.current_user_name = "Invitado"
        self.carrito = [] # Lista de diccionarios con el carrito actual
        self.cliente_actual = None # Cliente seleccionado para la venta
        
        self.ui.label_usuario_activo.setText(f"Usuario: {self.current_user_name}")
        self.load_views()
        self.connect_signals()

    def set_user_role(self, role: str):
        """Asigna el rol del usuario actualmente autenticado y bloquea la UI si es necesario."""
        self.user_role = role
        if self.user_role == "CAJERO":
            # Deshabilitar botones de administración
            self.ui.b_administracion_mainwindow.setEnabled(False)
            self.ui.b_clientes_mainwindow.setEnabled(True) # Los cajeros sí manejan clientes
            # Ocultarlos o dejarlos grises visualmente
        else:
            self.ui.b_administracion_mainwindow.setEnabled(True)
            self.ui.b_clientes_mainwindow.setEnabled(True)
        
    def set_active_user(self, nombre: str, username: str = "", user_id: int = None):
        """Actualiza la etiqueta de usuario activo en la ventana principal."""
        if user_id is not None:
            self.current_user_id = user_id
        self.current_user_name = nombre or username or "Invitado"
        self.ui.label_usuario_activo.setText(f"Usuario: {self.current_user_name}")
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
        self.ui_admin.btn_toggle_db.clicked.connect(self.cambiar_base_de_datos)
        self.ui_clientes_b.btn_registrar.clicked.connect(self.mostrar_dialogo_cliente)

        # Botones de Generación de Reportes
        self.ui_admin.btn_rep_ventas.clicked.connect(self.generar_reporte_ventas)
        self.ui_admin.btn_rep_inventario.clicked.connect(self.generar_reporte_inventario)
        self.ui_admin.btn_rep_clientes.clicked.connect(self.generar_reporte_clientes)
        self.ui_admin.btn_rep_empleados.clicked.connect(self.generar_reporte_usuarios)
        self.ui_admin.btn_rep_logs.clicked.connect(self.generar_reporte_logs)

        # Buscar y Cargar en Clientes
        self.ui_clientes_b.btn_buscar.clicked.connect(self.buscar_clientes)
        self.ui_clientes_b.btn_actualizar.clicked.connect(self.buscar_clientes)

        # Acciones de Tienda (Punto de Venta)
        self.ui_tienda.btn_buscar.clicked.connect(self.buscar_producto_tienda)
        self.ui_tienda.btn_agregar.clicked.connect(self.agregar_al_carrito)
        self.ui_tienda.btn_eliminar_item.clicked.connect(self.eliminar_del_carrito)
        self.ui_tienda.btn_cancelar_venta.clicked.connect(self.cancelar_venta)
        self.ui_tienda.btn_cobrar.clicked.connect(self.realizar_cobro)

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
        self.buscar_clientes() # Cargar clientes al entrar

    def show_administracion(self):
        self.ui.stackedWidget.setCurrentWidget(self.widget_admin)
        self.ui.label_seccion_actual.setText("Panel de Administración")
        self._limpiar_botones_menu()
        self.ui.b_administracion_mainwindow.setChecked(True)
        self.actualizar_tablas_admin()

    def actualizar_tablas_admin(self):
        # 1. Poblar Inventario
        self.ui_admin.tabla_productos.setRowCount(0)
        status, productos = buscar_producto("")
        if status and productos:
            status_c, categorias = buscar_categoria("")
            cat_map = {c['id_categoria']: c['nombre'] for c in categorias} if status_c else {}
            for row, p in enumerate(productos):
                p_dict = dict(p)
                self.ui_admin.tabla_productos.insertRow(row)
                self.ui_admin.tabla_productos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(p_dict.get('codigo', ''))))
                self.ui_admin.tabla_productos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(p_dict.get('nombre', ''))))
                self.ui_admin.tabla_productos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(p_dict.get('precio', ''))))
                self.ui_admin.tabla_productos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(p_dict.get('precio', '')))) # Venta y compra = same here logic
                self.ui_admin.tabla_productos.setItem(row, 4, QtWidgets.QTableWidgetItem(str(p_dict.get('stock', ''))))
                self.ui_admin.tabla_productos.setItem(row, 5, QtWidgets.QTableWidgetItem(str(cat_map.get(p_dict.get('id_categoria'), 'N/A'))))
                
        # 2. Poblar Categorías
        self.ui_admin.tabla_categorias.setRowCount(0)
        status, categorias = buscar_categoria("")
        if status and categorias:
            for row, c in enumerate(categorias):
                c_dict = dict(c)
                self.ui_admin.tabla_categorias.insertRow(row)
                self.ui_admin.tabla_categorias.setItem(row, 0, QtWidgets.QTableWidgetItem(str(c_dict.get('id_categoria', ''))))
                self.ui_admin.tabla_categorias.setItem(row, 1, QtWidgets.QTableWidgetItem(str(c_dict.get('nombre', ''))))
                self.ui_admin.tabla_categorias.setItem(row, 2, QtWidgets.QTableWidgetItem(str("Activo" if c_dict.get('estado') == 1 else "Inactivo")))
                
        # 3. Poblar Empleados
        self.ui_admin.tabla_empleados.setRowCount(0)
        status, empleados = buscar_usuarios("")
        if status and empleados:
            for row, e in enumerate(empleados):
                e_dict = dict(e)
                self.ui_admin.tabla_empleados.insertRow(row)
                self.ui_admin.tabla_empleados.setItem(row, 0, QtWidgets.QTableWidgetItem(str(e_dict.get('id_usuario', ''))))
                self.ui_admin.tabla_empleados.setItem(row, 1, QtWidgets.QTableWidgetItem(str(e_dict.get('nombre', ''))))
                self.ui_admin.tabla_empleados.setItem(row, 2, QtWidgets.QTableWidgetItem(str(e_dict.get('username', ''))))
                self.ui_admin.tabla_empleados.setItem(row, 3, QtWidgets.QTableWidgetItem(str(e_dict.get('rol', ''))))
                self.ui_admin.tabla_empleados.setItem(row, 4, QtWidgets.QTableWidgetItem(str("Activo" if e_dict.get('estado') == 1 else "Inactivo")))
                
        # 4. Poblar Proveedores
        self.ui_admin.tabla_proveedores.setRowCount(0)
        status, proveedores = buscar_proveedor("")
        if status and proveedores:
            for row, pr in enumerate(proveedores):
                pr_dict = dict(pr)
                self.ui_admin.tabla_proveedores.insertRow(row)
                self.ui_admin.tabla_proveedores.setItem(row, 0, QtWidgets.QTableWidgetItem(str(pr_dict.get('id_proveedor', ''))))
                self.ui_admin.tabla_proveedores.setItem(row, 1, QtWidgets.QTableWidgetItem(str(pr_dict.get('nombre', ''))))
                self.ui_admin.tabla_proveedores.setItem(row, 2, QtWidgets.QTableWidgetItem(str(pr_dict.get('telefono', ''))))
                self.ui_admin.tabla_proveedores.setItem(row, 3, QtWidgets.QTableWidgetItem(str(pr_dict.get('direccion', ''))))
                
        # 5. Poblar Historial/Ventas Recientes
        self.ui_admin.tabla_historial_ventas.setRowCount(0)
        status, ventas = listar_ventas()
        if status and ventas:
            # Obtener mapas rápidos de cajero / cliente
            u_status, us = buscar_usuarios("")
            c_status, cl = buscar_cliente("")
            us_map = {u['id_usuario']: u['nombre'] for u in us} if u_status else {}
            cl_map = {c['id_cliente']: c['nombre'] for c in cl} if c_status else {}
            for row, v in enumerate(ventas):
                v_dict = dict(v)
                self.ui_admin.tabla_historial_ventas.insertRow(row)
                self.ui_admin.tabla_historial_ventas.setItem(row, 0, QtWidgets.QTableWidgetItem(str(v_dict.get('id_venta', ''))))
                self.ui_admin.tabla_historial_ventas.setItem(row, 1, QtWidgets.QTableWidgetItem(str(v_dict.get('fecha_hora', ''))))
                self.ui_admin.tabla_historial_ventas.setItem(row, 2, QtWidgets.QTableWidgetItem(f"${v_dict.get('total', 0):.2f}"))
                self.ui_admin.tabla_historial_ventas.setItem(row, 3, QtWidgets.QTableWidgetItem(str(us_map.get(v_dict.get('id_usuario'), 'N/A'))))
                self.ui_admin.tabla_historial_ventas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(cl_map.get(v_dict.get('id_cliente'), 'Mostrador'))))

    def _limpiar_botones_menu(self):
        self.ui.b_tienda_mainwindow.setChecked(False)
        self.ui.b_clientes_mainwindow.setChecked(False)
        self.ui.b_administracion_mainwindow.setChecked(False)

    def cerrar_sesion(self):
        """Cierra la ventana principal y vuelve a mostrar el login, limpiando las entradas."""
        # Registrar salida antes de cerrar BD
        registrar_log({
            "id_usuario": self.current_user_id,
            "accion": "Cierre de Sesión",
            "modulo": "Auth",
            "descripcion": "El usuario cerró sesión."
        })
        db_conn.close_connection()
        self.main_window.close()
        if self.login_controller:
            self.login_controller.ui.line_usuario_login.clear()
            self.login_controller.ui.line_contrasea_login.clear()
            self.login_controller.show()

    def cambiar_base_de_datos(self):
        reply = QtWidgets.QMessageBox.question(
            self.main_window, 
            "Cambiar Base de Datos",
            "¿Estás seguro de que deseas cambiar la base de datos temporalmente?\nSe cerrará tu sesión actual.", 
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            texto_btn = self.ui_admin.btn_toggle_db.text()
            usar_ejemplo = "Ejemplo" not in texto_btn
            
            if usar_ejemplo:
                self.ui_admin.btn_toggle_db.setText("🔄 Cambiar Base de Datos (Actual: Ejemplo)")
            else:
                self.ui_admin.btn_toggle_db.setText("🔄 Cambiar Base de Datos (Actual: Producción)")
                
            db_conn.set_database(usar_ejemplo)
            QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Se ha cambiado la configuración de la Base de Datos. Inicia sesión nuevamente.")
            self.cerrar_sesion()

    # --- Generación de Reportes ---
    def _handle_report_result(self, status: bool, value: str, nombre_reporte: str):
        if status:
            QtWidgets.QMessageBox.information(self.main_window, "Reporte Generado", f"El {nombre_reporte} se generó exitosamente en:\n{value}")
        else:
            QtWidgets.QMessageBox.warning(self.main_window, "Error de Reporte", f"Ocurrió un error al generar el reporte:\n{value}")

    def generar_reporte_ventas(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_window, "Guardar Reporte de Ventas", "reporte_ventas.xlsx", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            status, value = reporte_ventas(file_path)
            self._handle_report_result(status, str(value), "Reporte de Ventas")

    def generar_reporte_inventario(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_window, "Guardar Reporte de Inventario", "reporte_inventario.xlsx", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            status, value = reporte_inventario(file_path)
            self._handle_report_result(status, str(value), "Reporte de Inventario")

    def generar_reporte_clientes(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_window, "Guardar Reporte de Clientes", "reporte_clientes.xlsx", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            status, value = reporte_clientes(file_path)
            self._handle_report_result(status, str(value), "Reporte de Clientes")

    def generar_reporte_usuarios(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_window, "Guardar Reporte de Empleados", "reporte_usuarios.xlsx", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            status, value = reporte_usuarios(file_path)
            self._handle_report_result(status, str(value), "Reporte de Empleados/Usuarios")

    def generar_reporte_logs(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self.main_window, "Guardar Reporte de Logs", "reporte_logs.xlsx", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            status, value = reporte_logs(file_path)
            self._handle_report_result(status, str(value), "Reporte de Logs")

    # --- Lógica de Clientes ---
    def buscar_clientes(self):
        criterio = self.ui_clientes_b.line_buscar.text().strip()
        status, clientes = buscar_cliente(criterio)
        if not status or not isinstance(clientes, (list, tuple)):
            QtWidgets.QMessageBox.warning(self.main_window, "Error", str(clientes))
            return
        
        self.ui_clientes_b.tabla_clientes.setRowCount(0)
        for row, c in enumerate(clientes):
            c_dict = dict(c) # type: ignore
            self.ui_clientes_b.tabla_clientes.insertRow(row)
            self.ui_clientes_b.tabla_clientes.setItem(row, 0, QtWidgets.QTableWidgetItem(str(c_dict.get('id_cliente', ''))))
            self.ui_clientes_b.tabla_clientes.setItem(row, 1, QtWidgets.QTableWidgetItem(str(c_dict.get('nombre', ''))))
            self.ui_clientes_b.tabla_clientes.setItem(row, 2, QtWidgets.QTableWidgetItem(str(c_dict.get('telefono', ''))))
            self.ui_clientes_b.tabla_clientes.setItem(row, 3, QtWidgets.QTableWidgetItem(str(c_dict.get('direccion', ''))))
            self.ui_clientes_b.tabla_clientes.setItem(row, 4, QtWidgets.QTableWidgetItem(str("Activo" if c_dict.get('estado') == 1 else "Inactivo")))

    # --- Lógica de Tienda (Punto de Venta) ---
    def buscar_producto_tienda(self):
        criterio = self.ui_tienda.line_buscar_producto.text().strip()
        dialog = DialogSeleccionarProducto(self.main_window)
        dialog.line_buscar.setText(criterio)
        
        def do_search():
            crit = dialog.line_buscar.text().strip()
            status, prods = buscar_producto(crit)
            dialog.tabla.setRowCount(0)
            if status and isinstance(prods, (list, tuple)):
                for row, p in enumerate(prods):
                    pd = dict(p) # type: ignore
                    dialog.tabla.insertRow(row)
                    dialog.tabla.setItem(row, 0, QtWidgets.QTableWidgetItem(str(pd.get('codigo', ''))))
                    dialog.tabla.setItem(row, 1, QtWidgets.QTableWidgetItem(str(pd.get('nombre', ''))))
                    dialog.tabla.setItem(row, 2, QtWidgets.QTableWidgetItem(str(pd.get('precio', ''))))
                    dialog.tabla.setItem(row, 3, QtWidgets.QTableWidgetItem(str(pd.get('stock', ''))))
        
        dialog.btn_buscar.clicked.connect(do_search)
        dialog.line_buscar.returnPressed.connect(do_search)
        
        if criterio:
            do_search()
            
        if dialog.exec():
            if dialog.producto_seleccionado:
                self.ui_tienda.line_buscar_producto.setText(dialog.producto_seleccionado)
                self.agregar_al_carrito()

    def agregar_al_carrito(self):
        codigo = self.ui_tienda.line_buscar_producto.text().strip()
        if not codigo:
            return
        
        status, productos = buscar_producto(codigo)
        if status and isinstance(productos, (list, tuple)) and len(productos) > 0:
            # Buscamos la coincidencia exacta por código
            p_exacto = next((dict(p) for p in productos if dict(p).get('codigo') == codigo), None) # type: ignore
            if not p_exacto:
                # Si no hay coincidencia exacta pero sí resultados, agarramos el primero
                p_exacto = dict(productos[0]) # type: ignore
            
            p_nombre = str(p_exacto.get('nombre', ''))
            p_stock = int(str(p_exacto.get('stock', 0)))
            
            # Pedir cantidad
            cantidad, ok = QtWidgets.QInputDialog.getInt(self.main_window, "Cantidad", f"Cantidad para {p_nombre}:", 1, 1, p_stock, 1)
            if ok:
                subtotal = cantidad * float(str(p_exacto.get('precio', 0)))
                self.carrito.append({
                    "id_producto": p_exacto.get('id_producto'),
                    "codigo": p_exacto.get('codigo'),
                    "nombre": p_nombre,
                    "cantidad": cantidad,
                    "precio_unitario": p_exacto.get('precio'),
                    "subtotal": subtotal
                })
                self.actualizar_tabla_carrito()
                self.ui_tienda.line_buscar_producto.clear()
        else:
            QtWidgets.QMessageBox.warning(self.main_window, "Error", "No se encontró el producto para añadir.")

    def eliminar_del_carrito(self):
        fila = self.ui_tienda.tabla_carrito.currentRow()
        if fila >= 0:
            self.carrito.pop(fila)
            self.actualizar_tabla_carrito()
        else:
            QtWidgets.QMessageBox.warning(self.main_window, "Aviso", "Seleccione un producto del carrito para quitar.")

    def cancelar_venta(self):
        if not self.carrito: return
        resp = QtWidgets.QMessageBox.question(self.main_window, "Cancelar Venta", "¿Está seguro que desea vaciar el carrito?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if resp == QtWidgets.QMessageBox.StandardButton.Yes:
            self.carrito.clear()
            self.actualizar_tabla_carrito()
            self.cliente_actual = None

    def actualizar_tabla_carrito(self):
        self.ui_tienda.tabla_carrito.setRowCount(0)
        total = 0.0
        for row, item in enumerate(self.carrito):
            self.ui_tienda.tabla_carrito.insertRow(row)
            self.ui_tienda.tabla_carrito.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item['codigo'])))
            self.ui_tienda.tabla_carrito.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item['nombre'])))
            self.ui_tienda.tabla_carrito.setItem(row, 2, QtWidgets.QTableWidgetItem(str(item['cantidad'])))
            self.ui_tienda.tabla_carrito.setItem(row, 3, QtWidgets.QTableWidgetItem(f"${item['precio_unitario']:.2f}"))
            self.ui_tienda.tabla_carrito.setItem(row, 4, QtWidgets.QTableWidgetItem(f"${item['subtotal']:.2f}"))
            total += item['subtotal']
        
        self.ui_tienda.label_total_valor.setText(f"$ {total:.2f}")

    def realizar_cobro(self):
        if not self.carrito:
            QtWidgets.QMessageBox.warning(self.main_window, "Carrito Vacío", "No hay productos para cobrar.")
            return
        
        # El ID viene del inicio de sesión (del controlador login o se asigna por defecto si falla)
        id_usuario = self.current_user_id
        
        total_venta = sum(item['subtotal'] for item in self.carrito)
        
        # ¿Cliente especifico o mostrador? (Podríamos agregar logica de seleccion de cliente aqui, por ahora None es mostrador)
        id_cliente = None
        if self.cliente_actual:
            id_cliente = self.cliente_actual['id_cliente']
            
        respuesta = QtWidgets.QMessageBox.question(
            self.main_window, 
            "Confirmar Cobro", 
            f"¿Desea registrar la venta por un total de ${total_venta:.2f}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        
        if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
            # 1. Registrar_venta maestra
            datos_venta = {
                "id_usuario": id_usuario,
                "id_cliente": id_cliente,
                "total": total_venta
            }
            status, result = registrar_venta(datos_venta)
            if not status:
                QtWidgets.QMessageBox.critical(self.main_window, "Error de Venta", f"Ocurrió un error al registrar: {result}")
                return
                
            id_venta_generada = int(str(result)) # <--- Ya modificado en el modelo para traer ID
            
            # 2. Detalles transaccionales    
            status_trans, msg_trans = registrar_venta_transaccional(id_venta_generada, self.carrito)
            
            if status_trans:
                registrar_log({
                    "id_usuario": self.current_user_id,
                    "accion": "Cobro de Venta",
                    "modulo": "Tienda",
                    "descripcion": f"Venta ID {id_venta_generada} por un total de ${total_venta:.2f}"
                })
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Cobro realizado y ticket registrado con éxito.")
                self.carrito.clear()
                self.actualizar_tabla_carrito()
                self.cliente_actual = None
            else:
                QtWidgets.QMessageBox.critical(self.main_window, "Error en Detalles", f"Se creó la venta general pero falló el registro de productos:\n{msg_trans}")


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
                registrar_log({
                    "id_usuario": self.current_user_id,
                    "accion": "Crear Categoría",
                    "modulo": "Administración",
                    "descripcion": f"Creó la categoría '{nombre}'"
                })
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
                registrar_log({
                    "id_usuario": self.current_user_id,
                    "accion": "Crear Producto",
                    "modulo": "Administración",
                    "descripcion": f"Creó el producto '{nombre}' ({codigo})"
                })
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
                registrar_log({
                    "id_usuario": self.current_user_id,
                    "accion": "Crear Empleado",
                    "modulo": "Administración",
                    "descripcion": f"Creó al empleado '{username}' ({rol})"
                })
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
                registrar_log({
                    "id_usuario": self.current_user_id,
                    "accion": "Crear Proveedor",
                    "modulo": "Administración",
                    "descripcion": f"Creó al proveedor '{nombre}'"
                })
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
                registrar_log({
                    "id_usuario": self.current_user_id,
                    "accion": "Crear Cliente",
                    "modulo": "Clientes",
                    "descripcion": f"Creó al cliente '{nombre}'"
                })
                QtWidgets.QMessageBox.information(self.main_window, "Éxito", "Cliente registrado correctamente.")
            else:
                QtWidgets.QMessageBox.warning(self.main_window, "Error", str(msg))
