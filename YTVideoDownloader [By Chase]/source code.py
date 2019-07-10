# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        MainWindow.setMinimumSize(QtCore.QSize(400, 350))
        MainWindow.setMaximumSize(QtCore.QSize(400, 350))
        MainWindow.setStyleSheet("QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"QMainWindow {\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646); \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblChoose = QtWidgets.QLabel(self.centralwidget)
        self.lblChoose.setGeometry(QtCore.QRect(0, 0, 241, 31))
        self.lblChoose.setStyleSheet("QLabel{color: #b1b1b1;\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;}")
        self.lblChoose.setObjectName("lblChoose")
        self.lblQuality = QtWidgets.QLabel(self.centralwidget)
        self.lblQuality.setGeometry(QtCore.QRect(0, 90, 251, 31))
        self.lblQuality.setStyleSheet("QLabel{color: #b1b1b1;\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;}")
        self.lblQuality.setObjectName("lblQuality")
        self.vidLinkLine = QtWidgets.QLineEdit(self.centralwidget)
        self.vidLinkLine.setGeometry(QtCore.QRect(10, 220, 191, 20))
        self.vidLinkLine.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.vidLinkLine.setObjectName("vidLinkLine")
        self.lblVidLink = QtWidgets.QLabel(self.centralwidget)
        self.lblVidLink.setGeometry(QtCore.QRect(10, 200, 61, 16))
        self.lblVidLink.setStyleSheet("color: #b1b1b1;")
        self.lblVidLink.setObjectName("lblVidLink")
        self.lblSaveDir = QtWidgets.QLabel(self.centralwidget)
        self.lblSaveDir.setGeometry(QtCore.QRect(10, 250, 121, 16))
        self.lblSaveDir.setStyleSheet("color: #b1b1b1;")
        self.lblSaveDir.setObjectName("lblSaveDir")
        self.saveDirLine = QtWidgets.QLineEdit(self.centralwidget)
        self.saveDirLine.setGeometry(QtCore.QRect(10, 270, 191, 20))
        self.saveDirLine.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}")
        self.saveDirLine.setObjectName("saveDirLine")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(10, 300, 111, 41))
        self.btnDownload.setStyleSheet("QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.btnDownload.setObjectName("btnDownload")
        self.lblPixmap = QtWidgets.QLabel(self.centralwidget)
        self.lblPixmap.setGeometry(QtCore.QRect(230, 160, 151, 151))
        self.lblPixmap.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.lblPixmap.setText("")
        self.lblPixmap.setPixmap(QtGui.QPixmap("resized.jpg"))
        self.lblPixmap.setObjectName("lblPixmap")
        self.lblMadeBy = QtWidgets.QLabel(self.centralwidget)
        self.lblMadeBy.setGeometry(QtCore.QRect(230, 310, 161, 21))
        self.lblMadeBy.setStyleSheet("QLabel{color: #b1b1b1;\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;}")
        self.lblMadeBy.setOpenExternalLinks(True)
        self.lblMadeBy.setObjectName("lblMadeBy")
        self.groupUp = QtWidgets.QGroupBox(self.centralwidget)
        self.groupUp.setGeometry(QtCore.QRect(0, 19, 120, 81))
        self.groupUp.setStyleSheet("QGroupBox { border:none }")
        self.groupUp.setTitle("")
        self.groupUp.setObjectName("groupUp")
        self.radioVidAud = QtWidgets.QRadioButton(self.groupUp)
        self.radioVidAud.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.radioVidAud.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.radioVidAud.setObjectName("radioVidAud")
        self.radioVidOnly = QtWidgets.QRadioButton(self.groupUp)
        self.radioVidOnly.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioVidOnly.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.radioVidOnly.setObjectName("radioVidOnly")
        self.radioAudOnly = QtWidgets.QRadioButton(self.groupUp)
        self.radioAudOnly.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioAudOnly.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"")
        self.radioAudOnly.setObjectName("radioAudOnly")
        self.groupDown = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDown.setGeometry(QtCore.QRect(0, 110, 120, 91))
        self.groupDown.setStyleSheet("QGroupBox { border:none }")
        self.groupDown.setTitle("")
        self.groupDown.setObjectName("groupDown")
        self.radio720p = QtWidgets.QRadioButton(self.groupDown)
        self.radio720p.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radio720p.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.radio720p.setObjectName("radio720p")
        self.radio480p = QtWidgets.QRadioButton(self.groupDown)
        self.radio480p.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radio480p.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.radio480p.setObjectName("radio480p")
        self.radio360p = QtWidgets.QRadioButton(self.groupDown)
        self.radio360p.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radio360p.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.radio360p.setObjectName("radio360p")
        self.radio144p = QtWidgets.QRadioButton(self.groupDown)
        self.radio144p.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radio144p.setStyleSheet("QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}")
        self.radio144p.setObjectName("radio144p")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnDownload.clicked.connect(lambda: self.algorithm())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Video Downloader"))
        self.lblChoose.setText(_translate("MainWindow", "Please choose what are you downloading"))
        self.lblQuality.setText(_translate("MainWindow", "Choose a video quality [If you chose video]"))
        self.lblVidLink.setText(_translate("MainWindow", "Video Link"))
        self.lblSaveDir.setText(_translate("MainWindow", "Saving Directory"))
        self.btnDownload.setText(_translate("MainWindow", "Download"))
        self.lblMadeBy.setText(_translate("MainWindow", "<html><head/><body><p>Made by Chase on <a href=\"https://github.com/chasemepls/\"><span style=\" text-decoration: underline; color:#ffaa00;\">GitHub</span></a></p></body></html>"))
        self.radioVidAud.setText(_translate("MainWindow", "Video + Audio"))
        self.radioVidOnly.setText(_translate("MainWindow", "Video Only"))
        self.radioAudOnly.setText(_translate("MainWindow", "Audio Only"))
        self.radio720p.setText(_translate("MainWindow", "720p"))
        self.radio480p.setText(_translate("MainWindow", "480p"))
        self.radio360p.setText(_translate("MainWindow", "360p"))
        self.radio144p.setText(_translate("MainWindow", "144p"))

    def algorithm(self):
        try:
            ytLink = self.vidLinkLine.text()
            path = self.saveDirLine.text()
            yt = YouTube(ytLink)
            stream = None
            if self.radioVidAud.isChecked() and self.radio720p.isChecked():
                stream = yt.streams.get_by_itag('22')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidAud.isChecked() and self.radio480p.isChecked():
                stream = yt.streams.get_by_itag('18')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidAud.isChecked() and self.radio360p.isChecked():
                stream = yt.streams.get_by_itag('36')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidAud.isChecked() and self.radio144p.isChecked():
                stream = yt.streams.get_by_itag('17')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidOnly.isChecked() and self.radio720p.isChecked():
                stream = yt.streams.get_by_itag('137')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidOnly.isChecked() and self.radio480p.isChecked():
                stream = yt.streams.get_by_itag('135')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidOnly.isChecked() and self.radio360p.isChecked():
                stream = yt.streams.get_by_itag('134')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioVidOnly.isChecked() and self.radio144p.isChecked():
                stream = yt.streams.get_by_itag('160')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
            elif self.radioAudOnly.isChecked():
                stream = yt.streams.get_by_itag('140')
                stream.download(path)
                self.btnDownload.setText("Done!")
                path =os.path.realpath(path)
                os.startfile(path)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Error: Check that you have filled all of the fields, and also have legit YouTube links and Save Directories.')
            error_dialog.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

