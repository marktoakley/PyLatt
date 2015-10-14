'''
@author: Mark Oakley
'''
from math import exp
import random

from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.move import Reptate

class RandomSearch:
    '''Repeatedly generates random structures.'''
    def __init__(self, lattice, model, termini = None, first_structure = None):
        self.lattice = lattice
        self.model = model
        self.factory = LatticeStructureFactory(self.model.natoms, self.lattice, termini = termini)
        self.step=0
        if first_structure is None:
            self.best_structure = self.factory.random_avoid()
        else:
            self.best_structure =first_structure
        self.best_energy = self.model.calculate_energy(self.best_structure)
        
    def run(self, steps):
        '''Perform a simple random search.
        
        Parameters
        ----------
        steps: number of structures to generate
        
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
    '''Perform a Metropolis Monte Carlo search.
    
    Parameters
    ----------
    Required
    lattice: A Lattice frombcga.lattice
    model: A Model from bcga.model
    Optional
    termini: A list containing the indices of the ends of protein chains (only needed for multicain systems)
    first_structure: A bcga.lattice_structure object to start the search (A random one will be generated if none is supplied)
    temperature: The temperature used in the Metropolis test (units are dependent on the model being used)
    '''
    def __init__(self, lattice, model, termini = None, first_structure = None, temperature = 1.0):
        self.lattice = lattice
        self.model = model
        if first_structure is None:
            self.last_structure = LatticeStructureFactory(self.model.natoms, self.lattice, termini = termini).random_avoid()
        else:
            self.last_structure = first_structure
        self.model.calculate_energy(self.last_structure)
        self.best_structure = self.last_structure
        self.best_energy = self.best_structure.energy
        self.mover = Reptate()
        self.step = 0
        if temperature > 0:
            self.rt = float(temperature)
        else:
            raise ValueError("temperature must be > 0")
        
    def run(self, steps):
        for self.step in range (self.step +1, self.step + steps + 1):
            structure = self.mover.move(self.last_structure)
            energy = self.model.calculate_energy(structure)
            #print self.step, structure.energy, self.last_structure.energy, self.best_structure.energy
            if structure.energy < self.best_structure.energy:
                self.best_structure = structure
                self.best_energy = energy
            if random.random() < metropolis_probability(self.last_structure.energy, structure.energy, self.rt):
                self.last_structure = structure
        return self.best_structure
    
def metropolis_probability(e1, e2, rt=1.0):
    '''Return the Metropolis acceptance probability:
    
    e1: initial enrgy
    e2: final energy
    rt: gas constant * temperature
    '''
    return min(exp(-((e2 - e1) / (rt))), 1.)