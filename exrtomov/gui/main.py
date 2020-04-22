# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        if not MainAppWindow.objectName():
            MainAppWindow.setObjectName(u"MainAppWindow")
        MainAppWindow.resize(723, 252)
        font = QFont()
        font.setPointSize(14)
        MainAppWindow.setFont(font)
        self.centralwidget = QWidget(MainAppWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainAppFrame = QFrame(self.centralwidget)
        self.mainAppFrame.setObjectName(u"mainAppFrame")
        self.mainAppFrame.setFrameShape(QFrame.StyledPanel)
        self.mainAppFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.mainAppFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.mainAppFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.mainAppFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.exrFolderButton = QPushButton(self.frame_3)
        self.exrFolderButton.setObjectName(u"exrFolderButton")

        self.gridLayout_2.addWidget(self.exrFolderButton, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.movFolderButton = QPushButton(self.frame_3)
        self.movFolderButton.setObjectName(u"movFolderButton")

        self.gridLayout_2.addWidget(self.movFolderButton, 1, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.conversionButton = QPushButton(self.frame_5)
        self.conversionButton.setObjectName(u"conversionButton")

        self.gridLayout_5.addWidget(self.conversionButton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.mainAppFrame, 0, 0, 1, 1)

        MainAppWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainAppWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainAppWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainAppWindow)

        QMetaObject.connectSlotsByName(MainAppWindow)
    # setupUi

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(QCoreApplication.translate("MainAppWindow", u"Converter v0.1", None))
        self.label.setText(QCoreApplication.translate("MainAppWindow", u"Converter", None))
        self.exrFolderButton.setText(QCoreApplication.translate("MainAppWindow", u"EXR Sequence Folder", None))
        self.movFolderButton.setText(QCoreApplication.translate("MainAppWindow", u"MOV Folder", None))
        self.conversionButton.setText(QCoreApplication.translate("MainAppWindow", u"Convert", None))
    # retranslateUi

