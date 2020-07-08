# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\ChangePasswordDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.resize(320, 340)
        self.frame = QtWidgets.QFrame(ChangePasswordDialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 280, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Modify = QtWidgets.QPushButton(self.frame)
        self.Modify.setGeometry(QtCore.QRect(30, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Modify.setFont(font)
        self.Modify.setDefault(True)
        self.Modify.setObjectName("Modify")
        self.Cancel = QtWidgets.QPushButton(self.frame)
        self.Cancel.setGeometry(QtCore.QRect(150, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Cancel.setFont(font)
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
        self.NewPasswordAgain = QtWidgets.QLineEdit(self.frame)
        self.NewPasswordAgain.setGeometry(QtCore.QRect(100, 180, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.NewPasswordAgain.setFont(font)
        self.NewPasswordAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPasswordAgain.setObjectName("NewPasswordAgain")
        self.NewPassword = QtWidgets.QLineEdit(self.frame)
        self.NewPassword.setGeometry(QtCore.QRect(100, 130, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.NewPassword.setFont(font)
        self.NewPassword.setAutoFillBackground(False)
        self.NewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPassword.setObjectName("NewPassword")
        self.OldPassword = QtWidgets.QLineEdit(self.frame)
        self.OldPassword.setGeometry(QtCore.QRect(100, 80, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.OldPassword.setFont(font)
        self.OldPassword.setAutoFillBackground(False)
        self.OldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.OldPassword.setObjectName("OldPassword")
        self.OldPasswordLabel = QtWidgets.QLabel(self.frame)
        self.OldPasswordLabel.setGeometry(QtCore.QRect(20, 80, 70, 30))
        self.OldPasswordLabel.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.OldPasswordLabel.setFont(font)
        self.OldPasswordLabel.setObjectName("OldPasswordLabel")
        self.NewPasswordLabel = QtWidgets.QLabel(self.frame)
        self.NewPasswordLabel.setGeometry(QtCore.QRect(20, 130, 70, 30))
        self.NewPasswordLabel.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.NewPasswordLabel.setFont(font)
        self.NewPasswordLabel.setObjectName("NewPasswordLabel")
        self.NewPasswordAgainLabel = QtWidgets.QLabel(self.frame)
        self.NewPasswordAgainLabel.setGeometry(QtCore.QRect(20, 180, 70, 30))
        self.NewPasswordAgainLabel.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.NewPasswordAgainLabel.setFont(font)
        self.NewPasswordAgainLabel.setObjectName("NewPasswordAgainLabel")
        self.OldPasswordLabel.setBuddy(self.OldPassword)
        self.NewPasswordLabel.setBuddy(self.NewPassword)
        self.NewPasswordAgainLabel.setBuddy(self.NewPasswordAgain)

        self.retranslateUi(ChangePasswordDialog)
        self.Modify.clicked.connect(ChangePasswordDialog.changePassword)
        self.Cancel.clicked.connect(ChangePasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)
        ChangePasswordDialog.setTabOrder(self.OldPassword, self.NewPassword)
        ChangePasswordDialog.setTabOrder(self.NewPassword, self.NewPasswordAgain)
        ChangePasswordDialog.setTabOrder(self.NewPasswordAgain, self.Modify)
        ChangePasswordDialog.setTabOrder(self.Modify, self.Cancel)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "修改密码"))
        self.Modify.setText(_translate("ChangePasswordDialog", "修改"))
        self.Cancel.setText(_translate("ChangePasswordDialog", "取消"))
        self.Title.setText(_translate("ChangePasswordDialog", "修改密码"))
        self.OldPasswordLabel.setText(_translate("ChangePasswordDialog", "旧密码"))
        self.NewPasswordLabel.setText(_translate("ChangePasswordDialog", "新密码"))
        self.NewPasswordAgainLabel.setText(_translate("ChangePasswordDialog", "确认密码"))
