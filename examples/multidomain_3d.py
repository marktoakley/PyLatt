'''
A Monte Carlo search on a 2D lattice using the HP potential.

@author: Mark Oakley
'''
from pylatt.model import HP
from pylatt.lattice import CubicLattice
from pylatt.plotter import plot_3d
from pylatt.search import MonteCarlo

sequence = "HHHHPPHHHHHHHHPPHHHH"
model = HP(sequence)
termini = [0,9,10,19]
lattice = CubicLattice()

search = MonteCarlo(lattice, model, termini = termini)


structure = search.run(100)

plot_3d(structure, model)
