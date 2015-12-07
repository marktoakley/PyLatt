import sys
from _search_dialog import *

from pylatt.model import *
from pylatt.lattice import *
from pylatt.search import *
from pylatt.plotter import *

class GUIForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DialogSearchSetup()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.run)

    def PlotFunc(self):
        randomNumbers = random.sample(range(0, 10), 10)
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.plot(randomNumbers)
        self.ui.widget.canvas.draw()
        

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
        self.ui.log.append("Using "+self.model+" model on "+self.lattice+" lattice.")
        self.ui.log.append("Searching for "+str(self.steps)+" steps.")  
        search = MonteCarlo(lattice, model, temperature = 2.0)
        structure = search.run(self.steps)
        self.ui.log.append("Lowest energy found: "+str(structure.energy))
        if (isinstance(lattice, SquareLattice)):
            plot_2d(structure, self.ui.widget.canvas.fig, model)
        else:
            plot_3d(structure, self.ui.widget.canvas.fig, model)
        self.ui.widget.canvas.draw()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    sys.exit(app.exec_())