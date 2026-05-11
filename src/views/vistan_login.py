# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vistan_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(579, 300)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(160, 110, 251, 91))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_usuario_login = QLabel(self.verticalLayoutWidget_3)
        self.label_usuario_login.setObjectName(u"label_usuario_login")

        self.verticalLayout.addWidget(self.label_usuario_login)

        self.line_usuario_login = QLineEdit(self.verticalLayoutWidget_3)
        self.line_usuario_login.setObjectName(u"line_usuario_login")

        self.verticalLayout.addWidget(self.line_usuario_login)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_contrasea_login = QLabel(self.verticalLayoutWidget_3)
        self.label_contrasea_login.setObjectName(u"label_contrasea_login")

        self.verticalLayout_2.addWidget(self.label_contrasea_login)

        self.line_contrasea_login = QLineEdit(self.verticalLayoutWidget_3)
        self.line_contrasea_login.setObjectName(u"line_contrasea_login")

        self.verticalLayout_2.addWidget(self.line_contrasea_login)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.label_foto = QLabel(Form)
        self.label_foto.setObjectName(u"label_foto")
        self.label_foto.setGeometry(QRect(240, 50, 91, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_usuario_login.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Usuario</span></p></body></html>", None))
        self.label_contrasea_login.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Contrase\u00f1a</span></p></body></html>", None))
        self.label_foto.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>", None))
    # retranslateUi

