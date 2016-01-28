# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_search_output.ui'
#
# Created: Thu Jan 28 18:35:52 2016
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
        DialogSearchDisplay.resize(655, 540)
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
        self.log.setGeometry(QtCore.QRect(120, 10, 521, 121))
        self.log.setObjectName(_fromUtf8("log"))
        self.widget = matplotlibWidget(DialogSearchDisplay)
        self.widget.setGeometry(QtCore.QRect(120, 140, 521, 391))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.button_set_up = QtGui.QPushButton(DialogSearchDisplay)
        self.button_set_up.setGeometry(QtCore.QRect(10, 10, 98, 27))
        self.button_set_up.setObjectName(_fromUtf8("button_set_up"))

        self.retranslateUi(DialogSearchDisplay)
        QtCore.QMetaObject.connectSlotsByName(DialogSearchDisplay)

    def retranslateUi(self, DialogSearchDisplay):
        DialogSearchDisplay.setWindowTitle(_translate("DialogSearchDisplay", "Lattice Monte Carlo", None))
        self.button_run.setText(_translate("DialogSearchDisplay", "Run", None))
        self.button_set_up.setText(_translate("DialogSearchDisplay", "Set Up", None))

from matplotlibWidget import matplotlibWidget
