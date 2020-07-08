# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\MainPartUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        self.VLine = QtWidgets.QFrame(MainWindow)
        self.VLine.setGeometry(QtCore.QRect(240, 0, 20, 640))
        self.VLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.VLine.setLineWidth(3)
        self.VLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.VLine.setObjectName("VLine")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass
