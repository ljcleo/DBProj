# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuestPartUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GuestPart(object):
    def setupUi(self, GuestPart):
        GuestPart.setObjectName("GuestPart")
        GuestPart.resize(960, 640)
        self.GuestFrame = QtWidgets.QFrame(GuestPart)
        self.GuestFrame.setGeometry(QtCore.QRect(65, 150, 120, 280))
        self.GuestFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GuestFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GuestFrame.setObjectName("GuestFrame")
        self.GuestLabel = QtWidgets.QLabel(self.GuestFrame)
        self.GuestLabel.setGeometry(QtCore.QRect(-5, 0, 130, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.GuestLabel.setFont(font)
        self.GuestLabel.setScaledContents(False)
        self.GuestLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuestLabel.setObjectName("GuestLabel")
        self.GuestQuit = QtWidgets.QPushButton(self.GuestFrame)
        self.GuestQuit.setGeometry(QtCore.QRect(0, 250, 120, 30))
        self.GuestQuit.setAutoDefault(False)
        self.GuestQuit.setObjectName("GuestQuit")
        self.LoginOrRegister = QtWidgets.QPushButton(self.GuestFrame)
        self.LoginOrRegister.setGeometry(QtCore.QRect(0, 200, 120, 30))
        self.LoginOrRegister.setAutoDefault(False)
        self.LoginOrRegister.setDefault(False)
        self.LoginOrRegister.setObjectName("LoginOrRegister")

        self.retranslateUi(GuestPart)
        self.GuestQuit.clicked.connect(GuestPart.close)
        self.LoginOrRegister.clicked.connect(GuestPart.loginOrRegister)
        QtCore.QMetaObject.connectSlotsByName(GuestPart)

    def retranslateUi(self, GuestPart):
        _translate = QtCore.QCoreApplication.translate
        GuestPart.setWindowTitle(_translate("GuestPart", "Login"))
        self.GuestLabel.setText(_translate("GuestPart", "当前未登录"))
        self.GuestQuit.setText(_translate("GuestPart", "退出系统"))
        self.LoginOrRegister.setText(_translate("GuestPart", "登录/注册"))
