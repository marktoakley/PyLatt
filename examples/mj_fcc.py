'''
A Monte Carlo search on a face-centered cubic lattice using the MJ potential.

@author: Mark Oakley
'''
from pylatt.model import MJ
from pylatt.lattice import *
from pylatt.plotter import plot_3d
from pylatt.search import MonteCarlo

sequence = "LMVGGVVIA"
model = MJ(sequence)
lattice = FCCLattice()

search = MonteCarlo(lattice, model)

structure = search.run(1000)

plot_3d(structure, model)
