# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceFQztUQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
# IMPORT CUSTOM WIDGETS
from custom_qstacked_widgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(446, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border: none;\n"
"font: 55 12pt url(:/fonts/resources/fonts/PlayfairDisplay-VariableFont_wght.ttf);\n"
"background:  transparent;\n"
"color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));\n"
"}\n"
"QProgressBar {\n"
"    background-color: #1a2127;\n"
"    border:  rgb(41, 52, 61);\n"
"    color:  #fff;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"        background-color:  qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(85, 255, 255, 255));\n"
"        color: #fff;\n"
"        border-radius: 5px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.myStackedWidget = QStackedWidget(self.centralwidget)
        self.myStackedWidget.setObjectName(u"myStackedWidget")
        self.myStackedWidget.setMaximumSize(QSize(300, 450))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/images/resources/images/3.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.myStackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/images/resources/images/4.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.myStackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/images/resources/images/8.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.myStackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/images/resources/images/2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.myStackedWidget.addWidget(self.page)

        self.horizontalLayout.addWidget(self.myStackedWidget)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(37, 106, 112);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nxt = QPushButton(self.frame_4)
        self.nxt.setObjectName(u"nxt")

        self.verticalLayout_4.addWidget(self.nxt)

        self.prev = QPushButton(self.frame_4)
        self.prev.setObjectName(u"prev")

        self.verticalLayout_4.addWidget(self.prev)

        self.page1 = QPushButton(self.frame_4)
        self.page1.setObjectName(u"page1")

        self.verticalLayout_4.addWidget(self.page1)

        self.page2 = QPushButton(self.frame_4)
        self.page2.setObjectName(u"page2")

        self.verticalLayout_4.addWidget(self.page2)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.nxt.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"Previous Page ", None))
        self.page1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.page2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
    # retranslateUi

