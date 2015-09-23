'''
A simple search on a cubic 3D lattice using the HP potential.

@author: Mark Oakley
'''
from pylatt.model import HP
from pylatt.lattice import *
from pylatt.plotter import plot_3d
from pylatt.search import RandomSearch

sequence = "PHPPHPHHHPHHPHHHHH"
model = HP(sequence)
lattice = CubicLattice()

search = RandomSearch(lattice, model)

structure = search.run(100)

plot_3d(structure, model)
