# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenEreWZu.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import icon_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(800, 600)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(70, 60, 660, 380))
        self.main_frame.setStyleSheet(u"QFrame {\n"
"	border: 2px solid rgb(156, 156, 156);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
" 	\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.main_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 290, 581, 31))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.517, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.loading_label = QLabel(self.main_frame)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setGeometry(QRect(10, 320, 641, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.loading_label.setFont(font)
        self.loading_label.setLayoutDirection(Qt.LeftToRight)
        self.loading_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(98, 114, 164);\n"
"	border: none\n"
"}")
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.logo_frame = QFrame(self.main_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(130, 50, 371, 121))
        self.logo_frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	image: url(eduneering_logo2.png);\n"
"	border: none\n"
"}")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.version_label = QLabel(self.main_frame)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(10, 350, 641, 20))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.version_label.setFont(font1)
        self.version_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(125, 125, 125);\n"
"	border: none;\n"
"}\n"
"")
        self.version_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.info_label = QLabel(self.main_frame)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(10, 200, 641, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(True)
        self.info_label.setFont(font2)
        self.info_label.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.info_label.setAlignment(Qt.AlignCenter)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.loading_label.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.version_label.setText(QCoreApplication.translate("SplashScreen", u"Version 0.1.2", None))
        self.info_label.setText(QCoreApplication.translate("SplashScreen", u"G\u00f6r\u00fcnt\u00fc \u0130\u015flemeli \u00c7ekme Deney D\u00fczene\u011fi", None))
    # retranslateUi

