# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 235, 254);\n"
"background-color: rgb(250, 240, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 3, 1, 1)
        self.DisplayWInvFile = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DisplayWInvFile.setFont(font)
        self.DisplayWInvFile.setObjectName("DisplayWInvFile")
        self.gridLayout.addWidget(self.DisplayWInvFile, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 3, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.tableWidgetInvFile = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetInvFile.setRowCount(0)
        self.tableWidgetInvFile.setColumnCount(20)
        self.tableWidgetInvFile.setObjectName("tableWidgetInvFile")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetInvFile.setHorizontalHeaderItem(0, item)
        self.tableWidgetInvFile.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetInvFile, 1, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 3, 1)
        self.line_45 = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_45.setFont(font)
        self.line_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setObjectName("line_45")
        self.gridLayout.addWidget(self.line_45, 0, 1, 1, 1)
        self.DisplayInvFile = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DisplayInvFile.setFont(font)
        self.DisplayInvFile.setObjectName("DisplayInvFile")
        self.gridLayout.addWidget(self.DisplayInvFile, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 1, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_18 = QtWidgets.QFrame(self.tab_5)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.horizontalLayout_2.addWidget(self.line_18)
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.line_17 = QtWidgets.QFrame(self.tab_5)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.horizontalLayout_2.addWidget(self.line_17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.accesdocs = QtWidgets.QLineEdit(self.tab_5)
        self.accesdocs.setObjectName("accesdocs")
        self.horizontalLayout_4.addWidget(self.accesdocs)
        self.accesDocsButton = QtWidgets.QPushButton(self.tab_5)
        self.accesDocsButton.setObjectName("accesDocsButton")
        self.horizontalLayout_4.addWidget(self.accesDocsButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 4, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_15 = QtWidgets.QFrame(self.tab_5)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayout_5.addWidget(self.line_15)
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.line_14 = QtWidgets.QFrame(self.tab_5)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout_5.addWidget(self.line_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tableWidgetDocs = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidgetDocs.setColumnCount(3)
        self.tableWidgetDocs.setObjectName("tableWidgetDocs")
        self.tableWidgetDocs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetDocs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetDocs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetDocs.setHorizontalHeaderItem(2, item)
        self.tableWidgetDocs.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidgetDocs)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_13 = QtWidgets.QFrame(self.tab_5)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout.addWidget(self.line_13)
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.line_16 = QtWidgets.QFrame(self.tab_5)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.horizontalLayout.addWidget(self.line_16)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.accesTerm = QtWidgets.QLineEdit(self.tab_5)
        self.accesTerm.setObjectName("accesTerm")
        self.horizontalLayout_3.addWidget(self.accesTerm)
        self.accesTermButton = QtWidgets.QPushButton(self.tab_5)
        self.accesTermButton.setObjectName("accesTermButton")
        self.horizontalLayout_3.addWidget(self.accesTermButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem4, 1, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_20 = QtWidgets.QFrame(self.tab_5)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.horizontalLayout_6.addWidget(self.line_20)
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.line_19 = QtWidgets.QFrame(self.tab_5)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.horizontalLayout_6.addWidget(self.line_19)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.tableWidgetTermes = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidgetTermes.setColumnCount(3)
        self.tableWidgetTermes.setObjectName("tableWidgetTermes")
        self.tableWidgetTermes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetTermes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetTermes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetTermes.setHorizontalHeaderItem(2, item)
        self.tableWidgetTermes.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tableWidgetTermes)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 2, 4, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 1, 3, 2, 1)
        self.line_21 = QtWidgets.QFrame(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_21.sizePolicy().hasHeightForWidth())
        self.line_21.setSizePolicy(sizePolicy)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_4.addWidget(self.line_21, 0, 2, 4, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 0, 1, 2, 1)
        spacerItem9 = QtWidgets.QSpacerItem(212, 318, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 2, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(195, 100, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem10, 0, 0, 2, 1)
        spacerItem11 = QtWidgets.QSpacerItem(212, 318, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 2, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem12, 1, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(195, 100, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 0, 4, 2, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_7.addWidget(self.line_5)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_7.addWidget(self.line_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.requetBool = QtWidgets.QLineEdit(self.tab_2)
        self.requetBool.setMinimumSize(QtCore.QSize(100, 0))
        self.requetBool.setMaximumSize(QtCore.QSize(600, 16777215))
        self.requetBool.setObjectName("requetBool")
        self.horizontalLayout_8.addWidget(self.requetBool)
        self.ModeleBoolButton = QtWidgets.QPushButton(self.tab_2)
        self.ModeleBoolButton.setMinimumSize(QtCore.QSize(30, 0))
        self.ModeleBoolButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ModeleBoolButton.setObjectName("ModeleBoolButton")
        self.horizontalLayout_8.addWidget(self.ModeleBoolButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem14, 0, 3, 2, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_9.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_9.addWidget(self.line_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.tableWidgetDocsBool = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetDocsBool.setObjectName("tableWidgetDocsBool")
        self.tableWidgetDocsBool.setColumnCount(1)
        self.tableWidgetDocsBool.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 1))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetDocsBool.setHorizontalHeaderItem(0, item)
        self.tableWidgetDocsBool.horizontalHeader().setMinimumSectionSize(28)
        self.tableWidgetDocsBool.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetDocsBool.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDocsBool.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDocsBool.verticalHeader().setDefaultSectionSize(34)
        self.tableWidgetDocsBool.verticalHeader().setMinimumSectionSize(34)
        self.verticalLayout_6.addWidget(self.tableWidgetDocsBool)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 2, 1, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem15 = QtWidgets.QSpacerItem(80, 448, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem15, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem16 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.line_12 = QtWidgets.QFrame(self.tab_3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_10.addWidget(self.line_12)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.line_11 = QtWidgets.QFrame(self.tab_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_10.addWidget(self.line_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        spacerItem17 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem18 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem18)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.line_7 = QtWidgets.QFrame(self.tab_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_11.addWidget(self.line_7)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.line_10 = QtWidgets.QFrame(self.tab_3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_11.addWidget(self.line_10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.requetVec = QtWidgets.QLineEdit(self.tab_3)
        self.requetVec.setObjectName("requetVec")
        self.horizontalLayout_12.addWidget(self.requetVec)
        self.ModeleVectButton = QtWidgets.QPushButton(self.tab_3)
        self.ModeleVectButton.setObjectName("ModeleVectButton")
        self.horizontalLayout_12.addWidget(self.ModeleVectButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_9)
        spacerItem19 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.line_9 = QtWidgets.QFrame(self.tab_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_13.addWidget(self.line_9)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.line_8 = QtWidgets.QFrame(self.tab_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_13.addWidget(self.line_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.tableWidgetDocsVect = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidgetDocsVect.setObjectName("tableWidgetDocsVect")
        self.tableWidgetDocsVect.setColumnCount(2)
        self.tableWidgetDocsVect.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetDocsVect.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetDocsVect.setHorizontalHeaderItem(1, item)
        self.tableWidgetDocsVect.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDocsVect.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidgetDocsVect.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetDocsVect.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetDocsVect.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDocsVect.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDocsVect.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetDocsVect.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_8.addWidget(self.tableWidgetDocsVect)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.gridLayout_7.addLayout(self.verticalLayout_10, 0, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(80, 448, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem20, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modèles RI"))
        self.DisplayWInvFile.setText(_translate("MainWindow", "Fichier Inverse (Poids)"))
        self.label.setText(_translate("MainWindow", "Fichier Inverse"))
        item = self.tableWidgetInvFile.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Terme"))
        self.DisplayInvFile.setText(_translate("MainWindow", "Fichier Inverse (Fréquences)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Affichage"))
        self.label_9.setText(_translate("MainWindow", "Document"))
        self.accesDocsButton.setText(_translate("MainWindow", "Ok"))
        self.label_7.setText(_translate("MainWindow", "Documents "))
        item = self.tableWidgetDocs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidgetDocs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Frequence"))
        item = self.tableWidgetDocs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Poids"))
        self.label_8.setText(_translate("MainWindow", "Terme"))
        self.accesTermButton.setText(_translate("MainWindow", "Ok"))
        self.label_10.setText(_translate("MainWindow", "Termes"))
        item = self.tableWidgetTermes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Terme"))
        item = self.tableWidgetTermes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fréquence"))
        item = self.tableWidgetTermes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Poids"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Accès de bases"))
        self.label_3.setText(_translate("MainWindow", "Requete Booleenne"))
        self.ModeleBoolButton.setText(_translate("MainWindow", "Ok"))
        self.label_2.setText(_translate("MainWindow", "Documents pertinents"))
        item = self.tableWidgetDocsBool.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Documents"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Modèles Booleen"))
        self.label_6.setText(_translate("MainWindow", "Formule"))
        self.comboBox.setItemText(0, _translate("MainWindow", "innerProduct"))
        self.comboBox.setItemText(1, _translate("MainWindow", "coefDeDice"))
        self.comboBox.setItemText(2, _translate("MainWindow", "cos"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Jaccard"))
        self.label_5.setText(_translate("MainWindow", "Requete Vectorielle"))
        self.ModeleVectButton.setText(_translate("MainWindow", "Ok"))
        self.label_4.setText(_translate("MainWindow", "Documents pertinents"))
        item = self.tableWidgetDocsVect.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidgetDocsVect.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Similarité"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Modèle Vectoriel"))

