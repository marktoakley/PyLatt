"""
start a gui for a binary lennard jones cluster.

All that is really needed to start a gui is define a system and call run_gui

    system = BLJCluster(natoms, ntypeA)
    run_gui(system)

"""
import sys

from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

from pylatt.gui._search_dialog import Ui_DialogLJSetup as UI
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
        self.close()


    def on_buttonBox_rejected(self):
        self.close()


if __name__ == "__main__":
    # create a pop up window to get the number of atoms
    app = QtGui.QApplication(sys.argv)
    dialog = SearchDialog()
    dialog.exec_()
    if dialog.steps is None:
        sys.exit()
    # create the system and start the gui
    # (note: since the application is already started we need to pass it to run_gui)
    if ("Miyazawa" in dialog.model):
        model = MJ(dialog.sequence)
    else:
        model = HP(dialog.sequence)
    if ("Square" in dialog.lattice):
        lattice = SquareLattice()
    elif ("Diamond" in dialog.lattice):
        lattice = DiamondLattice()
    elif ("Cubic" in dialog.lattice):
        lattice = CubicLattice()
    elif ("BCC" in dialog.lattice):
        lattice = BCCLattice()
    elif ("FCC" in dialog.lattice):
        lattice = FCCLattice()
    print("Using "+dialog.model+" model on "+dialog.lattice+" lattice.")
    print("Searching for "+str(dialog.steps)+" steps.")  
    search = MonteCarlo(lattice, model, temperature = 2.0)
    structure = search.run(100)
    print("Lowest energy found: "+str(structure.energy))
    if (isinstance(lattice, SquareLattice)):
        plot_2d(structure, model)
    else:
        plot_3d(structure, model)        

