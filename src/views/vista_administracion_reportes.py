# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_administracion_reportes.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(471, 339)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 50, 381, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b_r_inventario_administracion_reportes = QPushButton(self.gridLayoutWidget)
        self.b_r_inventario_administracion_reportes.setObjectName(u"b_r_inventario_administracion_reportes")
        self.b_r_inventario_administracion_reportes.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon = QIcon()
        icon.addFile(u"../../images/garage_4398945.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_r_inventario_administracion_reportes.setIcon(icon)
        self.b_r_inventario_administracion_reportes.setIconSize(QSize(80, 80))

        self.verticalLayout.addWidget(self.b_r_inventario_administracion_reportes)

        self.label_r_inventario_administracion_reportes = QLabel(self.gridLayoutWidget)
        self.label_r_inventario_administracion_reportes.setObjectName(u"label_r_inventario_administracion_reportes")

        self.verticalLayout.addWidget(self.label_r_inventario_administracion_reportes)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.b_r_ventas_administracion_reportes = QPushButton(self.gridLayoutWidget)
        self.b_r_ventas_administracion_reportes.setObjectName(u"b_r_ventas_administracion_reportes")
        self.b_r_ventas_administracion_reportes.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon1 = QIcon()
        icon1.addFile(u"../../images/business_16503868.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_r_ventas_administracion_reportes.setIcon(icon1)
        self.b_r_ventas_administracion_reportes.setIconSize(QSize(80, 80))

        self.verticalLayout_3.addWidget(self.b_r_ventas_administracion_reportes)

        self.label_r_ventas_administracion_reportes = QLabel(self.gridLayoutWidget)
        self.label_r_ventas_administracion_reportes.setObjectName(u"label_r_ventas_administracion_reportes")

        self.verticalLayout_3.addWidget(self.label_r_ventas_administracion_reportes)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.b_r_clientes_administracion_reportes = QPushButton(self.gridLayoutWidget)
        self.b_r_clientes_administracion_reportes.setObjectName(u"b_r_clientes_administracion_reportes")
        self.b_r_clientes_administracion_reportes.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon2 = QIcon()
        icon2.addFile(u"../../images/team_18696096.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_r_clientes_administracion_reportes.setIcon(icon2)
        self.b_r_clientes_administracion_reportes.setIconSize(QSize(80, 80))

        self.verticalLayout_2.addWidget(self.b_r_clientes_administracion_reportes)

        self.label_r_clientes_administracion_reportes = QLabel(self.gridLayoutWidget)
        self.label_r_clientes_administracion_reportes.setObjectName(u"label_r_clientes_administracion_reportes")

        self.verticalLayout_2.addWidget(self.label_r_clientes_administracion_reportes)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.b_r_empleados_administracion_reportes = QPushButton(self.gridLayoutWidget)
        self.b_r_empleados_administracion_reportes.setObjectName(u"b_r_empleados_administracion_reportes")
        self.b_r_empleados_administracion_reportes.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon3 = QIcon()
        icon3.addFile(u"../../images/resume_18928734.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_r_empleados_administracion_reportes.setIcon(icon3)
        self.b_r_empleados_administracion_reportes.setIconSize(QSize(80, 80))

        self.verticalLayout_4.addWidget(self.b_r_empleados_administracion_reportes)

        self.label_r_empleados_administracion_reportes = QLabel(self.gridLayoutWidget)
        self.label_r_empleados_administracion_reportes.setObjectName(u"label_r_empleados_administracion_reportes")

        self.verticalLayout_4.addWidget(self.label_r_empleados_administracion_reportes)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b_r_inventario_administracion_reportes.setText("")
        self.label_r_inventario_administracion_reportes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Reporte de inventario </span></p></body></html>", None))
        self.b_r_ventas_administracion_reportes.setText("")
        self.label_r_ventas_administracion_reportes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Reporte de ventas</span></p></body></html>", None))
        self.b_r_clientes_administracion_reportes.setText("")
        self.label_r_clientes_administracion_reportes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Reporte clientes</span></p></body></html>", None))
        self.b_r_empleados_administracion_reportes.setText("")
        self.label_r_empleados_administracion_reportes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Reporte de empleados</span></p></body></html>", None))
    # retranslateUi

