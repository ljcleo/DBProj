# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\InformationPartUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
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
        self.CompanyLabel = QtWidgets.QLabel(self.InformationFrame)
        self.CompanyLabel.setGeometry(QtCore.QRect(250, 210, 80, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.CompanyLabel.setFont(font)
        self.CompanyLabel.setObjectName("CompanyLabel")
        self.OriginalName = QtWidgets.QLabel(self.InformationFrame)
        self.OriginalName.setGeometry(QtCore.QRect(250, 80, 320, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.OriginalName.setFont(font)
        self.OriginalName.setObjectName("OriginalName")
        self.DirectorLabel = QtWidgets.QLabel(self.InformationFrame)
        self.DirectorLabel.setGeometry(QtCore.QRect(250, 240, 80, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.DirectorLabel.setFont(font)
        self.DirectorLabel.setObjectName("DirectorLabel")
        self.ChineseName = QtWidgets.QLabel(self.InformationFrame)
        self.ChineseName.setGeometry(QtCore.QRect(250, 40, 320, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ChineseName.setFont(font)
        self.ChineseName.setObjectName("ChineseName")
        self.ScoreLabel = QtWidgets.QLabel(self.InformationFrame)
        self.ScoreLabel.setGeometry(QtCore.QRect(610, 40, 60, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreLabel.setFont(font)
        self.ScoreLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.CastLabel = QtWidgets.QLabel(self.InformationFrame)
        self.CastLabel.setGeometry(QtCore.QRect(250, 270, 80, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.CastLabel.setFont(font)
        self.CastLabel.setObjectName("CastLabel")
        self.Rating = QtWidgets.QLabel(self.InformationFrame)
        self.Rating.setGeometry(QtCore.QRect(590, 80, 80, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(191, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Rating.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Rating.setFont(font)
        self.Rating.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rating.setObjectName("Rating")
        self.ReleaseDateLabel = QtWidgets.QLabel(self.InformationFrame)
        self.ReleaseDateLabel.setGeometry(QtCore.QRect(250, 150, 80, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.ReleaseDateLabel.setFont(font)
        self.ReleaseDateLabel.setObjectName("ReleaseDateLabel")
        self.LengthLabel = QtWidgets.QLabel(self.InformationFrame)
        self.LengthLabel.setGeometry(QtCore.QRect(250, 180, 80, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.LengthLabel.setFont(font)
        self.LengthLabel.setObjectName("LengthLabel")
        self.GenreLabel = QtWidgets.QLabel(self.InformationFrame)
        self.GenreLabel.setGeometry(QtCore.QRect(250, 120, 80, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.GenreLabel.setFont(font)
        self.GenreLabel.setObjectName("GenreLabel")
        self.ReturnHomepage = QtWidgets.QPushButton(self.InformationFrame)
        self.ReturnHomepage.setGeometry(QtCore.QRect(580, 300, 90, 28))
        self.ReturnHomepage.setAutoDefault(False)
        self.ReturnHomepage.setObjectName("ReturnHomepage")
        self.ModifyInformation = QtWidgets.QPushButton(self.InformationFrame)
        self.ModifyInformation.setGeometry(QtCore.QRect(250, 300, 90, 28))
        self.ModifyInformation.setAutoDefault(False)
        self.ModifyInformation.setObjectName("ModifyInformation")
        self.AllCast = QtWidgets.QPushButton(self.InformationFrame)
        self.AllCast.setGeometry(QtCore.QRect(620, 266, 50, 28))
        self.AllCast.setAutoDefault(False)
        self.AllCast.setObjectName("AllCast")
        self.AllDirector = QtWidgets.QPushButton(self.InformationFrame)
        self.AllDirector.setGeometry(QtCore.QRect(620, 236, 50, 28))
        self.AllDirector.setAutoDefault(False)
        self.AllDirector.setObjectName("AllDirector")
        self.Genre = QtWidgets.QLabel(self.InformationFrame)
        self.Genre.setGeometry(QtCore.QRect(330, 120, 280, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Genre.setFont(font)
        self.Genre.setObjectName("Genre")
        self.ReleaseDate = QtWidgets.QLabel(self.InformationFrame)
        self.ReleaseDate.setGeometry(QtCore.QRect(330, 150, 280, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.ReleaseDate.setFont(font)
        self.ReleaseDate.setObjectName("ReleaseDate")
        self.Length = QtWidgets.QLabel(self.InformationFrame)
        self.Length.setGeometry(QtCore.QRect(330, 180, 280, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Length.setFont(font)
        self.Length.setObjectName("Length")
        self.Company = QtWidgets.QLabel(self.InformationFrame)
        self.Company.setGeometry(QtCore.QRect(330, 210, 280, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Company.setFont(font)
        self.Company.setObjectName("Company")
        self.Director = QtWidgets.QLabel(self.InformationFrame)
        self.Director.setGeometry(QtCore.QRect(330, 240, 280, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Director.setFont(font)
        self.Director.setObjectName("Director")
        self.Cast = QtWidgets.QLabel(self.InformationFrame)
        self.Cast.setGeometry(QtCore.QRect(330, 270, 280, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Cast.setFont(font)
        self.Cast.setObjectName("Cast")
        self.Picture = QtWidgets.QLabel(self.InformationFrame)
        self.Picture.setGeometry(QtCore.QRect(40, 40, 180, 254))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.Picture.setFont(font)
        self.Picture.setScaledContents(True)
        self.Picture.setAlignment(QtCore.Qt.AlignCenter)
        self.Picture.setObjectName("Picture")
        self.CommentFrame = QtWidgets.QFrame(InformationPart)
        self.CommentFrame.setGeometry(QtCore.QRect(280, 380, 660, 230))
        self.CommentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CommentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CommentFrame.setObjectName("CommentFrame")
        self.CommentLabel = QtWidgets.QLabel(self.CommentFrame)
        self.CommentLabel.setGeometry(QtCore.QRect(30, 0, 61, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CommentLabel.setFont(font)
        self.CommentLabel.setObjectName("CommentLabel")
        self.AddComment = QtWidgets.QPushButton(self.CommentFrame)
        self.AddComment.setGeometry(QtCore.QRect(540, 0, 120, 28))
        self.AddComment.setAutoDefault(True)
        self.AddComment.setDefault(True)
        self.AddComment.setObjectName("AddComment")
        self.ToStoryLine = QtWidgets.QPushButton(self.CommentFrame)
        self.ToStoryLine.setGeometry(QtCore.QRect(570, 200, 90, 28))
        self.ToStoryLine.setAutoDefault(True)
        self.ToStoryLine.setDefault(True)
        self.ToStoryLine.setObjectName("ToStoryLine")
        self.CommentTable = QtWidgets.QTableWidget(self.CommentFrame)
        self.CommentTable.setGeometry(QtCore.QRect(30, 50, 630, 130))
        self.CommentTable.setObjectName("CommentTable")
        self.CommentTable.setColumnCount(1)
        self.CommentTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommentTable.setHorizontalHeaderItem(0, item)
        self.CommentTable.horizontalHeader().setVisible(False)
        self.CommentTable.verticalHeader().setVisible(False)
        self.MoreInformationFrame = QtWidgets.QFrame(InformationPart)
        self.MoreInformationFrame.setGeometry(QtCore.QRect(280, 380, 660, 230))
        self.MoreInformationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MoreInformationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MoreInformationFrame.setObjectName("MoreInformationFrame")
        self.StorylineLabel = QtWidgets.QLabel(self.MoreInformationFrame)
        self.StorylineLabel.setGeometry(QtCore.QRect(150, 0, 60, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.StorylineLabel.setFont(font)
        self.StorylineLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StorylineLabel.setObjectName("StorylineLabel")
        self.Storyline = QtWidgets.QTextBrowser(self.MoreInformationFrame)
        self.Storyline.setGeometry(QtCore.QRect(20, 40, 320, 140))
        self.Storyline.setObjectName("Storyline")
        self.PrizeHistoryLabel = QtWidgets.QLabel(self.MoreInformationFrame)
        self.PrizeHistoryLabel.setGeometry(QtCore.QRect(460, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PrizeHistoryLabel.setFont(font)
        self.PrizeHistoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PrizeHistoryLabel.setObjectName("PrizeHistoryLabel")
        self.PrizeHistory = QtWidgets.QTextBrowser(self.MoreInformationFrame)
        self.PrizeHistory.setGeometry(QtCore.QRect(400, 40, 240, 140))
        self.PrizeHistory.setObjectName("PrizeHistory")
        self.ToComment = QtWidgets.QPushButton(self.MoreInformationFrame)
        self.ToComment.setGeometry(QtCore.QRect(570, 200, 90, 28))
        self.ToComment.setAutoDefault(True)
        self.ToComment.setDefault(True)
        self.ToComment.setObjectName("ToComment")
        self.DirectorLabel.setBuddy(self.AllDirector)
        self.CastLabel.setBuddy(self.AllCast)
        self.StorylineLabel.setBuddy(self.Storyline)
        self.PrizeHistoryLabel.setBuddy(self.PrizeHistory)

        self.retranslateUi(InformationPart)
        self.AddComment.clicked.connect(InformationPart.addComment)
        self.ReturnHomepage.clicked.connect(InformationPart.returnHomepage)
        self.AllDirector.clicked.connect(InformationPart.showAllDirector)
        self.AllCast.clicked.connect(InformationPart.showAllCast)
        self.ModifyInformation.clicked.connect(InformationPart.modifyMovie)
        self.ToStoryLine.clicked.connect(InformationPart.toStoryline)
        self.ToComment.clicked.connect(InformationPart.toComment)
        QtCore.QMetaObject.connectSlotsByName(InformationPart)
        InformationPart.setTabOrder(self.AllDirector, self.AllCast)
        InformationPart.setTabOrder(self.AllCast, self.ModifyInformation)
        InformationPart.setTabOrder(self.ModifyInformation, self.ReturnHomepage)
        InformationPart.setTabOrder(self.ReturnHomepage, self.Storyline)
        InformationPart.setTabOrder(self.Storyline, self.PrizeHistory)
        InformationPart.setTabOrder(self.PrizeHistory, self.ToComment)
        InformationPart.setTabOrder(self.ToComment, self.AddComment)
        InformationPart.setTabOrder(self.AddComment, self.ToStoryLine)

    def retranslateUi(self, InformationPart):
        _translate = QtCore.QCoreApplication.translate
        InformationPart.setWindowTitle(_translate("InformationPart", "Information"))
        self.CompanyLabel.setText(_translate("InformationPart", "发行公司："))
        self.OriginalName.setText(_translate("InformationPart", "Zootopia"))
        self.DirectorLabel.setText(_translate("InformationPart", "导演："))
        self.ChineseName.setText(_translate("InformationPart", "疯狂动物城"))
        self.ScoreLabel.setText(_translate("InformationPart", "评分"))
        self.CastLabel.setText(_translate("InformationPart", "主演："))
        self.Rating.setText(_translate("InformationPart", "9.8/10"))
        self.ReleaseDateLabel.setText(_translate("InformationPart", "上映日期："))
        self.LengthLabel.setText(_translate("InformationPart", "片长："))
        self.GenreLabel.setText(_translate("InformationPart", "类型："))
        self.ReturnHomepage.setText(_translate("InformationPart", "返回主页"))
        self.ModifyInformation.setText(_translate("InformationPart", "修改信息"))
        self.AllCast.setText(_translate("InformationPart", "..."))
        self.AllDirector.setText(_translate("InformationPart", "..."))
        self.Genre.setText(_translate("InformationPart", "类型"))
        self.ReleaseDate.setText(_translate("InformationPart", "日期"))
        self.Length.setText(_translate("InformationPart", "分钟"))
        self.Company.setText(_translate("InformationPart", "公司（地点）"))
        self.Director.setText(_translate("InformationPart", "导演"))
        self.Cast.setText(_translate("InformationPart", "主演"))
        self.CommentLabel.setText(_translate("InformationPart", "评论"))
        self.AddComment.setText(_translate("InformationPart", "添加/修改评论"))
        self.ToStoryLine.setText(_translate("InformationPart", "查看简介"))
        item = self.CommentTable.verticalHeaderItem(0)
        item.setText(_translate("InformationPart", "新建行"))
        item = self.CommentTable.verticalHeaderItem(1)
        item.setText(_translate("InformationPart", "新建行"))
        item = self.CommentTable.verticalHeaderItem(2)
        item.setText(_translate("InformationPart", "新建行"))
        item = self.CommentTable.verticalHeaderItem(3)
        item.setText(_translate("InformationPart", "新建行"))
        item = self.CommentTable.verticalHeaderItem(4)
        item.setText(_translate("InformationPart", "新建行"))
        item = self.CommentTable.horizontalHeaderItem(0)
        item.setText(_translate("InformationPart", "新建列"))
        self.StorylineLabel.setText(_translate("InformationPart", "简介"))
        self.Storyline.setHtml(_translate("InformationPart", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介这是简介</p></body></html>"))
        self.PrizeHistoryLabel.setText(_translate("InformationPart", "获奖信息"))
        self.PrizeHistory.setHtml(_translate("InformationPart", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息这是获奖信息</p></body></html>"))
        self.ToComment.setText(_translate("InformationPart", "查看评论"))
