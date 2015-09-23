'''
Move by reptation.

Notes
-----
This is also an attempt to sort out the interface for a generic move
superclass.

@author: Mark Oakley
'''
import random
import numpy as np
from pylatt.lattice_structure import LatticeStructure

class Reptator:
    '''Move by reptation.'''
    
    def move(self, structure):
        '''Take a LatticeStructure and return another one by
        performing a reptation move.'''
        
        coords = np.zeros((structure.natoms,3),dtype=int)
        trapped = True
        while trapped:
            trapped = False
            if random.random() < 0.5: # Choose terminus to move
                move_res=0
            else:
                move_res=structure.natoms-1
            next_move = structure.free_moves(move_res)
            if len(next_move) == 0:
                trapped = True
                break
        my_move = random.choice(next_move)
        if move_res == 0:
            coords[0] = my_move
            for i in range(1,structure.natoms):
                coords[i] = structure.coords[i-1]
        else:
            coords[move_res] = my_move
            for i in range(0,structure.natoms-1):
                coords[i] = structure.coords[i+1]
        new_structure = LatticeStructure(structure.lattice, coords)
        new_structure.make_contact_map()
        return new_structure
            