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

class CornerFlip:
    
    def move(self, structure):
        trapped = True
        while trapped:
            trapped = False
            move_res = random.randint(1,structure.natoms-2)
            if move_res in structure.termini:
                trapped=True
            move1 = structure.free_moves(move_res-1)
            move2 = structure.free_moves(move_res+1)
            next_move=[]
            for i in move1:
                for j in move2:
                    if np.all(i == j):
                        next_move.append(i)
            if len(next_move) == 0:
                trapped = True    
        my_move = random.choice(next_move)        
        coords = np.copy(structure.coords)
        coords[move_res] = my_move
        new_structure = LatticeStructure(structure.lattice, coords, termini = structure.termini)
        return new_structure

class EndFlip:
    
    def move(self, structure):
        trapped = True

        while trapped:
            trapped = False
            index = random.randint(0, len(structure.termini)-1)
            move_res =structure.termini[index]
            if index%2==0: # First in chain
                next_move = structure.free_moves(move_res+1)
            else: # Last in chain
                next_move = structure.free_moves(move_res-1)
            if len(next_move) == 0:
                trapped = True     
        my_move = random.choice(next_move)        
        coords = np.copy(structure.coords)
        coords[move_res] = my_move
        new_structure = LatticeStructure(structure.lattice, coords, termini = structure.termini)
        return new_structure

class Reptate:
    '''Move by reptation.'''
    
    def move(self, structure):
        '''Take a LatticeStructure and return another one by
        performing a reptation move.'''
        coords = np.copy(structure.coords)
        trapped = True
        while trapped:
            index = random.randint(0, len(structure.termini)-1)
            move_res =structure.termini[index]
            trapped = False
            next_move = structure.free_moves(move_res)
            if len(next_move) == 0:
                trapped = True
        my_move = random.choice(next_move)
        if index%2==0: # First in chain
            end = structure.termini[index+1]
            coords[move_res] = my_move
            for i in range(move_res+1,end+1):
                coords[i] = structure.coords[i-1]
        else: # Last in chain
            end = structure.termini[index-1]
            coords[move_res] = my_move
            for i in range(end, move_res):
                coords[i] = structure.coords[i+1]
        new_structure = LatticeStructure(structure.lattice, coords, termini = structure.termini)
        return new_structure
            