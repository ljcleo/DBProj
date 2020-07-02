# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InformationPartUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InformationPart(object):
    def setupUi(self, InformationPart):
        InformationPart.setObjectName("InformationPart")
        InformationPart.resize(960, 640)
        self.HLineMovie = QtWidgets.QFrame(InformationPart)
        self.HLineMovie.setGeometry(QtCore.QRect(250, 340, 710, 20))
        self.HLineMovie.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HLineMovie.setFrameShape(QtWidgets.QFrame.HLine)
        self.HLineMovie.setObjectName("HLineMovie")
        self.InformationFrame = QtWidgets.QFrame(InformationPart)
        self.InformationFrame.setGeometry(QtCore.QRect(270, 10, 670, 330))
        self.InformationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InformationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InformationFrame.setObjectName("InformationFrame")
        self.Company = QtWidgets.QLabel(self.InformationFrame)
        self.Company.setGeometry(QtCore.QRect(250, 210, 220, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Company.setFont(font)
        self.Company.setObjectName("Company")
        self.OriginalName = QtWidgets.QLabel(self.InformationFrame)
        self.OriginalName.setGeometry(QtCore.QRect(250, 80, 240, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OriginalName.setFont(font)
        self.OriginalName.setObjectName("OriginalName")
        self.Director = QtWidgets.QLabel(self.InformationFrame)
        self.Director.setGeometry(QtCore.QRect(250, 240, 360, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Director.setFont(font)
        self.Director.setObjectName("Director")
        self.ChineseName = QtWidgets.QLabel(self.InformationFrame)
        self.ChineseName.setGeometry(QtCore.QRect(250, 40, 240, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ChineseName.setFont(font)
        self.ChineseName.setObjectName("ChineseName")
        self.ScoreLabel = QtWidgets.QLabel(self.InformationFrame)
        self.ScoreLabel.setGeometry(QtCore.QRect(510, 40, 60, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreLabel.setFont(font)
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.Cast = QtWidgets.QLabel(self.InformationFrame)
        self.Cast.setGeometry(QtCore.QRect(250, 270, 360, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Cast.setFont(font)
        self.Cast.setObjectName("Cast")
        self.Rate = QtWidgets.QLabel(self.InformationFrame)
        self.Rate.setGeometry(QtCore.QRect(510, 80, 80, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(191, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.Rate.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Rate.setFont(font)
        self.Rate.setAlignment(QtCore.Qt.AlignCenter)
        self.Rate.setObjectName("Rate")
        self.ReleaseDate = QtWidgets.QLabel(self.InformationFrame)
        self.ReleaseDate.setGeometry(QtCore.QRect(250, 150, 220, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.ReleaseDate.setFont(font)
        self.ReleaseDate.setObjectName("ReleaseDate")
        self.Length = QtWidgets.QLabel(self.InformationFrame)
        self.Length.setGeometry(QtCore.QRect(250, 180, 220, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Length.setFont(font)
        self.Length.setObjectName("Length")
        self.ReleaseDate_2 = QtWidgets.QLabel(self.InformationFrame)
        self.ReleaseDate_2.setGeometry(QtCore.QRect(250, 120, 220, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.ReleaseDate_2.setFont(font)
        self.ReleaseDate_2.setObjectName("ReleaseDate_2")
        self.ReturnHomepage = QtWidgets.QPushButton(self.InformationFrame)
        self.ReturnHomepage.setGeometry(QtCore.QRect(580, 300, 90, 28))
        self.ReturnHomepage.setAutoDefault(False)
        self.ReturnHomepage.setObjectName("ReturnHomepage")
        self.ModifyInformation = QtWidgets.QPushButton(self.InformationFrame)
        self.ModifyInformation.setGeometry(QtCore.QRect(250, 300, 90, 28))
        self.ModifyInformation.setAutoDefault(False)
        self.ModifyInformation.setObjectName("ModifyInformation")
        self.AllCast = QtWidgets.QPushButton(self.InformationFrame)
        self.AllCast.setGeometry(QtCore.QRect(619, 270, 51, 28))
        self.AllCast.setAutoDefault(False)
        self.AllCast.setObjectName("AllCast")
        self.AllDirector = QtWidgets.QPushButton(self.InformationFrame)
        self.AllDirector.setGeometry(QtCore.QRect(620, 240, 51, 28))
        self.AllDirector.setAutoDefault(False)
        self.AllDirector.setObjectName("AllDirector")
        self.CommentFrame = QtWidgets.QFrame(InformationPart)
        self.CommentFrame.setGeometry(QtCore.QRect(279, 379, 661, 231))
        self.CommentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CommentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CommentFrame.setObjectName("CommentFrame")
        self.Rate1 = QtWidgets.QLabel(self.CommentFrame)
        self.Rate1.setGeometry(QtCore.QRect(550, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Rate1.setFont(font)
        self.Rate1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rate1.setObjectName("Rate1")
        self.UserName2 = QtWidgets.QLabel(self.CommentFrame)
        self.UserName2.setGeometry(QtCore.QRect(30, 140, 80, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UserName2.setFont(font)
        self.UserName2.setObjectName("UserName2")
        self.UserName1 = QtWidgets.QLabel(self.CommentFrame)
        self.UserName1.setGeometry(QtCore.QRect(30, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UserName1.setFont(font)
        self.UserName1.setObjectName("UserName1")
        self.Comment2 = QtWidgets.QLabel(self.CommentFrame)
        self.Comment2.setGeometry(QtCore.QRect(30, 170, 600, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Comment2.setFont(font)
        self.Comment2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Comment2.setObjectName("Comment2")
        self.Rate2 = QtWidgets.QLabel(self.CommentFrame)
        self.Rate2.setGeometry(QtCore.QRect(550, 140, 80, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Rate2.setFont(font)
        self.Rate2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rate2.setObjectName("Rate2")
        self.CommentLabel = QtWidgets.QLabel(self.CommentFrame)
        self.CommentLabel.setGeometry(QtCore.QRect(30, 0, 61, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.CommentLabel.setFont(font)
        self.CommentLabel.setObjectName("CommentLabel")
        self.Comment1 = QtWidgets.QLabel(self.CommentFrame)
        self.Comment1.setGeometry(QtCore.QRect(30, 80, 600, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.Comment1.setFont(font)
        self.Comment1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Comment1.setObjectName("Comment1")
        self.AddComment = QtWidgets.QPushButton(self.CommentFrame)
        self.AddComment.setGeometry(QtCore.QRect(570, 10, 90, 28))
        self.AddComment.setAutoDefault(True)
        self.AddComment.setDefault(True)
        self.AddComment.setObjectName("AddComment")

        self.retranslateUi(InformationPart)
        self.AddComment.clicked.connect(InformationPart.addComment)
        self.ReturnHomepage.clicked.connect(InformationPart.returnHomepage)
        self.ModifyInformation.clicked.connect(InformationPart.modifyInformation)
        self.AllDirector.clicked.connect(InformationPart.showAllDirector)
        self.AllCast.clicked.connect(InformationPart.showAllCast)
        QtCore.QMetaObject.connectSlotsByName(InformationPart)

    def retranslateUi(self, InformationPart):
        _translate = QtCore.QCoreApplication.translate
        InformationPart.setWindowTitle(_translate("InformationPart", "Information"))
        self.Company.setText(_translate("InformationPart", "发行公司：迪士尼（美国）"))
        self.OriginalName.setText(_translate("InformationPart", "Zootopia"))
        self.Director.setText(_translate("InformationPart", "导演：拜伦·霍华德/瑞奇·摩尔/杰拉德·布什"))
        self.ChineseName.setText(_translate("InformationPart", "疯狂动物城"))
        self.ScoreLabel.setText(_translate("InformationPart", "评分"))
        self.Cast.setText(_translate("InformationPart", "主演：金妮弗·古德温/杰森·贝特曼 ..."))
        self.Rate.setText(_translate("InformationPart", "4.8/5"))
        self.ReleaseDate.setText(_translate("InformationPart", "上映日期：2020/6/10"))
        self.Length.setText(_translate("InformationPart", "片长：120分钟"))
        self.ReleaseDate_2.setText(_translate("InformationPart", "类型：喜剧/动画/冒险"))
        self.ReturnHomepage.setText(_translate("InformationPart", "返回主页"))
        self.ModifyInformation.setText(_translate("InformationPart", "修改信息"))
        self.AllCast.setText(_translate("InformationPart", "..."))
        self.AllDirector.setText(_translate("InformationPart", "..."))
        self.Rate1.setText(_translate("InformationPart", "评分：5"))
        self.UserName2.setText(_translate("InformationPart", "李铁柱"))
        self.UserName1.setText(_translate("InformationPart", "张翠花"))
        self.Comment2.setText(_translate("InformationPart", "舒服了舒服了舒服了舒服了舒服了舒服了舒服了舒服了舒服了舒服了"))
        self.Rate2.setText(_translate("InformationPart", "评分：5"))
        self.CommentLabel.setText(_translate("InformationPart", "评论"))
        self.Comment1.setText(_translate("InformationPart", "不会真有人不喜欢这部电影吧不会吧不会吧不会吧不会吧不会吧不会吧"))
        self.AddComment.setText(_translate("InformationPart", "添加评论"))