'''
Classes of moves for Monte Carlo searches

Notes
-----
This is also an attempt to sort out the interface for a generic move
superclass.

@author: Mark Oakley
'''
import random
import numpy as np
from abc import ABCMeta, abstractmethod

from pylatt.lattice_structure import LatticeStructure

class Move:
    '''Abstract superclass for moves.'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self,structure):
        '''Take a generate a new LatticeStructure by performing one step from
        an existing LatticeStructure.'''
        pass
    
class CornerFlip(Move):
    
    def move(self, structure):
        trapped = True
        while trapped:
            trapped = False
            move_res = random.randint(1,structure.natoms-2)
            if (structure.chainID[move_res-1]!=structure.chainID[move_res+1]):
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
        new_structure = LatticeStructure(structure.lattice, coords, model = structure.model, chainID = structure.chainID)
        return new_structure

class EndFlip(Move):
    
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
        new_structure = LatticeStructure(structure.lattice, coords, model = structure.model, chainID = structure.chainID)
        return new_structure

class Reptate(Move):
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
        new_structure = LatticeStructure(structure.lattice, coords, model = structure.model, chainID = structure.chainID)
        return new_structure
            