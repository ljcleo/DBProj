# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        RegisterDialog.setObjectName("RegisterDialog")
        RegisterDialog.resize(300, 400)
        self.frame = QtWidgets.QFrame(RegisterDialog)
        self.frame.setGeometry(QtCore.QRect(25, 25, 250, 350))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Register = QtWidgets.QPushButton(self.frame)
        self.Register.setGeometry(QtCore.QRect(25, 230, 90, 28))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Register.setFont(font)
        self.Register.setDefault(True)
        self.Register.setObjectName("Register")
        self.Cancel = QtWidgets.QPushButton(self.frame)
        self.Cancel.setGeometry(QtCore.QRect(135, 230, 90, 28))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Cancel.setFont(font)
        self.Cancel.setObjectName("Cancel")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(65, 45, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setTextFormat(QtCore.Qt.AutoText)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.PasswordAgain = QtWidgets.QLineEdit(self.frame)
        self.PasswordAgain.setGeometry(QtCore.QRect(45, 180, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.PasswordAgain.setFont(font)
        self.PasswordAgain.setObjectName("PasswordAgain")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(45, 140, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Password.setFont(font)
        self.Password.setAutoFillBackground(False)
        self.Password.setObjectName("Password")
        self.UserName = QtWidgets.QLineEdit(self.frame)
        self.UserName.setGeometry(QtCore.QRect(45, 100, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.UserName.setFont(font)
        self.UserName.setAutoFillBackground(False)
        self.UserName.setObjectName("UserName")

        self.retranslateUi(RegisterDialog)
        self.Register.clicked.connect(RegisterDialog.register)
        self.Cancel.clicked.connect(RegisterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)
        RegisterDialog.setTabOrder(self.UserName, self.Password)
        RegisterDialog.setTabOrder(self.Password, self.PasswordAgain)
        RegisterDialog.setTabOrder(self.PasswordAgain, self.Register)
        RegisterDialog.setTabOrder(self.Register, self.Cancel)

    def retranslateUi(self, RegisterDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "Register"))
        self.Register.setText(_translate("RegisterDialog", "注册"))
        self.Cancel.setText(_translate("RegisterDialog", "取消"))
        self.Title.setText(_translate("RegisterDialog", "XXX数据库"))
        self.PasswordAgain.setText(_translate("RegisterDialog", "确认密码"))
        self.Password.setText(_translate("RegisterDialog", "密码"))
        self.UserName.setText(_translate("RegisterDialog", "用户名"))
