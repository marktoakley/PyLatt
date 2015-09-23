'''
A simple search on a 2D lattice using the HP potential.

@author: Mark Oakley
'''
from pylatt.model import HP
from pylatt.lattice import SquareLattice
from pylatt.plotter import plot_2d
from pylatt.search import RandomSearch

sequence = "PHPPHPHHHPHHPHHHHH"
model = HP(sequence)
lattice = SquareLattice()

search = RandomSearch(lattice, model)

structure = search.run(100)

plot_2d(structure, model)
