# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogr_giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 230, 101, 21))
        self.label.setStyleSheet("background-color: rgb(164, 213, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 280, 61, 20))
        self.label_2.setStyleSheet("background-color: rgb(164, 213, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 230, 151, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 280, 151, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 130, 191, 51))
        self.label_3.setStyleSheet("background-color: rgb(239, 126, 24);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 10, 71, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 195, 99);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri dönme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 350, 151, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(251, 255, 160);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ÖĞRENCİ GİRİŞİ"))
        self.label.setText(_translate("MainWindow", "ÖĞRENCİ NO:"))
        self.label_2.setText(_translate("MainWindow", "ŞİFRE:"))
        self.label_3.setText(_translate("MainWindow", "       ÖĞRENCİ GİRİŞİ"))
        self.pushButton_2.setText(_translate("MainWindow", "GERİ"))
        self.pushButton.setText(_translate("MainWindow", "GİRİŞ YAP"))
