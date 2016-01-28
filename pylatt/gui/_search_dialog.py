# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_search_dialog.ui'
#
# Created: Thu Jan 28 17:07:53 2016
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

class Ui_DialogSearchSetup(object):
    def setupUi(self, DialogSearchSetup):
        DialogSearchSetup.setObjectName(_fromUtf8("DialogSearchSetup"))
        DialogSearchSetup.resize(325, 324)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSearchSetup.sizePolicy().hasHeightForWidth())
        DialogSearchSetup.setSizePolicy(sizePolicy)
        DialogSearchSetup.setModal(True)
        self.pushButton = QtGui.QPushButton(DialogSearchSetup)
        self.pushButton.setGeometry(QtCore.QRect(110, 280, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayoutWidget = QtGui.QWidget(DialogSearchSetup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 301, 241))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_sequence = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_sequence.setInputMask(_fromUtf8(""))
        self.lineEdit_sequence.setObjectName(_fromUtf8("lineEdit_sequence"))
        self.gridLayout.addWidget(self.lineEdit_sequence, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.comboBox_model = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_model.setObjectName(_fromUtf8("comboBox_model"))
        self.comboBox_model.addItem(_fromUtf8(""))
        self.comboBox_model.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_model, 2, 1, 1, 1)
        self.comboBox_lattice = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_lattice.setObjectName(_fromUtf8("comboBox_lattice"))
        self.comboBox_lattice.addItem(_fromUtf8(""))
        self.comboBox_lattice.addItem(_fromUtf8(""))
        self.comboBox_lattice.addItem(_fromUtf8(""))
        self.comboBox_lattice.addItem(_fromUtf8(""))
        self.comboBox_lattice.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_lattice, 3, 1, 1, 1)
        self.lineEdit_steps = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_steps.setObjectName(_fromUtf8("lineEdit_steps"))
        self.gridLayout.addWidget(self.lineEdit_steps, 4, 1, 1, 1)

        self.retranslateUi(DialogSearchSetup)
        QtCore.QMetaObject.connectSlotsByName(DialogSearchSetup)

    def retranslateUi(self, DialogSearchSetup):
        DialogSearchSetup.setWindowTitle(_translate("DialogSearchSetup", "Lattice Monte Carlo", None))
        self.pushButton.setText(_translate("DialogSearchSetup", "Run", None))
        self.label_2.setText(_translate("DialogSearchSetup", "Model", None))
        self.lineEdit_sequence.setText(_translate("DialogSearchSetup", "PHPPHPHHHPHHPHHHHH", None))
        self.label.setText(_translate("DialogSearchSetup", "Sequence", None))
        self.label_3.setText(_translate("DialogSearchSetup", "Lattice", None))
        self.label_4.setText(_translate("DialogSearchSetup", "Steps", None))
        self.comboBox_model.setItemText(0, _translate("DialogSearchSetup", "Hydrophobic-Polar", None))
        self.comboBox_model.setItemText(1, _translate("DialogSearchSetup", "Miyazawa-Jernigan", None))
        self.comboBox_lattice.setItemText(0, _translate("DialogSearchSetup", "Square", None))
        self.comboBox_lattice.setItemText(1, _translate("DialogSearchSetup", "Diamond", None))
        self.comboBox_lattice.setItemText(2, _translate("DialogSearchSetup", "Cubic", None))
        self.comboBox_lattice.setItemText(3, _translate("DialogSearchSetup", "BCC", None))
        self.comboBox_lattice.setItemText(4, _translate("DialogSearchSetup", "FCC", None))
        self.lineEdit_steps.setText(_translate("DialogSearchSetup", "100", None))

