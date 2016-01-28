import sys
from _search_dialog import *

from pylatt.model import *
from pylatt.lattice import *
from pylatt.search import *
from pylatt.plotter import *
from pylatt.gui._search_output import Ui_DialogSearchDisplay

class DisplayForm(QtGui.QDialog):

    def __init__(self, parent=None, search=None, app=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DialogSearchDisplay()
        self.ui.setupUi(self)
        self.window2=None
        QtCore.QObject.connect(self.ui.button_set_up, QtCore.SIGNAL('clicked()'), self.set_up)
        QtCore.QObject.connect(self.ui.button_run, QtCore.SIGNAL('clicked()'), self.run)
        if (search != None):
            self.search = search
            self.search.run
    
    def set_up(self):
        if self.window2 is None:
            self.window2 = SetUpForm(parent = self)
        self.window2.show()
          
    def run(self):
        structure = self.search.run(self.steps)
        self.ui.log.append("Lowest energy found: "+str(structure.energy))
        if (isinstance(structure.lattice, SquareLattice)):
            plot_2d(structure, self.ui.widget.canvas.fig)
        else:
            plot_3d(structure, self.ui.widget.canvas.fig)
        self.ui.widget.canvas.draw()

class SetUpForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DialogSearchSetup()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.run)
        self.parent = parent

    def run(self):
        self.sequence = self.ui.lineEdit_sequence.text()
        self.steps = int(self.ui.lineEdit_steps.text())
        self.model = str(self.ui.comboBox_model.currentText())
        self.lattice = str(self.ui.comboBox_lattice.currentText())
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
        self.parent.ui.log.append("Using "+self.model+" model on "+self.lattice+" lattice.")
        self.parent.ui.log.append("Searching for "+str(self.steps)+" steps.")    
        self.parent.search = MonteCarlo(lattice, model, temperature = 2.0)
        self.parent.steps = self.steps
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = DisplayForm()
    myapp.show()
    sys.exit(app.exec_())