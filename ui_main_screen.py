# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screenqOFOrO.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 637)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(20, 10, 903, 600))
        self.main_frame.setMinimumSize(QSize(800, 600))
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_tabWidget = QTabWidget(self.main_frame)
        self.main_tabWidget.setObjectName(u"main_tabWidget")
        self.main_tabWidget.setStyleSheet(u"QTabWidget::Pane{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::Tab{\n"
"	min-width: 100px;\n"
"	min-height: 25px;\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	margin-left: 3px;\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"QTabBar::Tab:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.499682, y1:0, x2:0.5, y2:1, stop:0 rgba(124, 124, 124, 150), stop:1 rgba(206, 206, 206, 255));\n"
"}\n"
"\n"
"QTabBar::Tab:pressed{\n"
"	border: 2px solid rgb(80, 80, 80);\n"
"}")
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.verticalLayout_5 = QVBoxLayout(self.tab_config)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_config_top = QFrame(self.tab_config)
        self.frame_config_top.setObjectName(u"frame_config_top")
        self.frame_config_top.setMinimumSize(QSize(0, 30))
        self.frame_config_top.setMaximumSize(QSize(16777215, 30))
        self.frame_config_top.setFrameShape(QFrame.StyledPanel)
        self.frame_config_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_config_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(670, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.button_minimize_1 = QPushButton(self.frame_config_top)
        self.button_minimize_1.setObjectName(u"button_minimize_1")
        self.button_minimize_1.setMinimumSize(QSize(20, 20))
        self.button_minimize_1.setMaximumSize(QSize(20, 20))
        self.button_minimize_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	image: url(minimize.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_minimize_1)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.button_restore_1 = QPushButton(self.frame_config_top)
        self.button_restore_1.setObjectName(u"button_restore_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_restore_1.sizePolicy().hasHeightForWidth())
        self.button_restore_1.setSizePolicy(sizePolicy)
        self.button_restore_1.setMinimumSize(QSize(20, 20))
        self.button_restore_1.setMaximumSize(QSize(20, 20))
        self.button_restore_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"QPushButton::hover{	\n"
"	image: url(maximize.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_restore_1)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.button_exit_1 = QPushButton(self.frame_config_top)
        self.button_exit_1.setObjectName(u"button_exit_1")
        self.button_exit_1.setMinimumSize(QSize(20, 20))
        self.button_exit_1.setMaximumSize(QSize(20, 20))
        self.button_exit_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{	\n"
"	image: url(close.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_exit_1)

        self.horizontalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addWidget(self.frame_config_top)

        self.frame_config_center = QFrame(self.tab_config)
        self.frame_config_center.setObjectName(u"frame_config_center")
        self.frame_config_center.setStyleSheet(u"")
        self.frame_config_center.setFrameShape(QFrame.StyledPanel)
        self.frame_config_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_config_center)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_config_left = QFrame(self.frame_config_center)
        self.frame_config_left.setObjectName(u"frame_config_left")
        self.frame_config_left.setFrameShape(QFrame.StyledPanel)
        self.frame_config_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_config_left)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.label_ = QLabel(self.frame_config_left)
        self.label_.setObjectName(u"label_")
        self.label_.setMinimumSize(QSize(0, 20))
        self.label_.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_.setFont(font)
        self.label_.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_)

        self.label_camera_1 = QLabel(self.frame_config_left)
        self.label_camera_1.setObjectName(u"label_camera_1")
        self.label_camera_1.setMinimumSize(QSize(390, 250))
        self.label_camera_1.setMaximumSize(QSize(16777215, 250))
        self.label_camera_1.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_camera_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_camera_1)

        self.grid_slider = QGridLayout()
        self.grid_slider.setObjectName(u"grid_slider")
        self.grid_slider.setHorizontalSpacing(10)
        self.grid_slider.setVerticalSpacing(0)
        self.label_s_min = QLabel(self.frame_config_left)
        self.label_s_min.setObjectName(u"label_s_min")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_s_min.setFont(font1)
        self.label_s_min.setStyleSheet(u"QLabel{\n"
"	margin-left: 5px;\n"
"}")

        self.grid_slider.addWidget(self.label_s_min, 4, 0, 1, 1)

        self.label_s_max = QLabel(self.frame_config_left)
        self.label_s_max.setObjectName(u"label_s_max")
        self.label_s_max.setFont(font1)
        self.label_s_max.setStyleSheet(u"QLabel{\n"
"	margin-left: 5px;\n"
"}")

        self.grid_slider.addWidget(self.label_s_max, 1, 0, 1, 1)

        self.slider_s_max = QSlider(self.frame_config_left)
        self.slider_s_max.setObjectName(u"slider_s_max")
        self.slider_s_max.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 0px solid #424242; \n"
"	height: 3px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 2px solid rgb(176, 176, 176);\n"
"	width: 16px; \n"
"	height: 5px; \n"
"	line-height: 5px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"		background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.slider_s_max.setMaximum(255)
        self.slider_s_max.setValue(255)
        self.slider_s_max.setOrientation(Qt.Horizontal)

        self.grid_slider.addWidget(self.slider_s_max, 1, 1, 1, 1)

        self.label_v_min = QLabel(self.frame_config_left)
        self.label_v_min.setObjectName(u"label_v_min")
        self.label_v_min.setFont(font1)
        self.label_v_min.setStyleSheet(u"QLabel{\n"
"	margin-left: 5px;\n"
"}")

        self.grid_slider.addWidget(self.label_v_min, 5, 0, 1, 1)

        self.slider_h_max = QSlider(self.frame_config_left)
        self.slider_h_max.setObjectName(u"slider_h_max")
        self.slider_h_max.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 0px solid #424242; \n"
