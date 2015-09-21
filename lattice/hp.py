'''
The two-colour hydrophobic-polar potential.

@author: Mark Oakley
'''

class HPPotential:
    '''The hydrophobic polar potential.'''
    
    def __init__(self,sequence):
        '''Set up the hydrophobic-polar potential.
        
        The parameter sequence is a string of "H" and "P" characters
        (e.g. "PPHHHPHHHP") denoting each residue as hydrophobic or polar.'''
        self.potential = [[-1,0],
                          [0,0]]
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
            energy += self.potential[self.isequence[contact[0]]][self.isequence[contact[1]]]
        return energy