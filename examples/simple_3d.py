'''
A simple search on a 2D lattice using the HP potential.

@author: Mark Oakley
'''
from lattice.model import HP
from lattice.moves import *
from lattice.test.plotter import plot_3d
from lattice.search import RandomSearch

sequence = "PHPPHPHHHPHHPHHHHH"
model = HP(sequence)
lattice = CubicLattice()

search = RandomSearch(lattice, model)

structure = search.run(100)

plot_3d(structure, model)