"	height: 3px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 2px solid rgb(176, 176, 176);\n"
"	width: 16px; \n"
"	height: 5px; \n"
"	line-height: 5px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"		background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.slider_h_max.setMaximum(179)
        self.slider_h_max.setValue(179)
        self.slider_h_max.setOrientation(Qt.Horizontal)

        self.grid_slider.addWidget(self.slider_h_max, 0, 1, 1, 1)

        self.slider_v_max = QSlider(self.frame_config_left)
        self.slider_v_max.setObjectName(u"slider_v_max")
        self.slider_v_max.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 0px solid #424242; \n"
"	height: 3px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 2px solid rgb(176, 176, 176);\n"
"	width: 16px; \n"
"	height: 5px; \n"
"	line-height: 5px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"		background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.slider_v_max.setMaximum(255)
        self.slider_v_max.setValue(255)
        self.slider_v_max.setOrientation(Qt.Horizontal)

        self.grid_slider.addWidget(self.slider_v_max, 2, 1, 1, 1)

        self.label_v_max = QLabel(self.frame_config_left)
        self.label_v_max.setObjectName(u"label_v_max")
        self.label_v_max.setFont(font1)
        self.label_v_max.setStyleSheet(u"QLabel{\n"
"	margin-left: 5px;\n"
"}")

        self.grid_slider.addWidget(self.label_v_max, 2, 0, 1, 1)

        self.label_h_max = QLabel(self.frame_config_left)
        self.label_h_max.setObjectName(u"label_h_max")
        self.label_h_max.setFont(font1)
        self.label_h_max.setStyleSheet(u"QLabel{\n"
"	margin-left: 5px;\n"
"}")

        self.grid_slider.addWidget(self.label_h_max, 0, 0, 1, 1)

        self.slider_s_min = QSlider(self.frame_config_left)
        self.slider_s_min.setObjectName(u"slider_s_min")
        self.slider_s_min.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 0px solid #424242; \n"
"	height: 3px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 2px solid rgb(176, 176, 176);\n"
"	width: 16px; \n"
"	height: 5px; \n"
"	line-height: 5px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"		background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.slider_s_min.setMaximum(255)
        self.slider_s_min.setOrientation(Qt.Horizontal)

        self.grid_slider.addWidget(self.slider_s_min, 4, 1, 1, 1)

        self.slider_h_min = QSlider(self.frame_config_left)
        self.slider_h_min.setObjectName(u"slider_h_min")
        self.slider_h_min.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 0px solid #424242; \n"
"	height: 3px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 2px solid rgb(176, 176, 176);\n"
"	width: 16px; \n"
"	height: 5px; \n"
"	line-height: 5px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"		background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.slider_h_min.setMaximum(179)
        self.slider_h_min.setOrientation(Qt.Horizontal)

        self.grid_slider.addWidget(self.slider_h_min, 3, 1, 1, 1)

        self.slider_v_min = QSlider(self.frame_config_left)
        self.slider_v_min.setObjectName(u"slider_v_min")
        self.slider_v_min.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 0px solid #424242; \n"
"	height: 3px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(176, 176, 176);\n"
"	border: 2px solid rgb(176, 176, 176);\n"
"	width: 16px; \n"
"	height: 5px; \n"
"	line-height: 5px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"		background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.slider_v_min.setMaximum(255)
        self.slider_v_min.setOrientation(Qt.Horizontal)

        self.grid_slider.addWidget(self.slider_v_min, 5, 1, 1, 1)

        self.label_h_min = QLabel(self.frame_config_left)
        self.label_h_min.setObjectName(u"label_h_min")
        self.label_h_min.setFont(font1)
        self.label_h_min.setStyleSheet(u"QLabel{\n"
"	margin-left: 5px;\n"
"}")

        self.grid_slider.addWidget(self.label_h_min, 3, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.grid_slider)

        self.layout_checkbox = QHBoxLayout()
        self.layout_checkbox.setObjectName(u"layout_checkbox")
        self.layout_checkbox.setContentsMargins(10, -1, -1, -1)
        self.checkBox_safety = QCheckBox(self.frame_config_left)
        self.checkBox_safety.setObjectName(u"checkBox_safety")
        self.checkBox_safety.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border: 2px solid rgb(20, 107, 17);\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(check.png);\n"
