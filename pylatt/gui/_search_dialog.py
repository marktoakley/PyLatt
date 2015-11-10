# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_search_dialog.ui'
#
# Created: Tue Nov 10 17:10:35 2015
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

class Ui_DialogLJSetup(object):
    def setupUi(self, DialogLJSetup):
        DialogLJSetup.setObjectName(_fromUtf8("DialogLJSetup"))
        DialogLJSetup.resize(347, 348)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogLJSetup.sizePolicy().hasHeightForWidth())
        DialogLJSetup.setSizePolicy(sizePolicy)
        DialogLJSetup.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(DialogLJSetup)
        self.buttonBox.setGeometry(QtCore.QRect(30, 280, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(DialogLJSetup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 301, 241))
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

        self.retranslateUi(DialogLJSetup)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogLJSetup.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogLJSetup.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogLJSetup)

    def retranslateUi(self, DialogLJSetup):
        DialogLJSetup.setWindowTitle(_translate("DialogLJSetup", "Create binary Lennard-Jones system", None))
        self.label_2.setText(_translate("DialogLJSetup", "Model", None))
        self.lineEdit_sequence.setText(_translate("DialogLJSetup", "PHPPHPHHHPHHPHHHHH", None))
        self.label.setText(_translate("DialogLJSetup", "Sequence", None))
        self.label_3.setText(_translate("DialogLJSetup", "Lattice", None))
        self.label_4.setText(_translate("DialogLJSetup", "Steps", None))
        self.comboBox_model.setItemText(0, _translate("DialogLJSetup", "Hydrophobic-Polar", None))
        self.comboBox_model.setItemText(1, _translate("DialogLJSetup", "Miyazawa-Jernigan", None))
        self.comboBox_lattice.setItemText(0, _translate("DialogLJSetup", "Square", None))
        self.comboBox_lattice.setItemText(1, _translate("DialogLJSetup", "Diamond", None))
        self.comboBox_lattice.setItemText(2, _translate("DialogLJSetup", "Cubic", None))
        self.comboBox_lattice.setItemText(3, _translate("DialogLJSetup", "BCC", None))
        self.comboBox_lattice.setItemText(4, _translate("DialogLJSetup", "FCC", None))
        self.lineEdit_steps.setText(_translate("DialogLJSetup", "100", None))

