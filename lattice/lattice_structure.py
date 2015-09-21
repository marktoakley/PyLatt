'''
Created on 18 Sep 2015

@author: Mark Oakley
'''

import numpy as np
import random

class Lattice_Structure:
    
    def __init__(self,lattice,coords):
        self.lattice = lattice
        self.coords=coords
        self.natoms=len(coords)
        self.overlaps=[]
            
    def make_contact_map(self):
        self.map=[]
        self.overlaps=[]
        for i in range(0,self.natoms):
            for j in range(i+2,self.natoms):
                distance=0
                for k in range(0,3):
                    distance+=(self.coords[i,k]-self.coords[j,k])**2
                if distance==0:
                    self.overlaps.append([i,j])
                elif distance==self.lattice.contact_length**2:
                    self.map.append([i,j])

        return self.map
    
    def occupied(self,point):
        '''Check whether a lattice point is occupied.'''
        return any(np.all(self.coords==point,axis=1))
    
class Lattice_Structure_Factory:
        def __init__(self,sequence,lattice):
            self.sequence=sequence
            self.lattice=lattice
            self.natoms=len(self.sequence)
            
        def random(self):
            '''Generate a random lattice structure. This is not self-avoiding and can have overlapping beads.'''
            coords=np.zeros((self.natoms,3),dtype=int)
            for i in range(1,self.natoms):
                coords[i] = np.add(coords[i-1],self.lattice.get_random_move())
            structure=Lattice_Structure(self.lattice,coords)
            structure.make_contact_map()
            return structure
        
        def random_avoid(self):
            '''Generate a self-avoiding random lattice structure..'''
            coords=np.zeros((self.natoms,3),dtype=int)
            structure=Lattice_Structure(self.lattice,coords)
            for i in range(1,self.natoms):
                next_move = []
                for row in self.lattice.moves:
                    if  not structure.occupied(row+coords[i-1]):
                        next_move.append(row+coords[i-1])
                my_move=random.choice(next_move)
                coords[i] = my_move
            structure.make_contact_map()
            return structure
                
            