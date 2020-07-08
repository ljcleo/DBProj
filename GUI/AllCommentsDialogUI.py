# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\AllCommentsDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AllCommentsDialog(object):
    def setupUi(self, AllCommentsDialog):
        AllCommentsDialog.setObjectName("AllCommentsDialog")
        AllCommentsDialog.resize(640, 520)
        self.CommentTable = QtWidgets.QTableWidget(AllCommentsDialog)
        self.CommentTable.setGeometry(QtCore.QRect(20, 140, 600, 360))
        self.CommentTable.setObjectName("CommentTable")
        self.CommentTable.setColumnCount(1)
        self.CommentTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setHorizontalHeaderItem(0, item)
        self.CommentTable.horizontalHeader().setVisible(False)
        self.CommentTable.horizontalHeader().setHighlightSections(False)
        self.Return = QtWidgets.QPushButton(AllCommentsDialog)
        self.Return.setGeometry(QtCore.QRect(520, 40, 100, 30))
        self.Return.setAutoDefault(False)
        self.Return.setObjectName("Return")
        self.CommentLabel = QtWidgets.QLabel(AllCommentsDialog)
        self.CommentLabel.setGeometry(QtCore.QRect(20, 100, 600, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CommentLabel.setFont(font)
        self.CommentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CommentLabel.setObjectName("CommentLabel")
        self.UserName = QtWidgets.QLabel(AllCommentsDialog)
        self.UserName.setGeometry(QtCore.QRect(20, 20, 480, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.UserName.setFont(font)
        self.UserName.setObjectName("UserName")
        self.Sex = QtWidgets.QLabel(AllCommentsDialog)
        self.Sex.setGeometry(QtCore.QRect(20, 60, 100, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Sex.setFont(font)
        self.Sex.setObjectName("Sex")
        self.Age = QtWidgets.QLabel(AllCommentsDialog)
        self.Age.setGeometry(QtCore.QRect(250, 60, 100, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")

        self.retranslateUi(AllCommentsDialog)
        self.Return.clicked.connect(AllCommentsDialog.accept)
        self.CommentTable.cellClicked['int','int'].connect(AllCommentsDialog.showMovieInfo)
        QtCore.QMetaObject.connectSlotsByName(AllCommentsDialog)

    def retranslateUi(self, AllCommentsDialog):
        _translate = QtCore.QCoreApplication.translate
        AllCommentsDialog.setWindowTitle(_translate("AllCommentsDialog", "评论信息"))
        item = self.CommentTable.horizontalHeaderItem(0)
        item.setText(_translate("AllCommentsDialog", "新建列"))
        self.Return.setText(_translate("AllCommentsDialog", "返回"))
        self.CommentLabel.setText(_translate("AllCommentsDialog", "管理员 某某的评论"))
        self.UserName.setText(_translate("AllCommentsDialog", "管理员 某某"))
        self.Sex.setText(_translate("AllCommentsDialog", "性别："))
        self.Age.setText(_translate("AllCommentsDialog", "年龄："))
