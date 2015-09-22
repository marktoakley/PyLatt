'''
A simple search on a 2D lattice using the HP potential.

@author: Mark Oakley
'''
from lattice.hp import HPPotential
from lattice.moves import SquareLattice
from lattice.test.plotter import plot_2d
from lattice.search import RandomSearch

sequence = "PHPPHPHHHPHHPHHHHH"
potential = HPPotential(sequence)
lattice = SquareLattice()

search = RandomSearch(lattice, potential)

structure = search.run(100)

plot_2d(structure, potential)
