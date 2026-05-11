import sys
from PySide6 import QtWidgets
from controllers.main_controller import MainController

if __name__ == "__main__":
    # 1. Crear la aplicación
    app = QtWidgets.QApplication(sys.argv)
    
    # 2. Crear la ventana principal de Qt
    MainWindow = QtWidgets.QMainWindow()
    
    # 3. Inicializar el controlador principal
    # El controlador se encarga de configurar la UI y las señales
    controller = MainController(MainWindow)
    
    # 4. Mostrar la ventana y ejecutar el bucle principal
    MainWindow.show()
    sys.exit(app.exec())
