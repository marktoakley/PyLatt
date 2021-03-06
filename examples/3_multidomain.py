'''
A Monte Carlo search on a multidomain protein.

@author: Mark Oakley
'''
from pylatt.model import MJ
from pylatt.lattice import FCCLattice
from pylatt.plotter import plot_3d
from pylatt.search import MonteCarlo
import matplotlib.pyplot as plt

'''To search a multidomain protein, set up a termini list. This
should contain the indices of the ends of each peptide chain. The
example here sets up two 9-residue peptides.'''
model = MJ("LMVGGVVIALMVGGVVIA")
chain_list = [9, 9]
lattice = FCCLattice()
search = MonteCarlo(lattice, model, chain_list)
structure = search.run(100)
plot_3d(structure)
plt.show()