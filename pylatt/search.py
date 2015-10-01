'''
@author: Mark Oakley
'''
from math import exp
import random

from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.move import Reptate

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
    '''Metropolis Monte Carlo.'''
    def __init__(self, lattice, model):
        self.lattice = lattice
        self.model = model
        self.last_structure = LatticeStructureFactory(self.model.natoms, self.lattice).random_avoid()
        self.model.calculate_energy(self.last_structure)
        self.best_structure = self.last_structure
        self.best_energy = self.best_structure.energy
        self.mover = Reptate()
        self.step = 0
        
    def run(self, steps):
        for self.step in range (self.step +1, self.step + steps + 1):
            structure = self.mover.move(self.last_structure)
            energy = self.model.calculate_energy(structure)
            #print self.step, structure.energy, self.last_structure.energy, self.best_structure.energy
            if structure.energy < self.best_structure.energy:
                self.best_structure = structure
                self.best_energy = energy
            if random.random() < metropolis_probability(self.last_structure.energy, structure.energy):
                self.last_structure = structure
        return self.best_structure
    
def metropolis_probability(e1, e2, r=1.0, t=1.0):
    return min(exp(-((e2 - e1) / (r * t))), 1.)