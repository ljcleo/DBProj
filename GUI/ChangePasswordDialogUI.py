# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePasswordDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.resize(300, 400)
        self.frame = QtWidgets.QFrame(ChangePasswordDialog)
        self.frame.setGeometry(QtCore.QRect(25, 25, 250, 350))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Modify = QtWidgets.QPushButton(self.frame)
        self.Modify.setGeometry(QtCore.QRect(25, 230, 90, 28))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Modify.setFont(font)
        self.Modify.setDefault(True)
        self.Modify.setObjectName("Modify")
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
        self.NewPasswordAgain = QtWidgets.QLineEdit(self.frame)
        self.NewPasswordAgain.setGeometry(QtCore.QRect(40, 180, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.NewPasswordAgain.setFont(font)
        self.NewPasswordAgain.setObjectName("NewPasswordAgain")
        self.NewPassword = QtWidgets.QLineEdit(self.frame)
        self.NewPassword.setGeometry(QtCore.QRect(40, 140, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.NewPassword.setFont(font)
        self.NewPassword.setAutoFillBackground(False)
        self.NewPassword.setObjectName("NewPassword")
        self.OldPassword = QtWidgets.QLineEdit(self.frame)
        self.OldPassword.setGeometry(QtCore.QRect(40, 100, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.OldPassword.setFont(font)
        self.OldPassword.setAutoFillBackground(False)
        self.OldPassword.setObjectName("OldPassword")

        self.retranslateUi(ChangePasswordDialog)
        self.Modify.clicked.connect(ChangePasswordDialog.changePassword)
        self.Cancel.clicked.connect(ChangePasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)
        ChangePasswordDialog.setTabOrder(self.NewPassword, self.NewPasswordAgain)
        ChangePasswordDialog.setTabOrder(self.NewPasswordAgain, self.Modify)
        ChangePasswordDialog.setTabOrder(self.Modify, self.Cancel)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "ChangePassword"))
        self.Modify.setText(_translate("ChangePasswordDialog", "修改"))
        self.Cancel.setText(_translate("ChangePasswordDialog", "取消"))
        self.Title.setText(_translate("ChangePasswordDialog", "XXX数据库"))
        self.NewPasswordAgain.setText(_translate("ChangePasswordDialog", "确认新密码"))
        self.NewPassword.setText(_translate("ChangePasswordDialog", "新密码"))
        self.OldPassword.setText(_translate("ChangePasswordDialog", "原密码"))
