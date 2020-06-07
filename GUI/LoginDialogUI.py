# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(400, 500)
        self.frame = QtWidgets.QFrame(LoginDialog)
        self.frame.setGeometry(QtCore.QRect(75, 75, 250, 350))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Login = QtWidgets.QPushButton(self.frame)
        self.Login.setGeometry(QtCore.QRect(25, 160, 90, 28))
        self.Login.setDefault(True)
        self.Login.setObjectName("Login")
        self.Register = QtWidgets.QPushButton(self.frame)
        self.Register.setGeometry(QtCore.QRect(25, 200, 200, 28))
        self.Register.setObjectName("Register")
        self.Cancel = QtWidgets.QPushButton(self.frame)
        self.Cancel.setGeometry(QtCore.QRect(135, 160, 90, 28))
        self.Cancel.setObjectName("Cancel")
        self.ChangePassword = QtWidgets.QPushButton(self.frame)
        self.ChangePassword.setGeometry(QtCore.QRect(25, 240, 200, 28))
        self.ChangePassword.setObjectName("ChangePassword")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(70, 10, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.UserName = QtWidgets.QLineEdit(self.frame)
        self.UserName.setGeometry(QtCore.QRect(45, 60, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.UserName.setFont(font)
        self.UserName.setAutoFillBackground(False)
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(45, 100, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Password.setFont(font)
        self.Password.setAutoFillBackground(False)
        self.Password.setObjectName("Password")

        self.retranslateUi(LoginDialog)
        self.Login.clicked.connect(LoginDialog.login)
        self.Cancel.clicked.connect(LoginDialog.reject)
        self.Register.clicked.connect(LoginDialog.register)
        self.ChangePassword.clicked.connect(LoginDialog.changePassword)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.UserName, self.Password)
        LoginDialog.setTabOrder(self.Password, self.Login)
        LoginDialog.setTabOrder(self.Login, self.Cancel)
        LoginDialog.setTabOrder(self.Cancel, self.Register)
        LoginDialog.setTabOrder(self.Register, self.ChangePassword)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.Login.setText(_translate("LoginDialog", "登录"))
        self.Register.setText(_translate("LoginDialog", "注册"))
        self.Cancel.setText(_translate("LoginDialog", "取消"))
        self.ChangePassword.setText(_translate("LoginDialog", "更改密码"))
        self.Title.setText(_translate("LoginDialog", "XXX数据库"))
        self.UserName.setText(_translate("LoginDialog", "用户名"))
        self.Password.setText(_translate("LoginDialog", "密码"))
