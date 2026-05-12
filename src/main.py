import sys
from PySide6 import QtWidgets
from controllers.main_controller import MainController
from controllers.login_controller import LoginController
from views.theme import DARK_THEME

if __name__ == "__main__":
    # 1. Crear la aplicación
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)
    
    # 2. Crear la ventana principal de Qt (oculta inicialmente)
    MainWindow = QtWidgets.QMainWindow()
    
    # 3. Inicializar el controlador principa, el controlador se encarga de configurar la UI principal
    main_controller = MainController(MainWindow)
    
    # 4. Inicializar el controlador de Login
    login_controller = LoginController(main_controller)
    login_controller.show()
    
    # 5. Ejecutar el bucle principal
    sys.exit(app.exec())
