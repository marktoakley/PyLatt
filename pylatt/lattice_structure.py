'''
@author: Mark Oakley
'''

import numpy as np
import random

from pylatt.lattice import CubicLattice
import pylatt.termini as termini

class LatticeStructure:
    '''Stores the coordinates and properties of pylatt model proteins.

    To generate new LatticeStructures, use the LatticeStructureFactory
    rather than the constructor in this class.'''
    
    def __init__(self,lattice,coords,model=None,chain_list=None,chainID=None,):
        self.lattice = lattice
        self.coords = np.array(coords)
        self.natoms = len(coords)
        self.model=model
        if chainID is not None:
            self.num_chains = len(set(chainID))
            self.chainID = chainID
        elif chain_list is None:
            self.num_chains=1
            self.chainID = self.natoms * [0]
        else:
            self.chainID = []
            self.num_chains = len(chain_list)
            curr_chain = 0
            for i in chain_list:
                for j in range(0, i):
                    self.chainID.append(curr_chain)
                curr_chain += 1
        self.termini = termini.find(self.chainID)
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
            for j in range(i+1,self.natoms):
                if ((j - i > 2) or
                    (self.chainID[i] != self.chainID[j])):
                    distance=self.get_distance2(i, j)
                    if distance == 0:
                        self.overlap_map.append([i,j])
                    elif distance == self.lattice.contact_length:
                        self.contact_map.append([i,j])
                        self.coordination_no[i] += 1
                        self.coordination_no[j] += 1
                
        return self.contact_map
    
    def get_distance2(self, i, j):
        '''Return the square of the distance between residues with indices i and j.
        If the distance is larger than the lattice contact distance, an arbitrary
        large value is returned.'''
        distance=0
        for k in range(0,3):
            distance += (self.coords[i,k]-self.coords[j,k])**2
            # Stop looping through axes as soon as it's clear the residues are
            # not in contact.
            if (distance > self.lattice.contact_length):
                distance = self.lattice.contact_length*2
                break
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
                if (self.chainID[i] == self.chainID[i+1]): 
                    return True
        return False
                
            
# def random(natoms, lattice=CubicLattice(), chain_list=None):
#     '''Generate a random pylatt structure.
#     
#     This is not self-avoiding and can have overlapping beads.
#     Using random_avoid is almost always a better choice.'''
#     coords = np.zeros((natoms,3),dtype=int)
#     for i in range(1,natoms):
#         coords[i] = np.add(coords[i-1],random.choice(lattice.get_moves(coords[i-1])))
#     structure=LatticeStructure(lattice,coords,chain_list =chain_list)
#     structure.make_contact_map()
#     return structure
        
def random_avoid(natoms, lattice=CubicLattice(), model = None, chain_list=None):
    '''Generate a self-avoiding random pylatt structure.
    
    Notes
    -----
    In low-coordinate lattices, traps with no free moves become
    more likely. This method repeatedly generates random structures
    until it finds one that is not trapped.'''
    trapped=True
    while trapped:
        trapped = False
        coords = np.zeros((natoms,3),dtype=int)
        structure = LatticeStructure(lattice,coords,model=model,chain_list=chain_list)
        for i in range(1,natoms):
            next_move = structure.free_moves(i-1)
            if len(next_move) == 0:
                trapped = True
                break
            my_move=random.choice(next_move)
            structure.coords[i] = my_move
        structure.make_contact_map()
    return structure
                
            
