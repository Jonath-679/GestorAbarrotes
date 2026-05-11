# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 593)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_bienvenido_mainwindow = QLabel(self.centralwidget)
        self.label_bienvenido_mainwindow.setObjectName(u"label_bienvenido_mainwindow")
        self.label_bienvenido_mainwindow.setGeometry(QRect(10, 20, 181, 51))
        self.label_bienvenido_mainwindow.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.b_cerrar_sesion_mainwindow = QPushButton(self.centralwidget)
        self.b_cerrar_sesion_mainwindow.setObjectName(u"b_cerrar_sesion_mainwindow")
        self.b_cerrar_sesion_mainwindow.setGeometry(QRect(10, 430, 141, 51))
        font = QFont()
        font.setPointSize(15)
        self.b_cerrar_sesion_mainwindow.setFont(font)
        self.b_cerrar_sesion_mainwindow.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        icon = QIcon()
        icon.addFile(u"../../images/left-direction_81935.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_cerrar_sesion_mainwindow.setIcon(icon)
        self.b_cerrar_sesion_mainwindow.setIconSize(QSize(23, 23))
        self.frame_barra = QFrame(self.centralwidget)
        self.frame_barra.setObjectName(u"frame_barra")
        self.frame_barra.setGeometry(QRect(210, 0, 771, 51))
        self.frame_barra.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_barra.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_barra.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 60, 721, 501))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 211, 501))
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 80, 211, 192))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.b_administracion_mainwindow = QPushButton(self.verticalLayoutWidget)
        self.b_administracion_mainwindow.setObjectName(u"b_administracion_mainwindow")
        self.b_administracion_mainwindow.setFont(font)
        self.b_administracion_mainwindow.setStyleSheet(u"background-color: rgb(142, 142, 142);")
        icon1 = QIcon()
        icon1.addFile(u"../../images/setting_7874339.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_administracion_mainwindow.setIcon(icon1)
        self.b_administracion_mainwindow.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.b_administracion_mainwindow)

        self.b_tienda_mainwindow = QPushButton(self.verticalLayoutWidget)
        self.b_tienda_mainwindow.setObjectName(u"b_tienda_mainwindow")
        self.b_tienda_mainwindow.setFont(font)
        self.b_tienda_mainwindow.setStyleSheet(u"background-color: rgb(142, 142, 142);")
        icon2 = QIcon()
        icon2.addFile(u"../../images/paper-bag_8949159.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_tienda_mainwindow.setIcon(icon2)
        self.b_tienda_mainwindow.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.b_tienda_mainwindow)

        self.b_clientes_mainwindow = QPushButton(self.verticalLayoutWidget)
        self.b_clientes_mainwindow.setObjectName(u"b_clientes_mainwindow")
        self.b_clientes_mainwindow.setFont(font)
        self.b_clientes_mainwindow.setStyleSheet(u"background-color: rgb(142, 142, 142);")
        icon3 = QIcon()
        icon3.addFile(u"../../images/people_18006202.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_clientes_mainwindow.setIcon(icon3)
        self.b_clientes_mainwindow.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.b_clientes_mainwindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_barra.raise_()
        self.stackedWidget.raise_()
        self.frame.raise_()
        self.b_cerrar_sesion_mainwindow.raise_()
        self.label_bienvenido_mainwindow.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_bienvenido_mainwindow.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Bienvenido</span></p></body></html>", None))
        self.b_cerrar_sesion_mainwindow.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
        self.b_administracion_mainwindow.setText(QCoreApplication.translate("MainWindow", u"Adminstracion", None))
        self.b_tienda_mainwindow.setText(QCoreApplication.translate("MainWindow", u"Tienda", None))
        self.b_clientes_mainwindow.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
    # retranslateUi

