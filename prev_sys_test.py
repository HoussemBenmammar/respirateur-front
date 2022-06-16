
from PyQt5 import QtCore, QtGui, QtWidgets
import json
   
# Opening JSON file
f = open('sys-test.json',)
data = json.load(f)
# Convert string to Python dict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color:#191970\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 611, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:\n"
"#E1F5FE")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 140, 261, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 100, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:\n"
"#E1F5FE")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1110, 0, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:\n"
"#E1F5FE;\n"
"background-color:#607D8B\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(1110, 50, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:#607D8B\n"
";\n"
"background-color:#1A237E\n"
"")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(1110, 100, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color:#607D8B\n"
";\n"
"background-color:#1A237E")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1110, 150, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color:\n"
"#E1F5FE;\n"
"background-color:#607D8B")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 410, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color:\n"
"#E1F5FE;\n"
"background-color:#607D8B")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(1110, 490, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color:\n"
"#E1F5FE;\n"
"background-color:#607D8B")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1110, 390, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color:\n"
"#E1F5FE;\n"
"background-color:#607D8B")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(1110, 440, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color:\n"
"#E1F5FE;\n"
"background-color:#607D8B")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 240, 921, 111))
        self.frame.setStyleSheet("background-color:#1A237E")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(20, 50, 891, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:\n"
"#E1F5FE")
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(1110, 210, 251, 181))
        self.frame_2.setStyleSheet("background-color:#000000")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(40, 0, 251, 211))
        self.frame_4.setStyleSheet("background-color:#000000")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1110, 550, 251, 181))
        self.frame_3.setStyleSheet("background-color:#000000")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(20, -20, 251, 211))
        self.frame_5.setStyleSheet("background-color:#000000")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System Test"))
        self.label.setText(_translate("MainWindow", "compliance :"+ data[0]['compliance']))
        self.label.setText(_translate("MainWindow", "resistance :"+ data[0]['resistance']))
        self.label.setText(_translate("MainWindow", "leakage :"+ data[0]['Leakage']))
        self.label_3.setText(_translate("MainWindow", "Prepare the device,close the y-piece"))
        self.pushButton.setText(_translate("MainWindow", "bypass system test"))
        self.pushButton_2.setText(_translate("MainWindow", "accept"))
        self.pushButton_3.setText(_translate("MainWindow", "repeat"))
        self.pushButton_4.setText(_translate("MainWindow", "O2 Sensor Calibration"))
        self.pushButton_5.setText(_translate("MainWindow", "System Test Start"))
        self.pushButton_6.setText(_translate("MainWindow", "Turn off the device"))
        self.pushButton_7.setText(_translate("MainWindow", "Config"))
        self.pushButton_8.setText(_translate("MainWindow", "Service"))
        self.label_4.setText(_translate("MainWindow", "Progress"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())