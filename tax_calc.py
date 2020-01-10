# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/akash/uidesign/tax_calc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(740, 539)
        font = QtGui.QFont()
        font.setUnderline(True)
        dialog.setFont(font)
        self.calc_tax_button = QtGui.QPushButton(dialog)
        self.calc_tax_button.setGeometry(QtCore.QRect(250, 320, 89, 25))
        self.calc_tax_button.setObjectName(_fromUtf8("calc_tax_button"))
        self.price = QtGui.QLabel(dialog)
        self.price.setGeometry(QtCore.QRect(70, 170, 67, 17))
        self.price.setObjectName(_fromUtf8("price"))
        self.taxrate = QtGui.QLabel(dialog)
        self.taxrate.setGeometry(QtCore.QRect(70, 260, 67, 17))
        self.taxrate.setObjectName(_fromUtf8("taxrate"))
        self.TaxCalculator = QtGui.QLabel(dialog)
        self.TaxCalculator.setGeometry(QtCore.QRect(200, 40, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TaxCalculator.setFont(font)
        self.TaxCalculator.setScaledContents(False)
        self.TaxCalculator.setWordWrap(False)
        self.TaxCalculator.setOpenExternalLinks(False)
        self.TaxCalculator.setObjectName(_fromUtf8("TaxCalculator"))
        self.price_box = QtGui.QTextEdit(dialog)
        self.price_box.setGeometry(QtCore.QRect(240, 140, 104, 70))
        self.price_box.setObjectName(_fromUtf8("price_box"))
        self.tax_rate = QtGui.QSpinBox(dialog)
        self.tax_rate.setGeometry(QtCore.QRect(270, 250, 48, 26))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName(_fromUtf8("tax_rate"))
        self.results_window = QtGui.QTextEdit(dialog)
        self.results_window.setGeometry(QtCore.QRect(150, 380, 301, 70))
        self.results_window.setObjectName(_fromUtf8("results_window"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Dialog", None))
        self.calc_tax_button.setText(_translate("dialog", "calc tax", None))
        self.price.setText(_translate("dialog", "price", None))
        self.taxrate.setText(_translate("dialog", "taxrate", None))
        self.TaxCalculator.setText(_translate("dialog", "Tax Calculator", None))

