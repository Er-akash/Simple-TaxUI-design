
from PyQt4 import QtCore, QtGui, uic
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import tax_calc

class simplecalc(QtGui.QMainWindow, tax_calc.Ui_dialog):
        def __init__(self):
                super(self.__class__,self).__init__()
                self.setupUi(self)
                self.calc_tax_button.clicked.connect(self.CalculateTax)
        def CalculateTax(self):
                price = int(self.price_box.toPlainText())
                print("price",price)
                tax = int(self.tax_rate.value())
                print("tax",tax)
                ##x=tax/100
                ##print(x)
                total_price = float(price+((tax*0.01)*price))
                print("total price is ",total_price)
                total_price_string = "The total price Along with tax is: " + str(total_price)
                self.results_window.setText(total_price_string)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = simplecalc()
	window.show()
	sys.exit(app.exec_())
