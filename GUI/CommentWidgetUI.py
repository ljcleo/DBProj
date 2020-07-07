# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\CommentWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentWidget(object):
    def setupUi(self, CommentWidget):
        CommentWidget.setObjectName("CommentWidget")
        CommentWidget.resize(630, 130)
        self.NameLabel = QtWidgets.QLabel(CommentWidget)
        self.NameLabel.setGeometry(QtCore.QRect(10, 10, 480, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.RateLabel = QtWidgets.QLabel(CommentWidget)
        self.RateLabel.setGeometry(QtCore.QRect(500, 10, 80, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RateLabel.setFont(font)
        self.RateLabel.setObjectName("RateLabel")
        self.CommentText = QtWidgets.QTextBrowser(CommentWidget)
        self.CommentText.setGeometry(QtCore.QRect(10, 40, 580, 80))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 107, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 107, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.CommentText.setPalette(palette)
        self.CommentText.setAutoFillBackground(False)
        self.CommentText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CommentText.setAcceptRichText(False)
        self.CommentText.setObjectName("CommentText")

        self.retranslateUi(CommentWidget)
        QtCore.QMetaObject.connectSlotsByName(CommentWidget)

    def retranslateUi(self, CommentWidget):
        _translate = QtCore.QCoreApplication.translate
        CommentWidget.setWindowTitle(_translate("CommentWidget", "Form"))
        self.NameLabel.setText(_translate("CommentWidget", "张翠花"))
        self.RateLabel.setText(_translate("CommentWidget", "评分：8.5"))
        self.CommentText.setHtml(_translate("CommentWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。最好限制一下字数不然滚轮太多了。</p></body></html>"))
