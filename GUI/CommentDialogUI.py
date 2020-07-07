# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\CommentDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentDialog(object):
    def setupUi(self, CommentDialog):
        CommentDialog.setObjectName("CommentDialog")
        CommentDialog.resize(540, 270)
        self.RatingLabel = QtWidgets.QLabel(CommentDialog)
        self.RatingLabel.setGeometry(QtCore.QRect(30, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.RatingLabel.setFont(font)
        self.RatingLabel.setObjectName("RatingLabel")
        self.OKButton = QtWidgets.QPushButton(CommentDialog)
        self.OKButton.setGeometry(QtCore.QRect(320, 30, 90, 30))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(CommentDialog)
        self.CancelButton.setGeometry(QtCore.QRect(420, 30, 90, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.CommentText = QtWidgets.QPlainTextEdit(CommentDialog)
        self.CommentText.setGeometry(QtCore.QRect(30, 80, 480, 160))
        self.CommentText.setObjectName("CommentText")
        self.Rating = QtWidgets.QDoubleSpinBox(CommentDialog)
        self.Rating.setGeometry(QtCore.QRect(230, 30, 80, 30))
        self.Rating.setDecimals(1)
        self.Rating.setMaximum(10.0)
        self.Rating.setSingleStep(0.1)
        self.Rating.setObjectName("Rating")

        self.retranslateUi(CommentDialog)
        self.CancelButton.clicked.connect(CommentDialog.reject)
        self.OKButton.clicked.connect(CommentDialog.comment)
        QtCore.QMetaObject.connectSlotsByName(CommentDialog)

    def retranslateUi(self, CommentDialog):
        _translate = QtCore.QCoreApplication.translate
        CommentDialog.setWindowTitle(_translate("CommentDialog", "评论"))
        self.RatingLabel.setText(_translate("CommentDialog", "请选择您对该电影的评分："))
        self.OKButton.setText(_translate("CommentDialog", "评论"))
        self.CancelButton.setText(_translate("CommentDialog", "取消"))
        self.CommentText.setPlaceholderText(_translate("CommentDialog", "请输入您的评论"))
