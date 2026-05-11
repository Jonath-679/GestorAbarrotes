import sys
from PySide6 import QtWidgets
from views.mainwindow import Ui_MainWindow

if __name__ == "__main__":
    # 1. Crear la aplicación
    app = QtWidgets.QApplication(sys.argv)
    
    # 2. Crear la ventana principal de Qt
    MainWindow = QtWidgets.QMainWindow()
    
    # 3. Instanciar tu clase de la interfaz y configurarla
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Make the UI responsive by applying layouts at runtime.
    central = ui.centralwidget

    main_layout = QtWidgets.QHBoxLayout(central)
    main_layout.setContentsMargins(10, 10, 10, 10)
    main_layout.setSpacing(10)

    left_container = QtWidgets.QWidget(central)
    left_layout = QtWidgets.QVBoxLayout(left_container)
    left_layout.setContentsMargins(0, 0, 0, 0)
    left_layout.setSpacing(10)
    left_layout.addWidget(ui.label_bienvenido_mainwindow)
    left_layout.addWidget(ui.frame, 1)
    left_layout.addWidget(ui.b_cerrar_sesion_mainwindow)
    left_container.setSizePolicy(
        QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding
    )
    left_container.setMinimumWidth(211)

    right_container = QtWidgets.QWidget(central)
    right_layout = QtWidgets.QVBoxLayout(right_container)
    right_layout.setContentsMargins(0, 0, 0, 0)
    right_layout.setSpacing(10)
    right_layout.addWidget(ui.frame_barra)
    right_layout.addWidget(ui.stackedWidget, 1)
    right_container.setSizePolicy(
        QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
    )

    ui.frame_barra.setSizePolicy(
        QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
    )
    ui.stackedWidget.setSizePolicy(
        QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
    )

    main_layout.addWidget(left_container)
    main_layout.addWidget(right_container, 1)

    MainWindow.setMinimumSize(MainWindow.sizeHint())
    
    # 4. Mostrar la ventana y ejecutar el bucle principal
    MainWindow.show()
    sys.exit(app.exec())
