# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_clientes_r.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(471, 302)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.b_guardar_vista_clientes = QPushButton(Form)
        self.b_guardar_vista_clientes.setObjectName(u"b_guardar_vista_clientes")
        self.b_guardar_vista_clientes.setGeometry(QRect(380, 220, 56, 51))
        icon = QIcon()
        icon.addFile(u"../../images/floppy-disk_620785.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_guardar_vista_clientes.setIcon(icon)
        self.b_guardar_vista_clientes.setIconSize(QSize(25, 25))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 471, 31))
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.line_buscar_vista_clientes = QLineEdit(Form)
        self.line_buscar_vista_clientes.setObjectName(u"line_buscar_vista_clientes")
        self.line_buscar_vista_clientes.setGeometry(QRect(300, 40, 113, 21))
        self.b_buscar_vista_clientes = QPushButton(Form)
        self.b_buscar_vista_clientes.setObjectName(u"b_buscar_vista_clientes")
        self.b_buscar_vista_clientes.setGeometry(QRect(420, 30, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"../../images/search_7079548.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_buscar_vista_clientes.setIcon(icon1)
        self.b_buscar_vista_clientes.setIconSize(QSize(18, 18))
        self.b_registrar_vista_clientes = QPushButton(Form)
        self.b_registrar_vista_clientes.setObjectName(u"b_registrar_vista_clientes")
        self.b_registrar_vista_clientes.setGeometry(QRect(30, 40, 71, 31))
        font = QFont()
        font.setPointSize(13)
        self.b_registrar_vista_clientes.setFont(font)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, 120, 191, 166))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre_vista_clientes = QLabel(self.verticalLayoutWidget)
        self.label_nombre_vista_clientes.setObjectName(u"label_nombre_vista_clientes")

        self.verticalLayout.addWidget(self.label_nombre_vista_clientes)

        self.line_nombre_vista_clientes = QLineEdit(self.verticalLayoutWidget)
        self.line_nombre_vista_clientes.setObjectName(u"line_nombre_vista_clientes")

        self.verticalLayout.addWidget(self.line_nombre_vista_clientes)

        self.label_direccion_vista_clientes = QLabel(self.verticalLayoutWidget)
        self.label_direccion_vista_clientes.setObjectName(u"label_direccion_vista_clientes")

        self.verticalLayout.addWidget(self.label_direccion_vista_clientes)

        self.line_direccion_vista_clientes = QLineEdit(self.verticalLayoutWidget)
        self.line_direccion_vista_clientes.setObjectName(u"line_direccion_vista_clientes")

        self.verticalLayout.addWidget(self.line_direccion_vista_clientes)

        self.label_telefono_vista_clientes = QLabel(self.verticalLayoutWidget)
        self.label_telefono_vista_clientes.setObjectName(u"label_telefono_vista_clientes")

        self.verticalLayout.addWidget(self.label_telefono_vista_clientes)

        self.line_telefono = QLineEdit(self.verticalLayoutWidget)
        self.line_telefono.setObjectName(u"line_telefono")

        self.verticalLayout.addWidget(self.line_telefono)

        self.label_estado_vista_clientes = QLabel(self.verticalLayoutWidget)
        self.label_estado_vista_clientes.setObjectName(u"label_estado_vista_clientes")

        self.verticalLayout.addWidget(self.label_estado_vista_clientes)

        self.caja_estado = QComboBox(self.verticalLayoutWidget)
        self.caja_estado.addItem("")
        self.caja_estado.addItem("")
        self.caja_estado.setObjectName(u"caja_estado")

        self.verticalLayout.addWidget(self.caja_estado)

        self.label_buscar_vista_clientes = QLabel(Form)
        self.label_buscar_vista_clientes.setObjectName(u"label_buscar_vista_clientes")
        self.label_buscar_vista_clientes.setGeometry(QRect(240, 40, 51, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b_guardar_vista_clientes.setText("")
        self.b_buscar_vista_clientes.setText("")
        self.b_registrar_vista_clientes.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.label_nombre_vista_clientes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nombre</span></p></body></html>", None))
        self.label_direccion_vista_clientes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Direccion</span></p></body></html>", None))
        self.label_telefono_vista_clientes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Telefono</span></p></body></html>", None))
        self.label_estado_vista_clientes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Estado</span></p></body></html>", None))
        self.caja_estado.setItemText(0, QCoreApplication.translate("Form", u"Activo", None))
        self.caja_estado.setItemText(1, QCoreApplication.translate("Form", u"Inactivo", None))

        self.label_buscar_vista_clientes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Buscar:</span></p></body></html>", None))
    # retranslateUi

