'''
@author: Mark Oakley
'''

import numpy as np
import random

from pylatt.lattice import CubicLattice

class LatticeStructure:
    '''Stores the coordinates and properties of pylatt model proteins.

    To generate new LatticeStructures, use the LatticeStructureFactory
    rather than the constructor in this class.'''
    
    def __init__(self,lattice,coords,termini=None):
        self.lattice = lattice
        self.coords = np.array(coords)
        self.natoms = len(coords)
        if termini == None:
            self.termini = [0, self.natoms -1]
        else:
            self.termini = termini
        self.num_chains = len(self.termini)/2
        self.contact_map = None
        self.overlap_map = None
        self.coordination_no = None
        self.make_contact_map()
        self.energy = None
            
    def make_contact_map(self):
        '''Generate the contact contact_map, overlap_map coordination_no for a protein structure.'''
        self.contact_map = []
        self.overlap_map = []
        self.coordination_no = [0] * self.natoms
        #Look for distant pairs
        for i in range(0,self.natoms):
            for j in range(i+2,self.natoms):
                distance=self.get_distance2(i, j)
                if distance == 0:
                    self.overlap_map.append([i,j])
                elif distance == self.lattice.contact_length:
                    self.contact_map.append([i,j])
                    self.coordination_no[i] += 1
                    self.coordination_no[j] += 1
        # Look for contacts between termini
        for index in range(0, len(self.termini)-1):
            i = self.termini[index]
            j = self.termini[index +1]
            if j - i ==1:
                distance=self.get_distance2(i, j)
                if distance == 0:
                    self.overlap_map.append([i,j])
                elif distance == self.lattice.contact_length:
                    self.contact_map.append([i,j])
                    self.coordination_no[i] += 1
                    self.coordination_no[j] += 1
                
        return self.contact_map
    
    def get_distance2(self, i, j):
        '''Return the square of the distance between residues with indices i and j.'''
        distance=0
        for k in range(0,3):
            distance += (self.coords[i,k]-self.coords[j,k])**2
        return distance
    
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
                if not ((i in self.termini) and (i+1 in self.termini)): 
                    return True
        return False
                
class LatticeStructureFactory:
    '''Generate new LatticeStructures.'''
        
    def __init__(self, natoms, lattice=CubicLattice(), termini=None):
        self.lattice = lattice
        self.natoms = natoms
        self.termini = termini
            
    def random(self):
        '''Generate a random pylatt structure.
        
        This is not self-avoiding and can have overlapping beads.
        Using random_avoid is almost always a better choice.'''
        coords = np.zeros((self.natoms,3),dtype=int)
        for i in range(1,self.natoms):
            coords[i] = np.add(coords[i-1],random.choice(self.lattice.get_moves(coords[i-1])))
        structure=LatticeStructure(self.lattice,coords,termini =self.termini)
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
            structure = LatticeStructure(self.lattice,coords,termini=self.termini)
            for i in range(1,self.natoms):
                next_move = structure.free_moves(i-1)
                if len(next_move) == 0:
                    trapped = True
                    break
                my_move=random.choice(next_move)
                structure.coords[i] = my_move
            structure.make_contact_map()
        return structure
                
            