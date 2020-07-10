# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBProj\GUI\HomepagePartUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomepagePart(object):
    def setupUi(self, HomepagePart):
        HomepagePart.setObjectName("HomepagePart")
        HomepagePart.resize(960, 640)
        self.HLineSearch = QtWidgets.QFrame(HomepagePart)
        self.HLineSearch.setGeometry(QtCore.QRect(250, 180, 710, 20))
        self.HLineSearch.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HLineSearch.setFrameShape(QtWidgets.QFrame.HLine)
        self.HLineSearch.setObjectName("HLineSearch")
        self.RecommendationFrame = QtWidgets.QFrame(HomepagePart)
        self.RecommendationFrame.setGeometry(QtCore.QRect(260, 210, 680, 410))
        self.RecommendationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RecommendationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RecommendationFrame.setObjectName("RecommendationFrame")
        self.RecommendationLabel = QtWidgets.QLabel(self.RecommendationFrame)
        self.RecommendationLabel.setGeometry(QtCore.QRect(30, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.RecommendationLabel.setFont(font)
        self.RecommendationLabel.setObjectName("RecommendationLabel")
        self.RecommendationPicture1 = QtWidgets.QLabel(self.RecommendationFrame)
        self.RecommendationPicture1.setGeometry(QtCore.QRect(10, 80, 180, 254))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.RecommendationPicture1.setFont(font)
        self.RecommendationPicture1.setScaledContents(True)
        self.RecommendationPicture1.setAlignment(QtCore.Qt.AlignCenter)
        self.RecommendationPicture1.setObjectName("RecommendationPicture1")
        self.RecommendationPicture2 = QtWidgets.QLabel(self.RecommendationFrame)
        self.RecommendationPicture2.setGeometry(QtCore.QRect(250, 80, 180, 254))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.RecommendationPicture2.setFont(font)
        self.RecommendationPicture2.setScaledContents(True)
        self.RecommendationPicture2.setAlignment(QtCore.Qt.AlignCenter)
        self.RecommendationPicture2.setObjectName("RecommendationPicture2")
        self.RecommendationPicture3 = QtWidgets.QLabel(self.RecommendationFrame)
        self.RecommendationPicture3.setGeometry(QtCore.QRect(490, 80, 180, 254))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.RecommendationPicture3.setFont(font)
        self.RecommendationPicture3.setScaledContents(True)
        self.RecommendationPicture3.setAlignment(QtCore.Qt.AlignCenter)
        self.RecommendationPicture3.setObjectName("RecommendationPicture3")
        self.Recommendation1 = QtWidgets.QPushButton(self.RecommendationFrame)
        self.Recommendation1.setGeometry(QtCore.QRect(0, 70, 200, 320))
        self.Recommendation1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Recommendation1.setStyleSheet("QPushButton#Recommendation1\n"
"{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton#Recommendation1:hover\n"
"{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 64);\n"
"}")
        self.Recommendation1.setObjectName("Recommendation1")
        self.Recommendation2 = QtWidgets.QPushButton(self.RecommendationFrame)
        self.Recommendation2.setGeometry(QtCore.QRect(240, 70, 200, 320))
        self.Recommendation2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Recommendation2.setStyleSheet("QPushButton#Recommendation2\n"
"{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton#Recommendation2:hover\n"
"{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 64);\n"
"}")
        self.Recommendation2.setObjectName("Recommendation2")
        self.Recommendation3 = QtWidgets.QPushButton(self.RecommendationFrame)
        self.Recommendation3.setGeometry(QtCore.QRect(480, 70, 200, 320))
        self.Recommendation3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Recommendation3.setStyleSheet("QPushButton#Recommendation3\n"
"{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton#Recommendation3:hover\n"
"{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 64);\n"
"}")
        self.Recommendation3.setObjectName("Recommendation3")
        self.RecommendationTitle1 = ScrollLabel(self.RecommendationFrame)
        self.RecommendationTitle1.setGeometry(QtCore.QRect(10, 350, 180, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RecommendationTitle1.setFont(font)
        self.RecommendationTitle1.setAlignment(QtCore.Qt.AlignCenter)
        self.RecommendationTitle1.setObjectName("RecommendationTitle1")
        self.RecommendationTitle2 = ScrollLabel(self.RecommendationFrame)
        self.RecommendationTitle2.setGeometry(QtCore.QRect(250, 350, 180, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RecommendationTitle2.setFont(font)
        self.RecommendationTitle2.setAlignment(QtCore.Qt.AlignCenter)
        self.RecommendationTitle2.setObjectName("RecommendationTitle2")
        self.RecommendationTitle3 = ScrollLabel(self.RecommendationFrame)
        self.RecommendationTitle3.setGeometry(QtCore.QRect(490, 350, 180, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RecommendationTitle3.setFont(font)
        self.RecommendationTitle3.setAlignment(QtCore.Qt.AlignCenter)
        self.RecommendationTitle3.setObjectName("RecommendationTitle3")
        self.RecommendationLabel.raise_()
        self.RecommendationPicture1.raise_()
        self.RecommendationPicture2.raise_()
        self.RecommendationPicture3.raise_()
        self.RecommendationTitle1.raise_()
        self.RecommendationTitle2.raise_()
        self.RecommendationTitle3.raise_()
        self.Recommendation1.raise_()
        self.Recommendation2.raise_()
        self.Recommendation3.raise_()
        self.SearchFrame = QtWidgets.QFrame(HomepagePart)
        self.SearchFrame.setGeometry(QtCore.QRect(320, 60, 570, 80))
        self.SearchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchFrame.setObjectName("SearchFrame")
        self.SearchInput = QtWidgets.QLineEdit(self.SearchFrame)
        self.SearchInput.setGeometry(QtCore.QRect(30, 20, 425, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.SearchInput.setFont(font)
        self.SearchInput.setObjectName("SearchInput")
        self.Search = QtWidgets.QPushButton(self.SearchFrame)
        self.Search.setGeometry(QtCore.QRect(470, 20, 75, 30))
        self.Search.setAutoDefault(True)
        self.Search.setDefault(True)
        self.Search.setObjectName("Search")

        self.retranslateUi(HomepagePart)
        self.Recommendation2.clicked.connect(HomepagePart.movie2)
        self.Recommendation1.clicked.connect(HomepagePart.movie1)
        self.Recommendation3.clicked.connect(HomepagePart.movie3)
        self.Search.clicked.connect(HomepagePart.search)
        QtCore.QMetaObject.connectSlotsByName(HomepagePart)
        HomepagePart.setTabOrder(self.SearchInput, self.Search)

    def retranslateUi(self, HomepagePart):
        _translate = QtCore.QCoreApplication.translate
        self.RecommendationLabel.setText(_translate("HomepagePart", "今日推荐"))
        self.RecommendationPicture1.setText(_translate("HomepagePart", "海报"))
        self.RecommendationPicture2.setText(_translate("HomepagePart", "海报"))
        self.RecommendationPicture3.setText(_translate("HomepagePart", "海报"))
        self.RecommendationTitle1.setText(_translate("HomepagePart", "电影名称"))
        self.RecommendationTitle2.setText(_translate("HomepagePart", "电影名称"))
        self.RecommendationTitle3.setText(_translate("HomepagePart", "电影名称"))
        self.SearchInput.setPlaceholderText(_translate("HomepagePart", "请输入您想搜索的影片"))
        self.Search.setText(_translate("HomepagePart", "搜索"))
        self.Search.setShortcut(_translate("HomepagePart", "Return"))
from DBProj.GUI.ScrollLabel import ScrollLabel