"}")

        self.layout_checkbox.addWidget(self.checkBox_safety)

        self.checkBox_secure = QCheckBox(self.frame_config_left)
        self.checkBox_secure.setObjectName(u"checkBox_secure")
        self.checkBox_secure.setStyleSheet(u"QCheckBox::indicator{\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border: 2px solid rgb(20, 107, 17);\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(check.png);\n"
"}")

        self.layout_checkbox.addWidget(self.checkBox_secure)


        self.verticalLayout_3.addLayout(self.layout_checkbox)


        self.horizontalLayout.addWidget(self.frame_config_left)

        self.frame_config_right = QFrame(self.frame_config_center)
        self.frame_config_right.setObjectName(u"frame_config_right")
        self.frame_config_right.setFrameShape(QFrame.StyledPanel)
        self.frame_config_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_config_right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_instructions = QLabel(self.frame_config_right)
        self.label_instructions.setObjectName(u"label_instructions")
        self.label_instructions.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_instructions.setFont(font2)
        self.label_instructions.setTextFormat(Qt.AutoText)
        self.label_instructions.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.label_instructions)

        self.grid_button_config_1 = QGridLayout()
        self.grid_button_config_1.setSpacing(10)
        self.grid_button_config_1.setObjectName(u"grid_button_config_1")
        self.button_weight = QPushButton(self.frame_config_right)
        self.button_weight.setObjectName(u"button_weight")
        self.button_weight.setMinimumSize(QSize(175, 100))
        self.button_weight.setMaximumSize(QSize(175, 100))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.button_weight.setFont(font3)
        self.button_weight.setAcceptDrops(False)
        self.button_weight.setAutoFillBackground(False)
        self.button_weight.setStyleSheet(u"QPushButton{\n"
"	border-margin: 5px;\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-radius: 10px;\n"
"	color: rgb(72, 82, 108);\n"
"	\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(197, 197, 197, 255), stop:1 rgba(225, 225, 225, 255));\n"
"}")
        self.button_weight.setCheckable(False)

        self.grid_button_config_1.addWidget(self.button_weight, 0, 0, 1, 1)

        self.button_measure = QPushButton(self.frame_config_right)
        self.button_measure.setObjectName(u"button_measure")
        self.button_measure.setMinimumSize(QSize(175, 100))
        self.button_measure.setMaximumSize(QSize(175, 100))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.button_measure.setFont(font4)
        self.button_measure.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-radius: 10px;\n"
"	color: rgb(72, 82, 108);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(197, 197, 197, 255), stop:1 rgba(225, 225, 225, 255));\n"
"}")

        self.grid_button_config_1.addWidget(self.button_measure, 0, 1, 1, 1)

        self.button_image = QPushButton(self.frame_config_right)
        self.button_image.setObjectName(u"button_image")
        self.button_image.setMinimumSize(QSize(175, 100))
        self.button_image.setMaximumSize(QSize(16777215, 100))
        self.button_image.setFont(font4)
        self.button_image.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-radius: 10px;\n"
"	color: rgb(72, 82, 108);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(197, 197, 197, 255), stop:1 rgba(225, 225, 225, 255));\n"
"}")

        self.grid_button_config_1.addWidget(self.button_image, 1, 0, 1, 1)

        self.button_activate = QPushButton(self.frame_config_right)
        self.button_activate.setObjectName(u"button_activate")
        self.button_activate.setMinimumSize(QSize(175, 100))
        self.button_activate.setMaximumSize(QSize(175, 100))
        self.button_activate.setFont(font4)
        self.button_activate.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-radius: 10px;\n"
