# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_tienda.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(411, 300)
        self.frame_total = QFrame(Form)
        self.frame_total.setObjectName(u"frame_total")
        self.frame_total.setGeometry(QRect(0, 270, 411, 31))
        self.frame_total.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_total.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame_total)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 161, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_total_vista_tienda = QLabel(self.horizontalLayoutWidget)
        self.label_total_vista_tienda.setObjectName(u"label_total_vista_tienda")

        self.horizontalLayout.addWidget(self.label_total_vista_tienda)

        self.label_total_vista_tienda_2 = QLabel(self.horizontalLayoutWidget)
        self.label_total_vista_tienda_2.setObjectName(u"label_total_vista_tienda_2")

        self.horizontalLayout.addWidget(self.label_total_vista_tienda_2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 411, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 409, 269))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 411, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 411, 31))
        self.frame_2.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_venta_vista_tienda = QLabel(self.frame_2)
        self.label_venta_vista_tienda.setObjectName(u"label_venta_vista_tienda")
        self.label_venta_vista_tienda.setGeometry(QRect(0, 0, 91, 31))
        self.label_fechaf_vista_tienda = QLabel(self.frame_2)
        self.label_fechaf_vista_tienda.setObjectName(u"label_fechaf_vista_tienda")
        self.label_fechaf_vista_tienda.setGeometry(QRect(230, 0, 81, 31))
        self.label_fechav_vista_tienda = QLabel(self.frame_2)
        self.label_fechav_vista_tienda.setObjectName(u"label_fechav_vista_tienda")
        self.label_fechav_vista_tienda.setGeometry(QRect(310, 0, 81, 21))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_total_vista_tienda.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">Total:</span></p></body></html>", None))
        self.label_total_vista_tienda_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">TextLabel</span></p></body></html>", None))
        self.label_venta_vista_tienda.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Venta</span></p></body></html>", None))
        self.label_fechaf_vista_tienda.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Fecha:</span></p></body></html>", None))
        self.label_fechav_vista_tienda.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">00/00/0000</span></p></body></html>", None))
    # retranslateUi

