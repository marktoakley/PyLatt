"""
GUI for optimisation of lattice model proteins.
"""
import sys

from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

from pylatt.gui._search_dialog import Ui_DialogSearchSetup as UI
from pylatt.model import *
from pylatt.lattice import *
from pylatt.search import *
from pylatt.plotter import *


class SearchDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = UI()
        self.ui.setupUi(self)
        self.setWindowTitle("Lattice Search")
    
    def get_input(self):
        self.sequence = self.ui.lineEdit_sequence.text()
        self.steps = int(self.ui.lineEdit_steps.text())
        self.model = str(self.ui.comboBox_model.currentText())
        self.lattice = str(self.ui.comboBox_lattice.currentText())

    def on_buttonBox_accepted(self):
        self.get_input()
        if ("Miyazawa" in self.model):
            model = MJ(self.sequence)
        else:
            model = HP(self.sequence)
        if ("Square" in self.lattice):
            lattice = SquareLattice()
        elif ("Diamond" in self.lattice):
            lattice = DiamondLattice()
        elif ("Cubic" in self.lattice):
            lattice = CubicLattice()
        elif ("BCC" in self.lattice):
            lattice = BCCLattice()
        elif ("FCC" in self.lattice):
            lattice = FCCLattice()
        print("Using "+self.model+" model on "+self.lattice+" lattice.")
        print("Searching for "+str(self.steps)+" steps.")  
        search = MonteCarlo(lattice, model, temperature = 2.0)
        structure = search.run(self.steps)
        print("Lowest energy found: "+str(structure.energy))
        if (isinstance(lattice, SquareLattice)):
            plot = plot_2d(structure, model)
        else:
            plot = plot_3d(structure, model)
        plot.show()
        self.close()

    def on_buttonBox_rejected(self):
        self.close()

if __name__ == "__main__":
    # create a pop up window to get the number of atoms
    app = QtGui.QApplication(sys.argv)
    dialog = SearchDialog()
    dialog.exec_()
