# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\LoginDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(320, 320)
        self.frame = QtWidgets.QFrame(LoginDialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 280, 280))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Login = QtWidgets.QPushButton(self.frame)
        self.Login.setGeometry(QtCore.QRect(30, 190, 100, 30))
        self.Login.setDefault(True)
        self.Login.setObjectName("Login")
        self.Register = QtWidgets.QPushButton(self.frame)
        self.Register.setGeometry(QtCore.QRect(30, 230, 220, 30))
        self.Register.setObjectName("Register")
        self.Cancel = QtWidgets.QPushButton(self.frame)
        self.Cancel.setGeometry(QtCore.QRect(150, 190, 100, 30))
        self.Cancel.setObjectName("Cancel")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(80, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.UserName = QtWidgets.QLineEdit(self.frame)
        self.UserName.setGeometry(QtCore.QRect(100, 80, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.UserName.setFont(font)
        self.UserName.setAutoFillBackground(False)
        self.UserName.setMaxLength(16)
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(100, 130, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Password.setFont(font)
        self.Password.setAutoFillBackground(False)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.UserIDLabel = QtWidgets.QLabel(self.frame)
        self.UserIDLabel.setGeometry(QtCore.QRect(20, 80, 70, 30))
        self.UserIDLabel.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.UserIDLabel.setFont(font)
        self.UserIDLabel.setObjectName("UserIDLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.frame)
        self.PasswordLabel.setGeometry(QtCore.QRect(20, 130, 70, 30))
        self.PasswordLabel.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.UserIDLabel.setBuddy(self.UserName)
        self.PasswordLabel.setBuddy(self.Password)

        self.retranslateUi(LoginDialog)
        self.Login.clicked.connect(LoginDialog.login)
        self.Cancel.clicked.connect(LoginDialog.reject)
        self.Register.clicked.connect(LoginDialog.register)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.UserName, self.Password)
        LoginDialog.setTabOrder(self.Password, self.Login)
        LoginDialog.setTabOrder(self.Login, self.Cancel)
        LoginDialog.setTabOrder(self.Cancel, self.Register)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "用户登录"))
        self.Login.setText(_translate("LoginDialog", "登录"))
        self.Register.setText(_translate("LoginDialog", "注册"))
        self.Cancel.setText(_translate("LoginDialog", "取消"))
        self.Title.setText(_translate("LoginDialog", "用户登录"))
        self.UserIDLabel.setText(_translate("LoginDialog", "用户名"))
        self.PasswordLabel.setText(_translate("LoginDialog", "密码"))
