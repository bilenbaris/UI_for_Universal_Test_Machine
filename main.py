import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,Signal,QThread,QPointF)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QImage, QKeySequence, QLinearGradient, QPixmap, QPalette, QPainter, QPixmap, QRadialGradient, QWindow)
from PySide6.QtCharts import QBarCategoryAxis, QChart,QChartView,QLineSeries, QValueAxis
from PySide6.QtWidgets import *

import cv2
import numpy as np
import time
import os
from pyzbar.pyzbar import decode
import planeCreator as pC
import csv
import pdfCreator

import random


# ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen
# ==> MAIN SCREEN
from ui_main_screen import Ui_MainWindow


# ==> GLOBALS
counter = 0
lower = np.array([50,50,50])
upper = np.array([100,100,100])
midpoint = np.array([0,0])

tempArray = [0,0,0,0]


flag_imageCalibration = False
flag_check = np.array([True,False,False])


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        #################################################

        ## REMOVE TITLE
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.main_frame.setGraphicsEffect(self.shadow)
  
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        ## TIMER IN MILISECONDS
        self.timer.start(35)

        ## SET LOADING LABEL
        QtCore.QTimer.singleShot(350, lambda: self.ui.loading_label.setText("<strong>Checking Camera</strong>"))
        QtCore.QTimer.singleShot(750, lambda: self.ui.loading_label.setText("<strong>Checking Values TXT</strong>"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.loading_label.setText("<strong>Cheking Coordinates TXT</strong>"))
        QtCore.QTimer.singleShot(2250, lambda: self.ui.loading_label.setText("<strong>Loading App</strong>"))
        
        self.show()

    def progress(self):
        
        global counter
        global checked
        global check_values
        global check_coordinates
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            
            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()
            
            #CLOSE SPLASH SCREEN
            self.close()
            
        # INCREASE COUNTER
        counter += 2


class Thread(QThread):
    changePixmap = Signal(QImage)
    
    def run(self):
        global flag_imageCalibration, flag_check, lower, upper, midpoint
        cap = cv2.VideoCapture(0)
        color = np.array([0,0,0,0,0,0])
        while True:
            ret, frameThread = cap.read()

            #FOR LABEL CAMERA 1
            if ret and flag_check[0]:  
                frameHSV = cv2.cvtColor(frameThread, cv2.COLOR_BGR2HSV)
                frameMask = cv2.inRange(frameHSV, lower, upper)
                frameMask = cv2.cvtColor(frameMask, cv2.COLOR_GRAY2RGB)
                convertToQtFormat = QImage(frameMask.data, frameMask.shape[1], frameMask.shape[0],  3*frameMask.shape[1],QImage.Format_RGB888)
                p = convertToQtFormat.scaled(480, 640, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
            
            # FOR LABEL CAMERA 2
            if ret and flag_check[1]:    
                cv2.circle(frameThread, midpoint, 5, (0,255,0), 5)
                convertToQtFormat = QImage(frameThread.data, frameThread.shape[1], frameThread.shape[0],  3*frameThread.shape[1],QImage.Format_RGB888).rgbSwapped()
                # QRect cropImage(10,20,30,40)
                p = convertToQtFormat.scaled(175, 250, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                pass
            
            # FOR CHART
            if ret and flag_check[2]:
                #BURASI TABLO İÇİN KULLANILICAK
                pass  

            if  flag_imageCalibration:
                
                color = np.concatenate((lower,upper))
                planeCreate = pC.PlanCreation()
                midpoint = planeCreate.findPlaneMidPoint(frameThread, color)
                if len(midpoint) > 0:
                    flag_imageCalibration = False
                

    def stop(self):
        self.terminate()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)

        ## REMOVE TITLE
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## THREAD
        self.thread = Thread() 
        self.thread.start()
        self.thread.changePixmap.connect(self.setImage)

        self.charts()

        ## TITLE BUTTONS
        self.ui.button_exit_1.clicked.connect(self.close)
        self.ui.button_exit_2.clicked.connect(self.close)
        self.ui.button_exit_3.clicked.connect(self.close)
        self.ui.button_minimize_1.clicked.connect(self.minimized)
        self.ui.button_minimize_2.clicked.connect(self.minimized)
        self.ui.button_minimize_3.clicked.connect(self.minimized)

        ## NEXT PAGE BUTTONS
        self.ui.button_next_1.clicked.connect(self.nextPage)
        self.ui.button_next_2.clicked.connect(self.nextPage)
        ############################################
        ## ==> CONFIGURATIONS PAGE WIDGETS <== ##

        self.ui.button_image.clicked.connect(self.imageCalibrate)
        ## INSTRUCTION BUTTONS


        ## SELECTING MATERIAL/TEST/SPECIMENT BUTTONS

        ## SLIDER CHECK   
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(35)

        ## CHECKBOX 

        ############################################
        ## ==> ANALYSIS PAGE WIDGETS <== ##

        ## ADD/REMOVE GRAPH BUTTONS

        ## PREVIOUS/NEST BUTTONS

        ############################################
        ## ==> RESULT PAGE WIDGETS <== ##

        ## REPORT INFORMATIONS BUTTONS
        self.ui.button_report_browse.clicked.connect(self.do_file)
        self.ui.button_report_print_pdf.clicked.connect(self.printPdf)
    ############################################
    #### ==> FUNCTIONS <== ####
        
    #MINIMIZE BUTTON
    def minimized(self):
        self.showMinimized()

    #SET IMAGE TO LABEL CAMERA 1
    def setImage(self, image):
        global flag_check
        if flag_check[0]:
            self.ui.label_camera_1.setPixmap(QPixmap.fromImage(image))
        elif flag_check[1]:
            rect = QRect(0,0,0,0)
            self.ui.label_camera_2.setPixmap(QPixmap.fromImage(image).copy(rect))

            # self.ui.label_camera_2.setPixmap(QPixmap.fromImage(image))

    #NEXT PAGE BUTTONS
    def nextPage(self):
        page = self.ui.main_tabWidget.currentIndex()
        self.ui.main_tabWidget.setCurrentIndex(page + 1)        

    #TIMER CHECK
    def check(self):
        global flag_check

        lower[0] = int(self.ui.slider_h_min.value())
        lower[1] = int(self.ui.slider_s_min.value())
        lower[2] = int(self.ui.slider_v_min.value())

        upper[0] = int(self.ui.slider_h_max.value())
        upper[1] = int(self.ui.slider_s_max.value())
        upper[2] = int(self.ui.slider_v_max.value())
    
        page = self.ui.main_tabWidget.currentIndex()
        if page == 0:
            flag_check[0] = True
            flag_check[1] = False
            flag_check[2] = False
        elif page == 1:
            flag_check[0] = False
            flag_check[1] = True
            flag_check[2] = False
        elif page == 2:
            flag_check[0] = False
            flag_check[1] = False
            flag_check[2] = True

    #IMAGE CALIBRATION BUTTON
    def imageCalibrate(self):
        global flag_imageCalibration
        flag_imageCalibration = True


    #FIND FILE DIR
    def do_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()
        self.ui.lineEdit_add_uni_logo.setText(fname[0])

    #PRINT TO PDF
    def printPdf(self):
        
        filedir = self.ui.lineEdit_add_uni_logo.text()
        uniName = self.ui.lineEdit_add_uni_name.text()
        name = self.ui.lineEdit_add_name.text()
        date = self.ui.lineEdit_add_date.text()
        stringArray = [uniName,name,date, 'ST-37']
        pdf = pdfCreator.pdfCreator()
        pdf.create(filedir, stringArray,tempArray)


    def charts(self):
        series = QLineSeries()

        series.append(0,6)
        series.append(3,5)
        series.append(3,8)
        series.append(7,3)
        series.append(12,7)

        series1 = QLineSeries()

        series1.append(0,6)
        series1.append(3,5)
        series1.append(3,8)
        series1.append(7,3)
        series1.append(12,7)

        series << QPointF(11,1) << QPointF(13,3) << QPointF(17,6) << QPointF(18,3) << QPointF(20,22) 

        series1 << QPointF(15,1) << QPointF(17,3) << QPointF(20,6) << QPointF(24,3) << QPointF(30,22) 

        chart = QChart()
        chart.addSeries(series)
        chart.addSeries(series1)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")

        chart.legend().setVisible(True)
        # chart.legend().setAlignment(Qt.AlignBottom)

        axisX = QValueAxis()
        axisX.setRange(0,30)

        axisY = QValueAxis()
        axisY.setRange(0,30)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        series.attachAxis(axisX)
        series.attachAxis(axisY)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
        self.ui.widgetChart.setLayout(vbox)
        
        # self.ui.widget.addWidget(chartview)
        # self.setLayout(vbox)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())