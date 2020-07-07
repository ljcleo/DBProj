# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommentDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentDialog(object):
    def setupUi(self, CommentDialog):
        CommentDialog.setObjectName("CommentDialog")
        CommentDialog.resize(640, 360)
        self.RateLabel = QtWidgets.QLabel(CommentDialog)
        self.RateLabel.setGeometry(QtCore.QRect(90, 71, 411, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.RateLabel.setFont(font)
        self.RateLabel.setObjectName("RateLabel")
        self.OKButton = QtWidgets.QPushButton(CommentDialog)
        self.OKButton.setGeometry(QtCore.QRect(155, 281, 90, 28))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(CommentDialog)
        self.CancelButton.setGeometry(QtCore.QRect(395, 281, 90, 28))
        self.CancelButton.setObjectName("CancelButton")
        self.CommentText = QtWidgets.QPlainTextEdit(CommentDialog)
        self.CommentText.setGeometry(QtCore.QRect(90, 130, 461, 131))
        self.CommentText.setObjectName("CommentText")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(CommentDialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(330, 80, 70, 25))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMaximum(10.0)
        self.doubleSpinBox.setProperty("value", 10.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.retranslateUi(CommentDialog)
        self.CancelButton.clicked.connect(CommentDialog.reject)
        self.OKButton.clicked.connect(CommentDialog.comment)
        QtCore.QMetaObject.connectSlotsByName(CommentDialog)

    def retranslateUi(self, CommentDialog):
        _translate = QtCore.QCoreApplication.translate
        CommentDialog.setWindowTitle(_translate("CommentDialog", "评论"))
        self.RateLabel.setText(_translate("CommentDialog", "请选择您对该电影的评分："))
        self.OKButton.setText(_translate("CommentDialog", "评论"))
        self.CancelButton.setText(_translate("CommentDialog", "取消"))
        self.CommentText.setPlainText(_translate("CommentDialog", "请输入您的评论"))
