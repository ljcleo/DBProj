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
        self.horizontalLayoutWidget = QtWidgets.QWidget(CommentDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 110, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.RateLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.RateLayout.setContentsMargins(0, 0, 0, 0)
        self.RateLayout.setObjectName("RateLayout")
        self.Rate1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Rate1.setObjectName("Rate1")
        self.RateLayout.addWidget(self.Rate1)
        self.Rate2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Rate2.setObjectName("Rate2")
        self.RateLayout.addWidget(self.Rate2)
        self.Rate3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Rate3.setObjectName("Rate3")
        self.RateLayout.addWidget(self.Rate3)
        self.Rate4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Rate4.setObjectName("Rate4")
        self.RateLayout.addWidget(self.Rate4)
        self.Rate5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Rate5.setChecked(True)
        self.Rate5.setObjectName("Rate5")
        self.RateLayout.addWidget(self.Rate5)
        self.RateLabel = QtWidgets.QLabel(CommentDialog)
        self.RateLabel.setGeometry(QtCore.QRect(100, 60, 411, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.RateLabel.setFont(font)
        self.RateLabel.setObjectName("RateLabel")
        self.OKButton = QtWidgets.QPushButton(CommentDialog)
        self.OKButton.setGeometry(QtCore.QRect(155, 300, 90, 28))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(CommentDialog)
        self.CancelButton.setGeometry(QtCore.QRect(395, 300, 90, 28))
        self.CancelButton.setObjectName("CancelButton")
        self.CommentText = QtWidgets.QPlainTextEdit(CommentDialog)
        self.CommentText.setGeometry(QtCore.QRect(100, 160, 440, 120))
        self.CommentText.setObjectName("CommentText")

        self.retranslateUi(CommentDialog)
        self.CancelButton.clicked.connect(CommentDialog.reject)
        self.OKButton.clicked.connect(CommentDialog.comment)
        QtCore.QMetaObject.connectSlotsByName(CommentDialog)

    def retranslateUi(self, CommentDialog):
        _translate = QtCore.QCoreApplication.translate
        CommentDialog.setWindowTitle(_translate("CommentDialog", "评论"))
        self.Rate1.setText(_translate("CommentDialog", "1"))
        self.Rate2.setText(_translate("CommentDialog", "2"))
        self.Rate3.setText(_translate("CommentDialog", "3"))
        self.Rate4.setText(_translate("CommentDialog", "4"))
        self.Rate5.setText(_translate("CommentDialog", "5"))
        self.RateLabel.setText(_translate("CommentDialog", "请选择您对该电影的评分："))
        self.OKButton.setText(_translate("CommentDialog", "评论"))
        self.CancelButton.setText(_translate("CommentDialog", "取消"))
        self.CommentText.setPlainText(_translate("CommentDialog", "请输入您的评论"))