"	color: rgb(72, 82, 108);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(197, 197, 197, 255), stop:1 rgba(225, 225, 225, 255));\n"
"}")

        self.grid_button_config_1.addWidget(self.button_activate, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.grid_button_config_1)

        self.grid_button_config_2 = QGridLayout()
        self.grid_button_config_2.setObjectName(u"grid_button_config_2")
        self.label_spec_standart = QLabel(self.frame_config_right)
        self.label_spec_standart.setObjectName(u"label_spec_standart")
        self.label_spec_standart.setMinimumSize(QSize(0, 20))
        self.label_spec_standart.setMaximumSize(QSize(16777215, 20))
        self.label_spec_standart.setFont(font1)
        self.label_spec_standart.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_button_config_2.addWidget(self.label_spec_standart, 4, 0, 1, 1)

        self.label_material = QLabel(self.frame_config_right)
        self.label_material.setObjectName(u"label_material")
        self.label_material.setMinimumSize(QSize(0, 22))
        self.label_material.setMaximumSize(QSize(16777215, 22))
        self.label_material.setFont(font1)
        self.label_material.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_button_config_2.addWidget(self.label_material, 0, 0, 1, 1)

        self.button_test_standart = QPushButton(self.frame_config_right)
        self.button_test_standart.setObjectName(u"button_test_standart")
        self.button_test_standart.setMinimumSize(QSize(80, 25))
        self.button_test_standart.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_button_config_2.addWidget(self.button_test_standart, 3, 1, 1, 1)

        self.lineEdit_spec_standart = QLineEdit(self.frame_config_right)
        self.lineEdit_spec_standart.setObjectName(u"lineEdit_spec_standart")
        self.lineEdit_spec_standart.setMinimumSize(QSize(0, 25))
        self.lineEdit_spec_standart.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_button_config_2.addWidget(self.lineEdit_spec_standart, 5, 0, 1, 1)

        self.button_material = QPushButton(self.frame_config_right)
        self.button_material.setObjectName(u"button_material")
        self.button_material.setMinimumSize(QSize(80, 25))
        self.button_material.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_button_config_2.addWidget(self.button_material, 1, 1, 1, 1)

        self.label_test_standart = QLabel(self.frame_config_right)
        self.label_test_standart.setObjectName(u"label_test_standart")
        self.label_test_standart.setMinimumSize(QSize(0, 22))
        self.label_test_standart.setMaximumSize(QSize(16777215, 22))
        self.label_test_standart.setFont(font1)
        self.label_test_standart.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_button_config_2.addWidget(self.label_test_standart, 2, 0, 1, 1)

        self.button_spec_standart = QPushButton(self.frame_config_right)
        self.button_spec_standart.setObjectName(u"button_spec_standart")
        self.button_spec_standart.setMinimumSize(QSize(80, 25))
        self.button_spec_standart.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_button_config_2.addWidget(self.button_spec_standart, 5, 1, 1, 1)

        self.lineEdit_material = QLineEdit(self.frame_config_right)
        self.lineEdit_material.setObjectName(u"lineEdit_material")
        self.lineEdit_material.setMinimumSize(QSize(0, 25))
        self.lineEdit_material.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_button_config_2.addWidget(self.lineEdit_material, 1, 0, 1, 1)

        self.lineEdit_test_standart = QLineEdit(self.frame_config_right)
        self.lineEdit_test_standart.setObjectName(u"lineEdit_test_standart")
        self.lineEdit_test_standart.setMinimumSize(QSize(0, 25))
        self.lineEdit_test_standart.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_button_config_2.addWidget(self.lineEdit_test_standart, 3, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.grid_button_config_2)


        self.horizontalLayout.addWidget(self.frame_config_right)


        self.verticalLayout_5.addWidget(self.frame_config_center)

        self.frame_config_bottom = QFrame(self.tab_config)
        self.frame_config_bottom.setObjectName(u"frame_config_bottom")
        self.frame_config_bottom.setMinimumSize(QSize(50, 35))
        self.frame_config_bottom.setMaximumSize(QSize(16777215, 35))
        self.frame_config_bottom.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_config_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_config_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_config_bottom)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.label_name_1 = QLabel(self.frame_config_bottom)
        self.label_name_1.setObjectName(u"label_name_1")

        self.horizontalLayout_3.addWidget(self.label_name_1)

        self.horizontalSpacer = QSpacerItem(599, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.button_next_1 = QPushButton(self.frame_config_bottom)
        self.button_next_1.setObjectName(u"button_next_1")
        self.button_next_1.setMinimumSize(QSize(80, 25))
        self.button_next_1.setLayoutDirection(Qt.LeftToRight)
        self.button_next_1.setAutoFillBackground(False)
        self.button_next_1.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border: 1px solid rgb(67, 67, 67);\n"
"\n"
"}")
        self.button_next_1.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.button_next_1)

        self.frame_3 = QFrame(self.frame_config_bottom)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(5, 5))
        self.frame_3.setMaximumSize(QSize(5, 5))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame_config_bottom)

        self.main_tabWidget.addTab(self.tab_config, "")
        self.tab_analysis = QWidget()
        self.tab_analysis.setObjectName(u"tab_analysis")
        self.verticalLayout_6 = QVBoxLayout(self.tab_analysis)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_analysis_top = QFrame(self.tab_analysis)
        self.frame_analysis_top.setObjectName(u"frame_analysis_top")
        self.frame_analysis_top.setMinimumSize(QSize(0, 30))
        self.frame_analysis_top.setMaximumSize(QSize(16777215, 30))
        self.frame_analysis_top.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_analysis_top)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(670, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.button_minimize_2 = QPushButton(self.frame_analysis_top)
        self.button_minimize_2.setObjectName(u"button_minimize_2")
        self.button_minimize_2.setMinimumSize(QSize(20, 20))
        self.button_minimize_2.setMaximumSize(QSize(20, 20))
        self.button_minimize_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	image: url(minimize.png);\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_minimize_2)

        self.horizontalSpacer_13 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.button_restore_2 = QPushButton(self.frame_analysis_top)
        self.button_restore_2.setObjectName(u"button_restore_2")
        self.button_restore_2.setMinimumSize(QSize(20, 20))
        self.button_restore_2.setMaximumSize(QSize(20, 20))
        self.button_restore_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"QPushButton::hover{	\n"
