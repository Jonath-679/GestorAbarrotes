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
    
    # 4. Mostrar la ventana y ejecutar el bucle principal
    MainWindow.show()
    sys.exit(app.exec())
