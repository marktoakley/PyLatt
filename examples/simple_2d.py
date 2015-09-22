'''
A simple search on a 2D lattice using the HP potential.

@author: Mark Oakley
'''
from lattice.model import HP
from lattice.moves import SquareLattice
from lattice.plotter import plot_2d
from lattice.search import RandomSearch

sequence = "PHPPHPHHHPHHPHHHHH"
model = HP(sequence)
lattice = SquareLattice()

search = RandomSearch(lattice, model)

structure = search.run(100)

plot_2d(structure, model)