"	image: url(maximize.png);\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_restore_2)

        self.horizontalSpacer_14 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.button_exit_2 = QPushButton(self.frame_analysis_top)
        self.button_exit_2.setObjectName(u"button_exit_2")
        self.button_exit_2.setMinimumSize(QSize(20, 20))
        self.button_exit_2.setMaximumSize(QSize(20, 20))
        self.button_exit_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{	\n"
"	image: url(close.png);\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_exit_2)

        self.horizontalSpacer_15 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)


        self.verticalLayout_6.addWidget(self.frame_analysis_top)

        self.frame_analysis_center = QFrame(self.tab_analysis)
        self.frame_analysis_center.setObjectName(u"frame_analysis_center")
        self.frame_analysis_center.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_analysis_center)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_analysis_left = QFrame(self.frame_analysis_center)
        self.frame_analysis_left.setObjectName(u"frame_analysis_left")
        self.frame_analysis_left.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_analysis_left)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layout_label_2 = QHBoxLayout()
        self.layout_label_2.setObjectName(u"layout_label_2")
        self.label_stress_strain = QLabel(self.frame_analysis_left)
        self.label_stress_strain.setObjectName(u"label_stress_strain")
        self.label_stress_strain.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_stress_strain.setFont(font5)

        self.layout_label_2.addWidget(self.label_stress_strain)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_label_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_8.addLayout(self.layout_label_2)

        self.layout_chart_camera = QHBoxLayout()
        self.layout_chart_camera.setObjectName(u"layout_chart_camera")
        self.frame_chart = QFrame(self.frame_analysis_left)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setMinimumSize(QSize(300, 250))
        self.frame_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_chart)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widgetChart = QWidget(self.frame_chart)
        self.widgetChart.setObjectName(u"widgetChart")

        self.horizontalLayout_2.addWidget(self.widgetChart)


        self.layout_chart_camera.addWidget(self.frame_chart)

        self.label_camera_2 = QLabel(self.frame_analysis_left)
        self.label_camera_2.setObjectName(u"label_camera_2")
        self.label_camera_2.setMinimumSize(QSize(175, 250))
        self.label_camera_2.setMaximumSize(QSize(175, 250))
        self.label_camera_2.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_camera_2.setAlignment(Qt.AlignCenter)

        self.layout_chart_camera.addWidget(self.label_camera_2)


        self.verticalLayout_8.addLayout(self.layout_chart_camera)

        self.grid_button_analysis = QGridLayout()
        self.grid_button_analysis.setObjectName(u"grid_button_analysis")
        self.grid_button_analysis.setVerticalSpacing(0)
        self.label_add_graph_1 = QLabel(self.frame_analysis_left)
        self.label_add_graph_1.setObjectName(u"label_add_graph_1")
        self.label_add_graph_1.setMinimumSize(QSize(0, 22))
        self.label_add_graph_1.setMaximumSize(QSize(16777215, 22))
        self.label_add_graph_1.setFont(font1)

        self.grid_button_analysis.addWidget(self.label_add_graph_1, 0, 0, 1, 1)

        self.label_add_graph_3 = QLabel(self.frame_analysis_left)
        self.label_add_graph_3.setObjectName(u"label_add_graph_3")
        self.label_add_graph_3.setMinimumSize(QSize(0, 22))
        self.label_add_graph_3.setMaximumSize(QSize(16777215, 22))
        self.label_add_graph_3.setFont(font1)

        self.grid_button_analysis.addWidget(self.label_add_graph_3, 6, 0, 1, 1)

        self.lineEdit_add_graph_1 = QLineEdit(self.frame_analysis_left)
        self.lineEdit_add_graph_1.setObjectName(u"lineEdit_add_graph_1")
        self.lineEdit_add_graph_1.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_graph_1.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_button_analysis.addWidget(self.lineEdit_add_graph_1, 1, 0, 1, 1)

        self.label_add_graph_2 = QLabel(self.frame_analysis_left)
        self.label_add_graph_2.setObjectName(u"label_add_graph_2")
        self.label_add_graph_2.setMinimumSize(QSize(0, 22))
        self.label_add_graph_2.setMaximumSize(QSize(16777215, 22))
        self.label_add_graph_2.setFont(font1)

        self.grid_button_analysis.addWidget(self.label_add_graph_2, 2, 0, 1, 1)

        self.button_graph_browse_1 = QPushButton(self.frame_analysis_left)
        self.button_graph_browse_1.setObjectName(u"button_graph_browse_1")
        self.button_graph_browse_1.setMinimumSize(QSize(80, 25))
        self.button_graph_browse_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_button_analysis.addWidget(self.button_graph_browse_1, 1, 1, 1, 1)

        self.button_graph_remove_2 = QPushButton(self.frame_analysis_left)
        self.button_graph_remove_2.setObjectName(u"button_graph_remove_2")
        self.button_graph_remove_2.setMinimumSize(QSize(80, 25))
        self.button_graph_remove_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(238, 75, 115);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{	\n"
"	background-color: qlineargradient(spread:pad, x1:0.511, y1:0.00568182, x2:0.511, y2:1, stop:0 rgba(230, 80, 115, 255), stop:1 rgba(242, 230, 230, 255));\n"
"}")

        self.grid_button_analysis.addWidget(self.button_graph_remove_2, 3, 2, 1, 1)

        self.button_graph_browse_2 = QPushButton(self.frame_analysis_left)
        self.button_graph_browse_2.setObjectName(u"button_graph_browse_2")
        self.button_graph_browse_2.setMinimumSize(QSize(80, 25))
        self.button_graph_browse_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_button_analysis.addWidget(self.button_graph_browse_2, 3, 1, 1, 1)

        self.lineEdit_add_graph_2 = QLineEdit(self.frame_analysis_left)
        self.lineEdit_add_graph_2.setObjectName(u"lineEdit_add_graph_2")
        self.lineEdit_add_graph_2.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_graph_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_button_analysis.addWidget(self.lineEdit_add_graph_2, 3, 0, 1, 1)

        self.button_graph_remove_1 = QPushButton(self.frame_analysis_left)
        self.button_graph_remove_1.setObjectName(u"button_graph_remove_1")
        self.button_graph_remove_1.setMinimumSize(QSize(80, 25))
        self.button_graph_remove_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(238, 75, 115);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{	\n"
"	background-color: qlineargradient(spread:pad, x1:0.511, y1:0.00568182, x2:0.511, y2:1, stop:0 rgba(230, 80, 115, 255), stop:1 rgba(242, 230, 230, 255));\n"
"}")

        self.grid_button_analysis.addWidget(self.button_graph_remove_1, 1, 2, 1, 1)

        self.lineEdit_add_graph_3 = QLineEdit(self.frame_analysis_left)
        self.lineEdit_add_graph_3.setObjectName(u"lineEdit_add_graph_3")
        self.lineEdit_add_graph_3.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_graph_3.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_button_analysis.addWidget(self.lineEdit_add_graph_3, 7, 0, 1, 1)

        self.button_graph_browse_3 = QPushButton(self.frame_analysis_left)
        self.button_graph_browse_3.setObjectName(u"button_graph_browse_3")
        self.button_graph_browse_3.setMinimumSize(QSize(80, 25))
        self.button_graph_browse_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_button_analysis.addWidget(self.button_graph_browse_3, 7, 1, 1, 1)

        self.button_graph_remove_3 = QPushButton(self.frame_analysis_left)
        self.button_graph_remove_3.setObjectName(u"button_graph_remove_3")
        self.button_graph_remove_3.setMinimumSize(QSize(80, 25))
        self.button_graph_remove_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(238, 75, 115);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{	\n"
"	background-color: qlineargradient(spread:pad, x1:0.511, y1:0.00568182, x2:0.511, y2:1, stop:0 rgba(230, 80, 115, 255), stop:1 rgba(242, 230, 230, 255));\n"
"}")

        self.grid_button_analysis.addWidget(self.button_graph_remove_3, 7, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.grid_button_analysis)


        self.horizontalLayout_7.addWidget(self.frame_analysis_left)

        self.frame_analysis_right = QFrame(self.frame_analysis_center)
        self.frame_analysis_right.setObjectName(u"frame_analysis_right")
        self.frame_analysis_right.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_analysis_right)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_formula = QLabel(self.frame_analysis_right)
        self.label_formula.setObjectName(u"label_formula")
        self.label_formula.setFont(font5)

        self.verticalLayout_7.addWidget(self.label_formula)

        self.stackedWidget_formula = QStackedWidget(self.frame_analysis_right)
        self.stackedWidget_formula.setObjectName(u"stackedWidget_formula")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_formula.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_formula.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget_formula)

        self.layout_formula_next_prev = QHBoxLayout()
        self.layout_formula_next_prev.setObjectName(u"layout_formula_next_prev")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_formula_next_prev.addItem(self.horizontalSpacer_5)

        self.button_formula_prev = QPushButton(self.frame_analysis_right)
        self.button_formula_prev.setObjectName(u"button_formula_prev")
        self.button_formula_prev.setMinimumSize(QSize(80, 25))
        self.button_formula_prev.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.layout_formula_next_prev.addWidget(self.button_formula_prev)

        self.button_formula_next = QPushButton(self.frame_analysis_right)
        self.button_formula_next.setObjectName(u"button_formula_next")
        self.button_formula_next.setMinimumSize(QSize(80, 25))
        self.button_formula_next.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.layout_formula_next_prev.addWidget(self.button_formula_next)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_formula_next_prev.addItem(self.horizontalSpacer_21)


        self.verticalLayout_7.addLayout(self.layout_formula_next_prev)


        self.horizontalLayout_7.addWidget(self.frame_analysis_right)


        self.verticalLayout_6.addWidget(self.frame_analysis_center)

        self.frame_analysis_bottom = QFrame(self.tab_analysis)
        self.frame_analysis_bottom.setObjectName(u"frame_analysis_bottom")
        self.frame_analysis_bottom.setMinimumSize(QSize(50, 35))
        self.frame_analysis_bottom.setMaximumSize(QSize(16777215, 35))
        self.frame_analysis_bottom.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_analysis_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_analysis_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_analysis_bottom)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.label_name_2 = QLabel(self.frame_analysis_bottom)
        self.label_name_2.setObjectName(u"label_name_2")

        self.horizontalLayout_6.addWidget(self.label_name_2)

        self.horizontalSpacer_4 = QSpacerItem(615, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.button_next_2 = QPushButton(self.frame_analysis_bottom)
        self.button_next_2.setObjectName(u"button_next_2")
        self.button_next_2.setMinimumSize(QSize(80, 25))
        self.button_next_2.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border: 1px solid rgb(67, 67, 67);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.button_next_2)

        self.frame_4 = QFrame(self.frame_analysis_bottom)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(5, 5))
        self.frame_4.setMaximumSize(QSize(5, 5))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_analysis_bottom)

        self.main_tabWidget.addTab(self.tab_analysis, "")
        self.tab__results = QWidget()
        self.tab__results.setObjectName(u"tab__results")
        self.verticalLayout_9 = QVBoxLayout(self.tab__results)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_results_top = QFrame(self.tab__results)
        self.frame_results_top.setObjectName(u"frame_results_top")
        self.frame_results_top.setMinimumSize(QSize(0, 30))
        self.frame_results_top.setMaximumSize(QSize(16777215, 30))
        self.frame_results_top.setFrameShape(QFrame.StyledPanel)
        self.frame_results_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_results_top)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(670, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.button_minimize_3 = QPushButton(self.frame_results_top)
        self.button_minimize_3.setObjectName(u"button_minimize_3")
        self.button_minimize_3.setMinimumSize(QSize(20, 20))
        self.button_minimize_3.setMaximumSize(QSize(20, 20))
        self.button_minimize_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	image: url(minimize.png);\n"
"}")

        self.horizontalLayout_12.addWidget(self.button_minimize_3)

        self.horizontalSpacer_17 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_17)

        self.button_restore_3 = QPushButton(self.frame_results_top)
        self.button_restore_3.setObjectName(u"button_restore_3")
        self.button_restore_3.setMinimumSize(QSize(20, 20))
        self.button_restore_3.setMaximumSize(QSize(20, 20))
        self.button_restore_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"QPushButton::hover{	\n"
