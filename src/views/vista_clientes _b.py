# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_clientes _b.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(481, 464)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 471, 31))
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.line_buscar = QLineEdit(Form)
        self.line_buscar.setObjectName(u"line_buscar")
        self.line_buscar.setGeometry(QRect(300, 40, 113, 21))
        self.b_buscar = QPushButton(Form)
        self.b_buscar.setObjectName(u"b_buscar")
        self.b_buscar.setGeometry(QRect(420, 30, 31, 31))
        icon = QIcon()
        icon.addFile(u"../../images/search_7079548.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_buscar.setIcon(icon)
        self.b_buscar.setIconSize(QSize(18, 18))
        self.b_registrar = QPushButton(Form)
        self.b_registrar.setObjectName(u"b_registrar")
        self.b_registrar.setGeometry(QRect(30, 40, 71, 31))
        font = QFont()
        font.setPointSize(13)
        self.b_registrar.setFont(font)
        self.label_buscar = QLabel(Form)
        self.label_buscar.setObjectName(u"label_buscar")
        self.label_buscar.setGeometry(QRect(240, 40, 51, 16))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 220, 471, 201))
        self.frame_2.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 80, 481, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.b_buscar.setText("")
        self.b_registrar.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.label_buscar.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Buscar:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Nombre</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Direccion</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Telefono</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Estado</span></p></body></html>", None))
    # retranslateUi

