# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePasswordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(QtWidgets.QDialog):
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
        self.NewPasswordAgain.setGeometry(QtCore.QRect(45, 180, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.NewPasswordAgain.setFont(font)
        self.NewPasswordAgain.setObjectName("NewPasswordAgain")
        self.NewPassword = QtWidgets.QLineEdit(self.frame)
        self.NewPassword.setGeometry(QtCore.QRect(45, 140, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.NewPassword.setFont(font)
        self.NewPassword.setAutoFillBackground(False)
        self.NewPassword.setObjectName("NewPassword")
        self.OldPassword = QtWidgets.QLineEdit(self.frame)
        self.OldPassword.setGeometry(QtCore.QRect(45, 100, 160, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.OldPassword.setFont(font)
        self.OldPassword.setAutoFillBackground(False)
        self.OldPassword.setObjectName("OldPassword")

        self.Cancel.clicked.connect(self.destroy)

        self.retranslateUi(ChangePasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "ChangePassword"))
        self.Modify.setText(_translate("ChangePasswordDialog", "修改"))
        self.Cancel.setText(_translate("ChangePasswordDialog", "取消"))
        self.Title.setText(_translate("ChangePasswordDialog", "XXX数据库"))
        self.NewPasswordAgain.setText(_translate("ChangePasswordDialog", "确认新密码"))
        self.NewPassword.setText(_translate("ChangePasswordDialog", "新密码"))
        self.OldPassword.setText(_translate("ChangePasswordDialog", "旧密码"))

    def ModifyClicked(self):
        oldpassword = self.OldPassword.text()
        newpassword = self.NewPassword.text()
        newpasswordagain = self.NewPasswordAgain.text()
        # CHECK OLD PASSWORD HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if newpasswordagain != newpassword:
            print("两次输入的密码不一致！")
            return
        else:
            print("新密码：", newpassword)
            self.destroy()
        return


class Ui_LoginDialog(QtWidgets.QDialog):
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

        self.Register.clicked.connect(self.ToRegister)
        self.ChangePassword.clicked.connect(self.ToChangePassword)
        self.Cancel.clicked.connect(self.close)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

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

    def ToChangePassword(self):
        print("Must be called from an object")

    def ToRegister(self):
        print("Must be callde from an object")


class Ui_RegisterDialog(QtWidgets.QInputDialog):
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

        """
        QDialog 类应该有 close accept reject三个内置函数
        但是我好像只有close 跑个几次能成功一次 reject和accept都一直崩溃
        现在这边是这样的 这个注册界面 点取消 他调用close 把两次密码改成一样 点注册 他调用accept
       
        第一个问题是 我在登录界面点注册  这个注册界面他有时候显示 Recursive call detected 就不跳出来
        第二个问题是 在注册界面 点取消调用close正常 点注册调用accept就出问题了
        
        理想情况应该是 这个界面 可以反复跳出的。。
        """

        self.Register.clicked.connect(self.RegisterClicked)
        self.Cancel.clicked.connect(self.close)

        self.retranslateUi(RegisterDialog)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)

    def retranslateUi(self, RegisterDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "Register"))
        self.Register.setText(_translate("RegisterDialog", "注册"))
        self.Cancel.setText(_translate("RegisterDialog", "取消"))
        self.Title.setText(_translate("RegisterDialog", "XXX数据库"))
        self.PasswordAgain.setText(_translate("RegisterDialog", "确认密码"))
        self.Password.setText(_translate("RegisterDialog", "密码"))
        self.UserName.setText(_translate("RegisterDialog", "用户名"))

    def RegisterClicked(self):
        username = self.UserName.text()
        password = self.Password.text()
        passwordagain = self.PasswordAgain.text()
        if passwordagain != password:
            print("两次输入的密码不一致！")
            return
        else:
            print("用户名：", username)
            print("密码：", password)
            self.accept()
        return