"	image: url(maximize.png);\n"
"}")

        self.horizontalLayout_12.addWidget(self.button_restore_3)

        self.horizontalSpacer_18 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)

        self.button_exit_3 = QPushButton(self.frame_results_top)
        self.button_exit_3.setObjectName(u"button_exit_3")
        self.button_exit_3.setMinimumSize(QSize(20, 20))
        self.button_exit_3.setMaximumSize(QSize(20, 20))
        self.button_exit_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover{	\n"
"	image: url(close.png);\n"
"}")

        self.horizontalLayout_12.addWidget(self.button_exit_3)

        self.horizontalSpacer_19 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)


        self.verticalLayout_9.addWidget(self.frame_results_top)

        self.frame_results_center = QFrame(self.tab__results)
        self.frame_results_center.setObjectName(u"frame_results_center")
        self.frame_results_center.setFrameShape(QFrame.StyledPanel)
        self.frame_results_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_results_center)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_results_left = QFrame(self.frame_results_center)
        self.frame_results_left.setObjectName(u"frame_results_left")
        self.frame_results_left.setFrameShape(QFrame.StyledPanel)
        self.frame_results_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_results_left)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_report = QLabel(self.frame_results_left)
        self.label_report.setObjectName(u"label_report")
        self.label_report.setMaximumSize(QSize(16777215, 20))
        self.label_report.setFont(font)

        self.verticalLayout_10.addWidget(self.label_report)

        self.grid_results_button = QGridLayout()
        self.grid_results_button.setObjectName(u"grid_results_button")
        self.grid_results_button.setVerticalSpacing(10)
        self.label_add_uni_logo = QLabel(self.frame_results_left)
        self.label_add_uni_logo.setObjectName(u"label_add_uni_logo")
        self.label_add_uni_logo.setMaximumSize(QSize(16777215, 22))
        self.label_add_uni_logo.setFont(font1)
        self.label_add_uni_logo.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.label_add_uni_logo, 0, 0, 1, 1)

        self.label_add_uni_name = QLabel(self.frame_results_left)
        self.label_add_uni_name.setObjectName(u"label_add_uni_name")
        self.label_add_uni_name.setMaximumSize(QSize(16777215, 22))
        self.label_add_uni_name.setFont(font1)
        self.label_add_uni_name.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.label_add_uni_name, 2, 0, 1, 1)

        self.lineEdit_add_uni_logo = QLineEdit(self.frame_results_left)
        self.lineEdit_add_uni_logo.setObjectName(u"lineEdit_add_uni_logo")
        self.lineEdit_add_uni_logo.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_uni_logo.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.lineEdit_add_uni_logo, 1, 0, 1, 1)

        self.button_report_apply_2 = QPushButton(self.frame_results_left)
        self.button_report_apply_2.setObjectName(u"button_report_apply_2")
        self.button_report_apply_2.setMinimumSize(QSize(80, 25))
        self.button_report_apply_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_results_button.addWidget(self.button_report_apply_2, 5, 1, 1, 1)

        self.label_add_date = QLabel(self.frame_results_left)
        self.label_add_date.setObjectName(u"label_add_date")
        self.label_add_date.setMaximumSize(QSize(16777215, 22))
        self.label_add_date.setFont(font1)
        self.label_add_date.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.label_add_date, 6, 0, 1, 1)

        self.button_report_browse = QPushButton(self.frame_results_left)
        self.button_report_browse.setObjectName(u"button_report_browse")
        self.button_report_browse.setMinimumSize(QSize(80, 25))
        self.button_report_browse.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_results_button.addWidget(self.button_report_browse, 1, 1, 1, 1)

        self.lineEdit_add_uni_name = QLineEdit(self.frame_results_left)
        self.lineEdit_add_uni_name.setObjectName(u"lineEdit_add_uni_name")
        self.lineEdit_add_uni_name.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_uni_name.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.lineEdit_add_uni_name, 3, 0, 1, 1)

        self.lineEdit_add_name = QLineEdit(self.frame_results_left)
        self.lineEdit_add_name.setObjectName(u"lineEdit_add_name")
        self.lineEdit_add_name.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_name.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.lineEdit_add_name, 5, 0, 1, 1)

        self.button_report_apply_1 = QPushButton(self.frame_results_left)
        self.button_report_apply_1.setObjectName(u"button_report_apply_1")
        self.button_report_apply_1.setMinimumSize(QSize(80, 25))
        self.button_report_apply_1.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_results_button.addWidget(self.button_report_apply_1, 3, 1, 1, 1)

        self.label_add_name = QLabel(self.frame_results_left)
        self.label_add_name.setObjectName(u"label_add_name")
        self.label_add_name.setMaximumSize(QSize(16777215, 22))
        self.label_add_name.setFont(font1)
        self.label_add_name.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.label_add_name, 4, 0, 1, 1)

        self.lineEdit_add_date = QLineEdit(self.frame_results_left)
        self.lineEdit_add_date.setObjectName(u"lineEdit_add_date")
        self.lineEdit_add_date.setMinimumSize(QSize(0, 25))
        self.lineEdit_add_date.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(214, 214, 214);\n"
