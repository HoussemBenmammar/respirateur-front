# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standby.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import random 
import json
import requests
import time
from PyQt5.QtCore import QTimer,QDateTime
import numpy as np
from connection import *
mode_msg=""
globale_values=[]
# Opening JSON ventilation file
ven_f = open('ventilation.json',)
vent = json.load(ven_f)

# Opening JSON ventilation file
gas_f = open('gas.json',)
gas = json.load(gas_f)

# Opening JSON mode file
mode_f = open('mode.json',)
mode = json.load(mode_f)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotOnCanvas
        self.pushButton.setGeometry(QtCore.QRect(10, 350, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickModepcvOrVen)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(790, 90, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 70, 1011, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 500, 201, 31))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(810, 460, 201, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 420, 201, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.clickGasOrVcv)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 350, 141, 51))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 350, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clickModeprvc)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(self.clickModesimv)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 350, 131, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(810, 380, 201, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(810, 340, 201, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(810, 300, 201, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.clickVentilation)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(810, 260, 201, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.clickAlarm)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(810, 220, 201, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(890, 110, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("home.png"))
        self.label.setObjectName("label")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_13.setGeometry(QtCore.QRect(810, 90, 201, 121))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 10, 201, 61))
        self.label_2.setStyleSheet("background-color:white;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 20, 41, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("lungs(1).png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, 10, 31, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("question(1).png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 40, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("leaf.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 10, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("pulse.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 10, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("frequency.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 40, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("analysis.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 40, 21, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("death.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(900, 510, 21, 16))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("back(1).png"))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(870, 10, 71, 61))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("immune.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 400, 81, 61))
        self.label_13.setStyleSheet("background-color:#FFFFFF")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(100, 400, 81, 61))
        self.label_14.setStyleSheet("background-color:#FFFFFF")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(200, 400, 81, 61))
        self.label_15.setStyleSheet("background-color:#FFFFFF")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(300, 400, 81, 61))
        self.label_16.setStyleSheet("background-color:#FFFFFF")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(500, 400, 81, 61))
        self.label_17.setStyleSheet("background-color:#FFFFFF")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(600, 400, 81, 61))
        self.label_18.setStyleSheet("background-color:#FFFFFF")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 470, 81, 61))
        self.label_19.setStyleSheet("background-color:#FFFFFF")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(100, 470, 81, 61))
        self.label_20.setStyleSheet("background-color:#FFFFFF")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(400, 400, 81, 61))
        self.label_21.setStyleSheet("background-color:#FFFFFF")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 350, 131, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.clickModepsv)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 90, 771, 261))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        # horizontal layout
        self.horizontalLayout_4=QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #canvas here 
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        #end of canvas
        #add canvas
        self.horizontalLayout_4.addWidget(self.canvas)
        #end of horizontal
        self.textBrowser_13.raise_()
        self.pushButton.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.pushButton_5.raise_()
        self.frame_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1023, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.BatteryState = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("smartphone-charger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BatteryState.setIcon(icon)
        self.BatteryState.setObjectName("BatteryState")
        self.actionman = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("restrooms(2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionman.setIcon(icon1)
        self.actionman.setObjectName("actionman")
        self.actioncough = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cough(2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncough.setIcon(icon2)
        self.actioncough.setObjectName("actioncough")
        self.actionTime = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("digital-clock-midnight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTime.setIcon(icon3)
        self.actionTime.setObjectName("actionTime")
        self.toolBar.addAction(self.actionTime)
        self.toolBar.addAction(self.BatteryState)
        self.toolBar.addAction(self.actionman)
        self.toolBar.addAction(self.actioncough)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ventilation"))
        self.pushButton_8.setText(_translate("MainWindow", "System"))
        self.pushButton_9.setText(_translate("MainWindow", "Functions"))
        self.pushButton_2.setText(_translate("MainWindow", "Gas"))
        self.pushButton_3.setText(_translate("MainWindow", "PRVC"))
        #self.pushButton_3.clicked.connect(self.plotOnCanvasRep)
        self.pushButton_4.setText(_translate("MainWindow", "SIMV"))
        self.pushButton_10.setText(_translate("MainWindow", "Warning"))
        self.pushButton_11.setText(_translate("MainWindow", "Maneuvers"))
        self.pushButton_12.setText(_translate("MainWindow", "Ventillation"))
        self.pushButton_13.setText(_translate("MainWindow", "Alarms"))
        self.pushButton_14.setText(_translate("MainWindow", "Patlent"))
        self.label_13.setText(_translate("MainWindow", "MVmax : 8"))
        self.label_14.setText(_translate("MainWindow", "MVmin : 8"))
        self.label_15.setText(_translate("MainWindow", "VTmax : 8"))
        self.label_16.setText(_translate("MainWindow", "VTmin : 8"))
        self.label_17.setText(_translate("MainWindow", "Fmin : 8"))
        self.label_18.setText(_translate("MainWindow", "Pmax : 8"))
        self.label_19.setText(_translate("MainWindow", "Pmin : 8"))
        self.label_20.setText(_translate("MainWindow", "Leakage : 8"))
        self.label_21.setText(_translate("MainWindow", "Fmax : 8"))
        self.pushButton_5.setText(_translate("MainWindow", "PSV"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.BatteryState.setText(_translate("MainWindow", "Battery"))
        self.actionman.setText(_translate("MainWindow", "man"))
        self.actioncough.setText(_translate("MainWindow", "cough"))
        self.actionTime.setText(_translate("MainWindow", "Time"))
        self.pushButton.hide()
        self.pushButton_2.hide()   
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.label_17.setHidden(True)
        self.label_18.setHidden(True)
        self.label_19.setHidden(True)
        self.label_20.setHidden(True)
        self.label_21.setHidden(True)
        self.label_13.setHidden(True)
        self.label_14.setHidden(True)
        self.label_15.setHidden(True)
        self.label_16.setHidden(True)
    
    
    def plotOnCanvasRep(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.plotOnCanvas)
        #self.timer.timeout.connect(self.clickModesimv)
        self.timer.start(100)
    def plotOnCanvas(self): 
        self.figure.clear()
        fruits = ['o2', 'peep', 'freq','t','ps','ramp','flow','vt','i']
        
        values=api(mode_msg)
        global global_values
        global_values=values
        print(mode_msg)
        #print(values)
        plt.bar(fruits,values,color="red",width=0.2)
        #plt.xlabel("type of fruits")
        plt.ylabel("Valuers")
        plt.title("mode : "+mode_msg)
        self.canvas.draw()
        self.label_13.setHidden(False)
        self.label_14.setHidden(False)
        self.label_15.setHidden(False)
        self.label_16.setHidden(False)
        self.label_17.setHidden(False)
        self.label_18.setHidden(False)
        self.label_19.setHidden(False)
        self.label_20.setHidden(False)
        self.label_21.setHidden(False)
        self.label_13.setStyleSheet("background-color: white")
        self.label_13.setText("o2: "+str(values[0]))  
        self.label_14.setText("Peep : "+str(values[1]))
        self.label_15.setText("Freq : "+str(values[2]))
        self.label_16.setText("Vt : "+str(values[7]))
        self.label_17.setText("I : "+str(values[8]))
        self.label_18.setText("Flow : "+str(values[6]))
        self.label_19.setText("Ps : "+str(values[4]))
        self.label_20.setText("Ramp : "+str(values[5]))
        self.label_21.setText("T : "+str(values[3]))
        if (values[0]>80):
            self.label_13.setStyleSheet("background-color: red")
            api_error()
        if (60 <= values[0] < 80):
            self.label_13.setStyleSheet("background-color: yellow")    
            
        #self.clickModesimv() 
    def clickAlarm(self) : 
             self.pushButton.setHidden(False)
             self.pushButton_2.setHidden(False)  
             self.pushButton.setText("Ventilation")
             self.pushButton_2.setText("Gas")
             self.pushButton_4.hide()
             self.pushButton_3.hide()
             self.pushButton_5.hide()

    def clickModepcvOrVen(self):
      # hide make sure message
      if self.pushButton.text()=="Ventilation" :
        vent=api_vent()
        self.label_13.setHidden(False)
        self.label_14.setHidden(False)
        self.label_15.setHidden(False)
        self.label_16.setHidden(False)
        self.label_17.setHidden(False)
        self.label_18.setHidden(False)
        self.label_19.setHidden(False)
        self.label_20.setHidden(True)
        self.label_21.setHidden(False)
        self.label_13.setText("mvmax: "+vent[0])  
        self.label_14.setText("mvmin : "+vent[1])
        self.label_15.setText("vtmax : "+vent[2])
        self.label_16.setText("vtmin : "+vent[3])
        self.label_17.setText("fmax : "+vent[4])
        self.label_18.setText("pmax : "+vent[5])
        self.label_19.setText("pmin : "+vent[6])
        self.label_21.setText("leakage : "+vent[7])
      else :
        global mode_msg
        mode_msg="PCV" 
        self.plotOnCanvasRep() 
                 
    
    def clickVentilation(self):
        # hide make sure message
        self.pushButton.setHidden(False)
        self.pushButton_2.setHidden(False)
        self.pushButton.setText("PCV")
        self.pushButton_2.setText("VCV")
        self.pushButton_3.setHidden(False)
        self.pushButton_4.setHidden(False)
        self.pushButton_5.setHidden(False)
        self.label_13.setHidden(True)
        self.label_14.setHidden(True)
        self.label_15.setHidden(True)
        self.label_16.setHidden(True)
        self.label_17.setHidden(True)
        self.label_18.setHidden(True)
        self.label_19.setHidden(True)
        self.label_20.setHidden(True)
        self.label_21.setHidden(True)
    
    def clickGasOrVcvRep(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.clickGasOrVcv)
        self.timer.start(50)

    def clickGasOrVcv(self):
        #z=z+1
        
        # hide make sure message
        if self.pushButton_2.text()=="Gas" :
         
            self.label_17.setHidden(True)
            self.label_18.setHidden(True)
            self.label_19.setHidden(True)
            self.label_20.setHidden(True)
            self.label_21.setHidden(True)
            self.label_13.setHidden(False)
            self.label_14.setHidden(False)
            self.label_15.setHidden(False)
            self.label_16.setHidden(False)
            i=0
                
            # response = requests.get('https://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5') 
            # gas=response.json() 
            gas=api_gas()
            self.label_13.setText("As max : " +gas[0])
            self.label_14.setText("As min : " +gas[1])
            self.label_15.setText("O2s max : " +gas[2])
            self.label_16.setText("O2s min : "+gas[3])
            #time.sleep(2)
            
         
        else :
         global mode_msg
         mode_msg="VCV"
         values=api(mode_msg)
         self.plotOnCanvasRep() 

    def clickModeprvc(self):
        # hide make sure message
        global mode_msg
        mode_msg="PRVC"
        values=api(mode_msg)
        self.plotOnCanvasRep()     
    
    def clickModepsv(self):
        global mode_msg
        mode_msg="PSV"
        values=api(mode_msg)
        self.plotOnCanvasRep()
        # hide make sure message
        
    
    def clickModesimv(self):
        # hide make sure message
        global mode_msg
        mode_msg="SIMV"
        #values=api(mode_msg)
        self.plotOnCanvasRep()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())