'''
Fit an off-lattice structure to a lattice

@author: Mark Oakley
'''
from pylatt.lattice import FCCLattice
from pylatt.off_lattice import read_from_pdb, to_lattice
from pylatt.plotter import plot_3d

structure = read_from_pdb("4mbn")

#plot_3d(structure)

latt_struc = to_lattice(structure, FCCLattice())

print latt_struc.coords

plot_3d(structure).show()
plot_3d(latt_struc).show()
