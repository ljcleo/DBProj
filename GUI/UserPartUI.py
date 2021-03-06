# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBProj\GUI\UserPartUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserPart(object):
    def setupUi(self, UserPart):
        UserPart.setObjectName("UserPart")
        UserPart.resize(960, 640)
        self.UserFrame = QtWidgets.QFrame(UserPart)
        self.UserFrame.setGeometry(QtCore.QRect(65, 150, 120, 380))
        self.UserFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UserFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UserFrame.setObjectName("UserFrame")
        self.Logout = QtWidgets.QPushButton(self.UserFrame)
        self.Logout.setGeometry(QtCore.QRect(0, 300, 120, 30))
        self.Logout.setAutoDefault(False)
        self.Logout.setDefault(False)
        self.Logout.setObjectName("Logout")
        self.UserQuit = QtWidgets.QPushButton(self.UserFrame)
        self.UserQuit.setGeometry(QtCore.QRect(0, 350, 120, 30))
        self.UserQuit.setAutoDefault(False)
        self.UserQuit.setObjectName("UserQuit")
        self.ModifyInformation = QtWidgets.QPushButton(self.UserFrame)
        self.ModifyInformation.setGeometry(QtCore.QRect(0, 200, 120, 30))
        self.ModifyInformation.setAutoDefault(False)
        self.ModifyInformation.setDefault(False)
        self.ModifyInformation.setObjectName("ModifyInformation")
        self.UserWelcomeLabel = QtWidgets.QLabel(self.UserFrame)
        self.UserWelcomeLabel.setGeometry(QtCore.QRect(0, 0, 121, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.UserWelcomeLabel.setFont(font)
        self.UserWelcomeLabel.setScaledContents(False)
        self.UserWelcomeLabel.setObjectName("UserWelcomeLabel")
        self.UserNameLabel = ScrollLabel(self.UserFrame)
        self.UserNameLabel.setGeometry(QtCore.QRect(-1, 40, 121, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.UserNameLabel.setFont(font)
        self.UserNameLabel.setScaledContents(False)
        self.UserNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UserNameLabel.setObjectName("UserNameLabel")
        self.ChangePassword = QtWidgets.QPushButton(self.UserFrame)
        self.ChangePassword.setGeometry(QtCore.QRect(0, 250, 120, 30))
        self.ChangePassword.setAutoDefault(False)
        self.ChangePassword.setDefault(False)
        self.ChangePassword.setObjectName("ChangePassword")
        self.ManageSubInfo = QtWidgets.QPushButton(self.UserFrame)
        self.ManageSubInfo.setGeometry(QtCore.QRect(0, 150, 120, 30))
        self.ManageSubInfo.setAutoDefault(False)
        self.ManageSubInfo.setDefault(False)
        self.ManageSubInfo.setObjectName("ManageSubInfo")
        self.ShowComment = QtWidgets.QPushButton(self.UserFrame)
        self.ShowComment.setGeometry(QtCore.QRect(0, 100, 120, 30))
        self.ShowComment.setAutoDefault(False)
        self.ShowComment.setDefault(False)
        self.ShowComment.setObjectName("ShowComment")

        self.retranslateUi(UserPart)
        self.ChangePassword.clicked.connect(UserPart.changePassword)
        self.Logout.clicked.connect(UserPart.logout)
        self.ModifyInformation.clicked.connect(UserPart.modifyInformation)
        self.UserQuit.clicked.connect(UserPart.close)
        self.ShowComment.clicked.connect(UserPart.showMyComments)
        self.ManageSubInfo.clicked.connect(UserPart.manageSubInfo)
        QtCore.QMetaObject.connectSlotsByName(UserPart)
        UserPart.setTabOrder(self.ShowComment, self.ManageSubInfo)
        UserPart.setTabOrder(self.ManageSubInfo, self.ModifyInformation)
        UserPart.setTabOrder(self.ModifyInformation, self.ChangePassword)
        UserPart.setTabOrder(self.ChangePassword, self.Logout)
        UserPart.setTabOrder(self.Logout, self.UserQuit)

    def retranslateUi(self, UserPart):
        _translate = QtCore.QCoreApplication.translate
        self.Logout.setText(_translate("UserPart", "退出登录"))
        self.UserQuit.setText(_translate("UserPart", "退出系统"))
        self.ModifyInformation.setText(_translate("UserPart", "修改个人信息"))
        self.UserWelcomeLabel.setText(_translate("UserPart", "欢迎，"))
        self.UserNameLabel.setText(_translate("UserPart", "用户昵称"))
        self.ChangePassword.setText(_translate("UserPart", "修改密码"))
        self.ManageSubInfo.setText(_translate("UserPart", "附属信息管理"))
        self.ShowComment.setText(_translate("UserPart", "查看我的主页"))
from DBProj.GUI.ScrollLabel import ScrollLabel
