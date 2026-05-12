# Tema oscuro unificado y moderno para la aplicación

DARK_THEME = """
QWidget {
    background-color: #1e1e1e;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 14px;
}

/* Modificadores de fondo para contenedores principales */
QMainWindow, QStackedWidget {
    background-color: #121212;
}

/* Campos de texto */
QLineEdit {
    background-color: #2b2b2b;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 8px;
    color: #ffffff;
}

QLineEdit:focus {
    border: 1px solid #007acc;
    background-color: #333333;
}

/* Botones principales y generales */
QPushButton {
    background-color: #007acc;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 10px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #0098ff;
}

QPushButton:pressed {
    background-color: #005c99;
}

/* Botones del menú lateral */
QPushButton.MenuButton {
    background-color: transparent;
    color: #cccccc;
    text-align: left;
    padding: 12px 16px;
    border-left: 3px solid transparent;
    border-radius: 0px;
    font-weight: 500;
}

QPushButton.MenuButton:hover {
    background-color: #2a2d2e;
    color: #ffffff;
}

QPushButton.MenuButton:checked {
    background-color: #2a2d2e;
    color: #ffffff;
    border-left: 3px solid #007acc;
}

/* Botones secundarios (ej. Cerrar sesión, cancelar) */
QPushButton.DangerButton {
    background-color: #c53030;
}

QPushButton.DangerButton:hover {
    background-color: #e53e3e;
}

/* Etiquetas */
QLabel {
    background-color: transparent;
}

QLabel.Title {
    font-size: 24px;
    font-weight: bold;
    color: #ffffff;
    padding-bottom: 10px;
}

QLabel.Subtitle {
    font-size: 18px;
    font-weight: 500;
    color: #a0a0a0;
}

/* Frames divisorios o de encabezado */
QFrame.HeaderFrame {
    background-color: #252526;
    border-bottom: 1px solid #333333;
}

/* ScrollAreas */
QScrollArea {
    border: none;
    background-color: transparent;
}
QScrollBar:vertical {
    border: none;
    background-color: #2b2b2b;
    width: 10px;
    margin: 0px 0px 0px 0px;
}
QScrollBar::handle:vertical {
    background-color: #4a4a4a;
    min-height: 20px;
    border-radius: 5px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
}

/* ESTADOS DESHABILITADOS */
QPushButton:disabled, QPushButton.MenuButton:disabled {
    background-color: #333333;
    color: #666666;
    border-left: 3px solid transparent;
}

QPushButton.MenuButton:disabled {
    background-color: transparent;
}

QComboBox {
    background-color: #2b2b2b;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 8px;
    color: #ffffff;
}

QComboBox:disabled {
    background-color: #333333;
    color: #666666;
}

/* Tablas */
QTableWidget {
    background-color: #1e1e1e;
    color: #e0e0e0;
    gridline-color: #333333;
    border: 1px solid #333333;
}
QHeaderView::section {
    background-color: #252526;
    color: #a0a0a0;
    padding: 5px;
    border: 1px solid #333333;
}
"""