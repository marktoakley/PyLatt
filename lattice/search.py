'''
@author: Mark Oakley
'''
from lattice.lattice_structure import LatticeStructureFactory

class RandomSearch:
    '''Repeatedly generates random structures.'''
    def __init__(self, lattice, potential):
        self.lattice = lattice
        self.potential = potential
        self.factory = LatticeStructureFactory(len(self.potential.isequence), self.lattice)
        
    def run(self, steps):
        '''Perform a simple random search.
        
        Parameters
        ----------
        steps: number of structures so generate
        
        Returns
        -------
        the best structure found
        '''
        best_energy = 0
        for i in range (1, steps):
            structure=self.factory.random_avoid()
            energy = self.potential.calculate_energy(structure)
            structure.energy = energy
            if energy < best_energy:
                best_energy=energy
                best_structure = structure
            #print i, energy, best_energy
        return best_structure