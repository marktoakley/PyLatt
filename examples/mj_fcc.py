'''
A search on a face-centered cubic lattice using the MJ potential.

@author: Mark Oakley
'''
from lattice.model import MJ
from lattice.moves import *
from lattice.plotter import plot_3d
from lattice.search import RandomSearch

sequence = "LMVGGVVIA"
model = MJ(sequence)
lattice = FCCLattice()

search = RandomSearch(lattice, model)

structure = search.run(1000)

plot_3d(structure, model)