"	border-radius: 10px;\n"
"}")

        self.grid_results_button.addWidget(self.lineEdit_add_date, 8, 0, 1, 1)

        self.button_report_apply_3 = QPushButton(self.frame_results_left)
        self.button_report_apply_3.setObjectName(u"button_report_apply_3")
        self.button_report_apply_3.setMinimumSize(QSize(80, 25))
        self.button_report_apply_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(72, 81, 110);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"		background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(71, 83, 107, 255), stop:1 rgba(153, 153, 153, 255));\n"
"}")

        self.grid_results_button.addWidget(self.button_report_apply_3, 8, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.grid_results_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.button_report_print_pdf = QPushButton(self.frame_results_left)
        self.button_report_print_pdf.setObjectName(u"button_report_print_pdf")
        self.button_report_print_pdf.setMaximumSize(QSize(16777215, 120))
        font6 = QFont()
        font6.setPointSize(18)
        font6.setBold(True)
        self.button_report_print_pdf.setFont(font6)
        self.button_report_print_pdf.setStyleSheet(u"QPushButton{\n"
"	border-margin: 5px;\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-radius: 10px;\n"
"	color: rgb(72, 82, 108);\n"
"	\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(197, 197, 197, 255), stop:1 rgba(225, 225, 225, 255));\n"
"}")

        self.verticalLayout_10.addWidget(self.button_report_print_pdf)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.horizontalLayout_11.addWidget(self.frame_results_left)

        self.frame_results_right = QFrame(self.frame_results_center)
        self.frame_results_right.setObjectName(u"frame_results_right")
        self.frame_results_right.setMinimumSize(QSize(374, 0))
        self.frame_results_right.setFrameShape(QFrame.StyledPanel)
        self.frame_results_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_results_right)


        self.verticalLayout_9.addWidget(self.frame_results_center)

        self.frame_results_bottom = QFrame(self.tab__results)
        self.frame_results_bottom.setObjectName(u"frame_results_bottom")
        self.frame_results_bottom.setMinimumSize(QSize(50, 35))
        self.frame_results_bottom.setMaximumSize(QSize(16777215, 35))
        self.frame_results_bottom.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_results_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_results_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_results_bottom)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)

        self.label_name_3 = QLabel(self.frame_results_bottom)
        self.label_name_3.setObjectName(u"label_name_3")

        self.horizontalLayout_13.addWidget(self.label_name_3)

        self.horizontalSpacer_8 = QSpacerItem(696, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.frame_5 = QFrame(self.frame_results_bottom)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(5, 5))
        self.frame_5.setMaximumSize(QSize(5, 5))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_5)


        self.verticalLayout_9.addWidget(self.frame_results_bottom)

        self.main_tabWidget.addTab(self.tab__results, "")

        self.verticalLayout.addWidget(self.main_tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_minimize_1.setText("")
        self.button_restore_1.setText("")
        self.button_exit_1.setText("")
        self.label_.setText(QCoreApplication.translate("MainWindow", u"Video Edge Detection Optimization", None))
        self.label_camera_1.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_s_min.setText(QCoreApplication.translate("MainWindow", u"S Min", None))
        self.label_s_max.setText(QCoreApplication.translate("MainWindow", u"S Max", None))
        self.label_v_min.setText(QCoreApplication.translate("MainWindow", u"V Min", None))
        self.label_v_max.setText(QCoreApplication.translate("MainWindow", u"V Max", None))
        self.label_h_max.setText(QCoreApplication.translate("MainWindow", u"H Max", None))
        self.label_h_min.setText(QCoreApplication.translate("MainWindow", u"H Min", None))
        self.checkBox_safety.setText(QCoreApplication.translate("MainWindow", u"Safety Distance is Fine", None))
        self.checkBox_secure.setText(QCoreApplication.translate("MainWindow", u"Components are Secured", None))
        self.label_instructions.setText(QCoreApplication.translate("MainWindow", u"<strong>Instructions </strong> <br>Testi ba\u015flatmadan \u00f6nce kalibrasyonr\u0131 tamamlay\u0131n\u0131z", None))
        self.button_weight.setText(QCoreApplication.translate("MainWindow", u"Weight\n"
"Calibration", None))
        self.button_measure.setText(QCoreApplication.translate("MainWindow", u"Measure", None))
        self.button_image.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Calibration", None))
        self.button_activate.setText(QCoreApplication.translate("MainWindow", u"Activate\n"
"System", None))
        self.label_spec_standart.setText(QCoreApplication.translate("MainWindow", u"Specimen Standart", None))
        self.label_material.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.button_test_standart.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.button_material.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_test_standart.setText(QCoreApplication.translate("MainWindow", u"Test Standart", None))
        self.button_spec_standart.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_name_1.setText(QCoreApplication.translate("MainWindow", u"Eduneering Team - Teknofest 2021", None))
        self.button_next_1.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_config), QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.button_minimize_2.setText("")
        self.button_restore_2.setText("")
        self.button_exit_2.setText("")
        self.label_stress_strain.setText(QCoreApplication.translate("MainWindow", u"Stress - Strain Curve", None))
        self.label_camera_2.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_add_graph_1.setText(QCoreApplication.translate("MainWindow", u"Add a Graph for Comparison", None))
        self.label_add_graph_3.setText(QCoreApplication.translate("MainWindow", u"Add a Graph for Comparison", None))
        self.label_add_graph_2.setText(QCoreApplication.translate("MainWindow", u"Add a Graph for Comparison", None))
        self.button_graph_browse_1.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.button_graph_remove_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.button_graph_browse_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.button_graph_remove_1.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.button_graph_browse_3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.button_graph_remove_3.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_formula.setText(QCoreApplication.translate("MainWindow", u"Instant Formula and Edu Panel", None))
        self.button_formula_prev.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.button_formula_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_name_2.setText(QCoreApplication.translate("MainWindow", u"Eduneering Team - Teknofest 2021", None))
        self.button_next_2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_analysis), QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.button_minimize_3.setText("")
        self.button_restore_3.setText("")
        self.button_exit_3.setText("")
        self.label_report.setText(QCoreApplication.translate("MainWindow", u"Report Information", None))
        self.label_add_uni_logo.setText(QCoreApplication.translate("MainWindow", u"Add University Logo", None))
        self.label_add_uni_name.setText(QCoreApplication.translate("MainWindow", u"Add University Name", None))
        self.button_report_apply_2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_add_date.setText(QCoreApplication.translate("MainWindow", u"Date of Testing", None))
        self.button_report_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.button_report_apply_1.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_add_name.setText(QCoreApplication.translate("MainWindow", u"Tester Name", None))
        self.button_report_apply_3.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.button_report_print_pdf.setText(QCoreApplication.translate("MainWindow", u"Print to PDF", None))
        self.label_name_3.setText(QCoreApplication.translate("MainWindow", u"Eduneering Team - Teknofest 2021", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab__results), QCoreApplication.translate("MainWindow", u"Results", None))
    # retranslateUi

