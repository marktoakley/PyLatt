'''
Created on 18 Sep 2015

@author: Mark Oakley
'''

import numpy as np
import random

from pylatt.lattice import CubicLattice
from __builtin__ import True

class LatticeStructure:
    '''Stores the coordinates and properties of pylatt model proteins.

    To generate new LatticeStructures, use the LatticeStructureFactory
    rather than the constructor in this class.'''
    
    def __init__(self,lattice,coords):
        self.lattice = lattice
        self.coords = np.array(coords)
        self.natoms = len(coords)
        self.make_contact_map()
            
    def make_contact_map(self):
        '''Generate the contact contact_map and overlap contact_map for a protein structure.'''
        self.contact_map = []
        self.overlap_map = []
        for i in range(0,self.natoms):
            for j in range(i+2,self.natoms):
                distance=0
                for k in range(0,3):
                    distance += (self.coords[i,k]-self.coords[j,k])**2
                if distance == 0:
                    self.overlap_map.append([i,j])
                elif distance == self.lattice.contact_length:
                    self.contact_map.append([i,j])
        return self.contact_map
    
    def free_moves(self, index):
        '''Return a list of unoccupied pylatt points surrounding a residue.'''
        moves = []
        for row in self.lattice.get_moves(self.coords[index]):
            if  not self.occupied(row+self.coords[index]):
                moves.append(row+self.coords[index])
        return moves
        
    def occupied(self,point):
        '''Check whether a pylatt point is occupied.'''
        return any(np.all(self.coords==point,axis=1))
    
    def broken_chain(self):
        '''Check for successive residues separated by more than one lattice point.
        If this returns True, there is probably a bug in the code used to make the LatticeStructure.'''
        for i in range(0, self.natoms-1):
            distance = 0
            for k in range(0,3):
                distance += (self.coords[i,k]-self.coords[i+1,k])**2
            if distance != self.lattice.contact_length:
                return True
        return False
                
                
            
    
class LatticeStructureFactory:
    '''Generate new LatticeStructures.'''
        
    def __init__(self, natoms, lattice=CubicLattice()):
        self.lattice = lattice
        self.natoms = natoms
            
    def random(self):
        '''Generate a random pylatt structure.
        
        This is not self-avoiding and can have overlapping beads.
        Using random_avoid is almost always a better choice.'''
        coords = np.zeros((self.natoms,3),dtype=int)
        for i in range(1,self.natoms):
            coords[i] = np.add(coords[i-1],random.choice(self.lattice.get_moves(coords[i-1])))
        structure=LatticeStructure(self.lattice,coords)
        structure.make_contact_map()
        return structure
        
    def random_avoid(self):
        '''Generate a self-avoiding random pylatt structure.
        
        Notes
        -----
        In low-coordinate lattices, traps with no free moves become
        more likely. This method repeatedly generates random structures
        until it finds one that is not trapped.'''
        trapped=True
        while trapped:
            trapped = False
            coords = np.zeros((self.natoms,3),dtype=int)
            structure = LatticeStructure(self.lattice,coords)
            for i in range(1,self.natoms):
                next_move = structure.free_moves(i-1)
                if len(next_move) == 0:
                    trapped = True
                    break
                my_move=random.choice(next_move)
                structure.coords[i] = my_move
            structure.make_contact_map()
        return structure
                
            