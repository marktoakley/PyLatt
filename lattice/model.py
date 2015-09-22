'''
The two-colour hydrophobic-polar model.

@author: Mark Oakley
'''

class HP:
    '''The Hydrophobic Polar model.'''
    
    def __init__(self,sequence):
        '''Set up the hydrophobic-polar model.
        
        The parameter sequence is a string of "H" and "P" characters
        (e.g. "PPHHHPHHHP") denoting each residue as hydrophobic or polar.'''
        self.pair_potential = [[-1,0],
                               [0,0]]
        self.sequence = sequence
        self.natoms = len(sequence)
        self.isequence = []
        for c in list(sequence):
            if c == 'H':
                self.isequence.append(0)
            elif c == 'P':
                self.isequence.append(1)

    def calculate_energy(self,structure):
        '''Calculate the energy of a LatticeStructure.'''
        energy = 0
        for contact in structure.map:
            energy += self.pair_potential[self.isequence[contact[0]]][self.isequence[contact[1]]]
        return energy