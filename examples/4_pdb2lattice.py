'''
Fit an off-lattice structure to a lattice

@author: Mark Oakley
'''
from pylatt.lattice import FCCLattice
from pylatt.off_lattice import read_from_pdb, to_lattice
from pylatt.plotter import display_fit

structure = read_from_pdb("4mbn")

latt_struc = to_lattice(structure, FCCLattice())

display_fit(latt_struc)