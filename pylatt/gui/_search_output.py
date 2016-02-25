# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_search_output.ui'
#
# Created: Thu Feb 25 15:26:06 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogSearchDisplay(object):
    def setupUi(self, DialogSearchDisplay):
        DialogSearchDisplay.setObjectName(_fromUtf8("DialogSearchDisplay"))
        DialogSearchDisplay.resize(608, 498)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSearchDisplay.sizePolicy().hasHeightForWidth())
        DialogSearchDisplay.setSizePolicy(sizePolicy)
        DialogSearchDisplay.setModal(True)
        self.button_run = QtGui.QPushButton(DialogSearchDisplay)
        self.button_run.setGeometry(QtCore.QRect(10, 50, 98, 27))
        self.button_run.setObjectName(_fromUtf8("button_run"))
        self.log = QtGui.QTextEdit(DialogSearchDisplay)
        self.log.setGeometry(QtCore.QRect(120, 10, 481, 121))
        self.log.setObjectName(_fromUtf8("log"))
        self.button_set_up = QtGui.QPushButton(DialogSearchDisplay)
        self.button_set_up.setGeometry(QtCore.QRect(10, 10, 98, 27))
        self.button_set_up.setObjectName(_fromUtf8("button_set_up"))
        self.tabWidget = QtGui.QTabWidget(DialogSearchDisplay)
        self.tabWidget.setGeometry(QtCore.QRect(120, 140, 481, 351))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.widget = matplotlibWidget(self.tab1)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 301))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.widget_2 = matplotlibWidget(self.tab2)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 451, 301))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))

        self.retranslateUi(DialogSearchDisplay)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogSearchDisplay)

    def retranslateUi(self, DialogSearchDisplay):
        DialogSearchDisplay.setWindowTitle(_translate("DialogSearchDisplay", "Lattice Monte Carlo", None))
        self.button_run.setText(_translate("DialogSearchDisplay", "Run", None))
        self.button_set_up.setText(_translate("DialogSearchDisplay", "Set Up", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("DialogSearchDisplay", "Structure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("DialogSearchDisplay", "Map", None))

from matplotlibWidget import matplotlibWidget
