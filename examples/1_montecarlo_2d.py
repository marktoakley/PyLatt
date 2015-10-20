'''
This example demonstrates the setting up and running of a Monte Carlo
search on a two-dimensional square lattice.

@author: Mark Oakley
'''
from pylatt.model import HP
from pylatt.lattice import SquareLattice
from pylatt.plotter import plot_2d
from pylatt.search import MonteCarlo

''' First choose a lattice. Here, we will use the two-dimensional
square lattice.'''
lattice = SquareLattice()
'''Select the protein sequrnce to search. Using the classic hydrophobic
polar model, we need to define a sequence of H and P residues.'''
model = HP("PHPPHPHHHPHHPHHHHH")
'''Now set up and run a Monte Carlo search. The temperature is an
optional parameter and defaults to 1.0 if not defined.'''
search = MonteCarlo(lattice, model, temperature = 2.0)
'''Run the search for 100 steps.The search returns the lowest energy
structure found. The energy of this structure is in structure.energy.'''
structure = search.run(100)
print "Lowest energy found: ", structure.energy
'''To visualise this structure, use plot_2d.'''
plot_2d(structure, model)
