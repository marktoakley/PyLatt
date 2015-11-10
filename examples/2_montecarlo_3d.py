'''
This example demonstrates MonteCarlo searches on a 3D lattice.

@author: Mark Oakley
'''
from pylatt.model import MJ
from pylatt.lattice import CubicLattice
from pylatt.plotter import plot_3d
from pylatt.search import MonteCarlo

'''Choose a 3D lattice (Diamond, Cubic, BCC or FCC)'''
lattice = CubicLattice()
'''Here we will use the Miyazawa-Jernigan potential. Define the
sequence using the standars single-letter amino acid codes.'''
model = MJ("LMVGGVVIA")
'''Set up and run the search as in the previous example.'''
search = MonteCarlo(lattice, model)
structure = search.run(1000)
print "Lowest energy found: ", structure.energy
'''Visualise the best structure ising plot_3d.'''
plot_3d(structure, model).show()

