# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HintUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hint(object):
    def setupUi(self, Hint):
        Hint.setObjectName("Hint")
        Hint.resize(250, 100)
        self.label = QtWidgets.QLabel(Hint)
        self.label.setGeometry(QtCore.QRect(0, 35, 250, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Hint)
        QtCore.QMetaObject.connectSlotsByName(Hint)

    def retranslateUi(self, Hint):
        _translate = QtCore.QCoreApplication.translate
        Hint.setWindowTitle(_translate("Hint", "提示"))
        self.label.setText(_translate("Hint", "提示内容"))
