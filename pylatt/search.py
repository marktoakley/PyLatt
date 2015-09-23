'''
@author: Mark Oakley
'''
from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.reptate import Reptator

class RandomSearch:
    '''Repeatedly generates random structures.'''
    def __init__(self, lattice, model):
        self.lattice = lattice
        self.model = model
        self.factory = LatticeStructureFactory(self.model.natoms, self.lattice)
        
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
            energy = self.model.calculate_energy(structure)
            structure.energy = energy
            if energy < best_energy:
                best_energy=energy
                best_structure = structure
            #print i, energy, best_energy
        return best_structure
    
class MonteCarlo:
    '''Metropolis Monte Carlo (without the Metropolis test at the moment).'''
    def __init__(self, lattice, model):
        self.lattice = lattice
        self.model = model
        self.last_structure = LatticeStructureFactory(self.model.natoms, self.lattice).random_avoid()
        self.model.calculate_energy(self.last_structure)
        self.best_structure = self.last_structure
        self.mover = Reptator()
        
    def run(self, steps):
        for i in range(1, steps):
            structure = self.mover.move(self.last_structure)
            energy = self.model.calculate_energy(structure)
            if structure.energy < self.best_structure.energy:
                self.best_structure = structure
            # Metropolis stuff goes here
            #print i, energy, self.best_structure.energy
            self.last_structure = structure
        return self.best_structure