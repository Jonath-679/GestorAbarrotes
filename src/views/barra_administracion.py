# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barra_administracion.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(424, 53)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 431, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.b_empleados_barra_administracion = QPushButton(self.horizontalLayoutWidget)
        self.b_empleados_barra_administracion.setObjectName(u"b_empleados_barra_administracion")
        font = QFont()
        font.setPointSize(10)
        self.b_empleados_barra_administracion.setFont(font)

        self.horizontalLayout.addWidget(self.b_empleados_barra_administracion)

        self.b_reportes_barra_administracion = QPushButton(self.horizontalLayoutWidget)
        self.b_reportes_barra_administracion.setObjectName(u"b_reportes_barra_administracion")
        self.b_reportes_barra_administracion.setFont(font)

        self.horizontalLayout.addWidget(self.b_reportes_barra_administracion)

        self.b_inventario_barra_administracion = QPushButton(self.horizontalLayoutWidget)
        self.b_inventario_barra_administracion.setObjectName(u"b_inventario_barra_administracion")
        self.b_inventario_barra_administracion.setFont(font)

        self.horizontalLayout.addWidget(self.b_inventario_barra_administracion)

        self.b_proveedores_barra_administracion = QPushButton(self.horizontalLayoutWidget)
        self.b_proveedores_barra_administracion.setObjectName(u"b_proveedores_barra_administracion")
        self.b_proveedores_barra_administracion.setFont(font)

        self.horizontalLayout.addWidget(self.b_proveedores_barra_administracion)

        self.b_historial_barra_administracion = QPushButton(self.horizontalLayoutWidget)
        self.b_historial_barra_administracion.setObjectName(u"b_historial_barra_administracion")
        self.b_historial_barra_administracion.setFont(font)

        self.horizontalLayout.addWidget(self.b_historial_barra_administracion)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b_empleados_barra_administracion.setText(QCoreApplication.translate("Form", u"Empleados", None))
        self.b_reportes_barra_administracion.setText(QCoreApplication.translate("Form", u"Reportes", None))
        self.b_inventario_barra_administracion.setText(QCoreApplication.translate("Form", u"Inventario", None))
        self.b_proveedores_barra_administracion.setText(QCoreApplication.translate("Form", u"Proveedores", None))
        self.b_historial_barra_administracion.setText(QCoreApplication.translate("Form", u"Historial", None))
    # retranslateUi

