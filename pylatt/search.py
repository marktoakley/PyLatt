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
        self.step=0
        self.best_structure = self.factory.random_avoid()
        self.best_energy = self.model.calculate_energy(self.best_structure)
        
    def run(self, steps):
        '''Perform a simple random search.
        
        Parameters
        ----------
        steps: number of structures so generate
        
        Returns
        -------
        the best structure found
        '''
        for self.step in range (self.step +1, self.step + steps + 1):
            structure=self.factory.random_avoid()
            energy = self.model.calculate_energy(structure)
            structure.energy = energy
            if energy < self.best_energy:
                self.best_energy=energy
                self.best_structure = structure
        return self.best_structure
    
class MonteCarlo:
    '''Metropolis Monte Carlo (without the Metropolis test at the moment).'''
    def __init__(self, lattice, model):
        self.lattice = lattice
        self.model = model
        self.last_structure = LatticeStructureFactory(self.model.natoms, self.lattice).random_avoid()
        self.model.calculate_energy(self.last_structure)
        self.best_structure = self.last_structure
        self.best_energy = self.best_structure.energy
        self.mover = Reptator()
        self.step = 0
        
    def run(self, steps):
        for self.step in range (self.step +1, self.step + steps + 1):
            structure = self.mover.move(self.last_structure)
            energy = self.model.calculate_energy(structure)
            if structure.energy < self.best_structure.energy:
                self.best_structure = structure
                self.best_energy = energy
            # Metropolis stuff goes here
            #print self.step, energy, self.best_structure.energy
            self.last_structure = structure
        return self.best_structure