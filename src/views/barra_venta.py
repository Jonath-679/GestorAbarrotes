# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barra_venta.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(451, 230)
        self.frame_de_barra = QFrame(Form)
        self.frame_de_barra.setObjectName(u"frame_de_barra")
        self.frame_de_barra.setGeometry(QRect(0, 30, 451, 61))
        self.frame_de_barra.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_de_barra.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_de_barra.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame_de_barra)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 140, 48))
        self.layou_botones = QHBoxLayout(self.horizontalLayoutWidget)
        self.layou_botones.setObjectName(u"layou_botones")
        self.layou_botones.setContentsMargins(0, 0, 0, 0)
        self.b_agruegar_producto_barra_ventana = QPushButton(self.horizontalLayoutWidget)
        self.b_agruegar_producto_barra_ventana.setObjectName(u"b_agruegar_producto_barra_ventana")
        self.b_agruegar_producto_barra_ventana.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon = QIcon()
        icon.addFile(u"../../images/add_11546776.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_agruegar_producto_barra_ventana.setIcon(icon)
        self.b_agruegar_producto_barra_ventana.setIconSize(QSize(40, 40))

        self.layou_botones.addWidget(self.b_agruegar_producto_barra_ventana)

        self.b_eliminar_producto_barra_ventana = QPushButton(self.horizontalLayoutWidget)
        self.b_eliminar_producto_barra_ventana.setObjectName(u"b_eliminar_producto_barra_ventana")
        self.b_eliminar_producto_barra_ventana.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon1 = QIcon()
        icon1.addFile(u"../../images/bin_18007458.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_eliminar_producto_barra_ventana.setIcon(icon1)
        self.b_eliminar_producto_barra_ventana.setIconSize(QSize(35, 35))

        self.layou_botones.addWidget(self.b_eliminar_producto_barra_ventana)

        self.label_costof_barra_ventana = QLabel(self.frame_de_barra)
        self.label_costof_barra_ventana.setObjectName(u"label_costof_barra_ventana")
        self.label_costof_barra_ventana.setGeometry(QRect(280, 20, 51, 21))
        self.label_nombre_barra_ventana = QLabel(self.frame_de_barra)
        self.label_nombre_barra_ventana.setObjectName(u"label_nombre_barra_ventana")
        self.label_nombre_barra_ventana.setGeometry(QRect(150, 20, 61, 21))
        self.label_costov_barra_ventana = QLabel(self.frame_de_barra)
        self.label_costov_barra_ventana.setObjectName(u"label_costov_barra_ventana")
        self.label_costov_barra_ventana.setGeometry(QRect(340, 20, 61, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b_agruegar_producto_barra_ventana.setText("")
        self.b_eliminar_producto_barra_ventana.setText("")
        self.label_costof_barra_ventana.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Costo:</span></p></body></html>", None))
        self.label_nombre_barra_ventana.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>", None))
        self.label_costov_barra_ventana.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>", None))
    # retranslateUi

