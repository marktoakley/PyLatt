'''
The two-colour hydrophobic-polar model.

@author: Mark Oakley
'''
from abc import ABCMeta, abstractmethod

class Potential():
    '''Superclass for interaction potentials.'''
    __metaclass__ = ABCMeta
        
    @abstractmethod
    def calculate_energy(self, structure): pass
    '''Calculate the energy of a LatticeStructure.'''
    
    def calculate_pair_energy(self,structure):
        '''Calculate the pairwise energy component for a LatticeStructure.'''
        energy = 0
        structure.make_contact_map()
        for contact in structure.contact_map:
            energy += self.pair_potential[self.isequence[contact[0]]][self.isequence[contact[1]]]
        structure.energy = energy
        return energy    
    
    def read_sequence(self, sequence):
        '''Set the protein sequence used in the model.
        The sequence is a string of single-letter amino acid codes.
        '''
        self.sequence = sequence
        self.natoms = len(sequence)
        self.isequence = []
        for c in list(sequence):
            try:
                self.isequence.append(self.labels.index(c))
            except ValueError:
                print ("Unknown residue type: ",c)
                raise

class HP(Potential):
    '''The Hydrophobic Polar model.'''
    
    def __init__(self,sequence):
        '''Set up the hydrophobic-polar model.
        
        See:
        K. F. Lau and K. A. Dill, Macromolecules, 1989, 22, 3986-3997, doi:10.1021/ma00200a030
        
        The parameter sequence is a string of "H" and "P" characters
        (e.g. "PPHHHPHHHP") denoting each residue as hydrophobic or polar.'''
        self.labels="HP"
        self.pair_potential = [[-1,0],
                               [0,0]]
        self.read_sequence(sequence)
        
    def calculate_energy(self, structure):
        return self.calculate_pair_energy(structure)

    
class MJ(Potential):
    '''The Miyazawa-Jernigan potential (just the pairwise part for now).
    
    See:
    S. Miyazawa and R. L. Jernigan, J. Mol. Biol., 1996, 256, 623-644, doi:10.1006/jmbi.1996.0114
    '''
    def __init__(self, sequence):
        self.labels = "CMFILVWYAGTSNQDEHRKP"
        self.pair_potential = [[ -5.44, -4.99, -5.8, -5.5, -5.83, -4.96, -4.95, -4.16, -3.57, -3.16, -3.11, -2.86, -2.59, -2.85, -2.41, -2.27, -3.6, -2.57, -1.95, -3.07 ],
                               [ -4.99, -5.46, -6.56, -6.02, -6.41, -5.32, -5.55, -4.91, -3.94, -3.39, -3.51, -3.03, -2.95, -3.3, -2.57, -2.89, -3.98,-3.12, -2.48, -3.45 ],
                               [ -5.8, -6.56, -7.26, -6.84, -7.28, -6.29, -6.16, -5.66, -4.81, -4.13, -4.28, -4.02, -3.75, -4.1, -3.48, -3.56, -4.77,-3.98, -3.36, -4.25 ],
                               [ -5.5, -6.02, -6.84, -6.54, -7.04, -6.05, -5.78, -5.25, -4.58,-3.78, -4.03, -3.52, -3.24, -3.67, -3.17, -3.27, -4.14,-3.63, -3.01, -3.76 ],
                               [ -5.83, -6.41, -7.28, -7.04, -7.37, -6.48, -6.14, -5.67, -4.91, -4.16, -4.34, -3.92, -3.74, -4.04, -3.4, -3.59, -4.54, -4.03, -3.37, -4.2 ],
                               [ -4.96, -5.32, -6.29, -6.05, -6.48, -5.52, -5.18, -4.62, -4.04,-3.38, -3.46, -3.05, -2.83, -3.07, -2.48, -2.67, -3.58, -3.07, -2.49, -3.32 ],
                               [ -4.95, -5.55, -6.16, -5.78, -6.14, -5.18, -5.06, -4.66, -3.82, -3.42, -3.22, -2.99, -3.07, -3.11, -2.84, -2.99, -3.98,-3.41, -2.69, -3.73 ],
                               [ -4.16, -4.91, -5.66, -5.25, -5.67, -4.62, -4.66, -4.17, -3.36,-3.01, -3.01, -2.78, -2.76, -2.97, -2.76, -2.79, -3.52,-3.16, -2.6, -3.19 ],
                               [ -3.57, -3.94, -4.81, -4.58, -4.91, -4.04, -3.82, -3.36, -2.72, -2.31, -2.32, -2.01, -1.84, -1.89, -1.7, -1.51, -2.41, -1.83, -1.31, -2.03 ],
                               [ -3.16, -3.39, -4.13, -3.78, -4.16, -3.38, -3.42, -3.01, -2.31, -2.24, -2.08, -1.82, -1.74, -1.66, -1.59, -1.22, -2.15, -1.72, -1.15, -1.87 ],
                               [ -3.11, -3.51, -4.28, -4.03, -4.34, -3.46, -3.22, -3.01, -2.32, -2.08, -2.12, -1.96, -1.88, -1.9, -1.8, -1.74, -2.42, -1.9, -1.31, -1.9 ],
                               [ -2.86, -3.03, -4.02, -3.52, -3.92, -3.05, -2.99, -2.78, -2.01,-1.82, -1.96, -1.67, -1.58, -1.49, -1.63, -1.48, -2.11, -1.62, -1.05, -1.57 ],
                               [ -2.59, -2.95, -3.75, -3.24, -3.74, -2.83, -3.07, -2.76, -1.84, -1.74, -1.88, -1.58, -1.68, -1.71, -1.68, -1.51, -2.08, -1.64, -1.21, -1.53 ],
                               [ -2.85, -3.3, -4.1, -3.67, -4.04, -3.07, -3.11, -2.97, -1.89,-1.66, -1.9, -1.49, -1.71, -1.54, -1.46, -1.42, -1.98, -1.8, -1.29, -1.73 ],
                               [-2.41, -2.57, -3.48, -3.17, -3.4, -2.48, -2.84, -2.76, -1.7, -1.59, -1.8, -1.63, -1.68, -1.46, -1.21, -1.02, -2.32,-2.29, -1.68, -1.33 ],
                               [ -2.27, -2.89, -3.56, -3.27, -3.59, -2.67, -2.99, -2.79, -1.51,-1.22, -1.74, -1.48, -1.51, -1.42, -1.02, -0.91, -2.15,-2.27, -1.8, -1.26 ],
                               [ -3.6, -3.98, -4.77, -4.14, -4.54, -3.58, -3.98, -3.52, -2.41,-2.15, -2.42, -2.11, -2.08, -1.98, -2.32, -2.15, -3.05,-2.16, -1.35, -2.25 ],
                               [ -2.57, -3.12, -3.98, -3.63, -4.03, -3.07, -3.41, -3.16, -1.83,-1.72, -1.9, -1.62, -1.64, -1.8, -2.29, -2.27, -2.16,-1.55, -0.59, -1.7 ],
                               [ -1.95, -2.48, -3.36, -3.01, -3.37, -2.49, -2.69, -2.6, -1.31, -1.15, -1.31, -1.05, -1.21, -1.29, -1.68, -1.8, -1.35,-0.59, -0.12, -0.97 ],
                               [-3.07, -3.45, -4.25, -3.76, -4.2, -3.32, -3.73, -3.19, -2.03,-1.87, -1.9, -1.57, -1.53, -1.73, -1.33, -1.26, -2.25,-1.7, -0.97, -1.75 ]]
        self.read_sequence(sequence)
        
    def calculate_energy(self, structure):
        return self.calculate_pair_energy(structure)
