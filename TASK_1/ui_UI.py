# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ashou\OneDrive\Documents\ImagePro\TASK_1\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1476, 716)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ImageSize = QtWidgets.QLabel(self.centralwidget)
        self.ImageSize.setObjectName("ImageSize")
        self.gridLayout_2.addWidget(self.ImageSize, 6, 1, 1, 1)
        self.ImageColor = QtWidgets.QLabel(self.centralwidget)
        self.ImageColor.setObjectName("ImageColor")
        self.gridLayout_2.addWidget(self.ImageColor, 5, 1, 1, 1)
        self.BodyPart = QtWidgets.QLabel(self.centralwidget)
        self.BodyPart.setMinimumSize(QtCore.QSize(140, 0))
        self.BodyPart.setObjectName("BodyPart")
        self.gridLayout_2.addWidget(self.BodyPart, 8, 1, 1, 1)
        self.Modality = QtWidgets.QLabel(self.centralwidget)
        self.Modality.setObjectName("Modality")
        self.gridLayout_2.addWidget(self.Modality, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        self.BitDepth = QtWidgets.QLabel(self.centralwidget)
        self.BitDepth.setObjectName("BitDepth")
        self.gridLayout_2.addWidget(self.BitDepth, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 2, 1, 1)
        self.PatientAge = QtWidgets.QLabel(self.centralwidget)
        self.PatientAge.setObjectName("PatientAge")
        self.gridLayout_2.addWidget(self.PatientAge, 3, 1, 1, 1)
        self.PatientName = QtWidgets.QLabel(self.centralwidget)
        self.PatientName.setObjectName("PatientName")
        self.gridLayout_2.addWidget(self.PatientName, 2, 1, 1, 1)
        self.ImageDim = QtWidgets.QLabel(self.centralwidget)
        self.ImageDim.setObjectName("ImageDim")
        self.gridLayout_2.addWidget(self.ImageDim, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(500, 0))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(500, 0))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(500, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(500, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(500, 0))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(500, 0))
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(500, 0))
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(500, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(20, 80, 700, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(700, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 530, 711, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LayoutShow = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutShow.setContentsMargins(0, 0, 0, 0)
        self.LayoutShow.setObjectName("LayoutShow")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 302, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.ScaleEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ScaleEdit.setFont(font)
        self.ScaleEdit.setObjectName("ScaleEdit")
        self.horizontalLayout_3.addWidget(self.ScaleEdit)
        self.ResizeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ResizeButton.setObjectName("ResizeButton")
        self.horizontalLayout_3.addWidget(self.ResizeButton)
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(0, 590, 722, 2))
        self.widget.setObjectName("widget")
        self.LayoutScale = QtWidgets.QVBoxLayout(self.widget)
        self.LayoutScale.setContentsMargins(0, 0, 0, 0)
        self.LayoutScale.setObjectName("LayoutScale")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1476, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBrowse = QtWidgets.QAction(MainWindow)
        self.actionBrowse.setObjectName("actionBrowse")
        self.menufile.addAction(self.actionBrowse)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImageSize.setText(_translate("MainWindow", "None"))
        self.ImageColor.setText(_translate("MainWindow", "None"))
        self.BodyPart.setText(_translate("MainWindow", "None"))
        self.Modality.setText(_translate("MainWindow", "None"))
        self.label_3.setText(_translate("MainWindow", "Information"))
        self.BitDepth.setText(_translate("MainWindow", "None"))
        self.PatientAge.setText(_translate("MainWindow", "None"))
        self.PatientName.setText(_translate("MainWindow", "None"))
        self.ImageDim.setText(_translate("MainWindow", "None"))
        self.label_5.setText(_translate("MainWindow", "Image Color: "))
        self.label_8.setText(_translate("MainWindow", "Patient\'s Name: "))
        self.label_4.setText(_translate("MainWindow", "Body Part Examined: "))
        self.label_2.setText(_translate("MainWindow", "Modality Used: "))
        self.label_7.setText(_translate("MainWindow", "Patient\'s Age: "))
        self.label_9.setText(_translate("MainWindow", "Bit Depth: "))
        self.label_10.setText(_translate("MainWindow", "Image Size: "))
        self.label_6.setText(_translate("MainWindow", "Image Dimensions (W/H): "))
        self.label.setText(_translate("MainWindow", "Image View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.label_11.setText(_translate("MainWindow", "Scale factor"))
        self.ScaleEdit.setText(_translate("MainWindow", "10"))
        self.ResizeButton.setText(_translate("MainWindow", "Resize"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.actionBrowse.setText(_translate("MainWindow", "Browse"))
