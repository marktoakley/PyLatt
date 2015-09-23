'''
@author: Mark Oakley
'''
import numpy as np
from abc import ABCMeta, abstractmethod

class Lattice():
    '''Abstract superclass for lattices.'''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_moves(self,point): pass
    '''Get a list of the moves accessible from a given pylatt point.
    Parameters:
    point: '''

class CubicLattice(Lattice):
    '''A 6-coordinate cubic pylatt.'''
    moves=np.array([[0,0,1],
                    [0,0,-1],
                    [0,1,0],
                    [0,-1,0],
                    [1,0,0],
                    [-1,0,0]])
    contact_length=1
    
    def get_moves(self, point):
        return self.moves

class SquareLattice(Lattice):
    '''A 4-coordinate square pylatt.
    This is two dimensional, with moves only along the x- and y-axes.'''
    moves=np.array([[1,0,0],
                    [-1,0,0],
                    [0,1,0],
                    [0,-1,0]])
    contact_length=1
    
    def get_moves(self, point):
        return self.moves

class BCCLattice(Lattice):
    '''An 8-coordinate body-centred cubic pylatt.'''
    moves=np.array([[1,1,1],
                    [1,1,-1],
                    [1,-1,1],
                    [1,-1,-1],
                    [-1,1,1],
                    [-1,1,-1],
                    [-1,-1,1],
                    [-1,-1,-1]])
    contact_length=3
    
    def get_moves(self, point):
        return self.moves
    
class FCCLattice(Lattice):
    '''A 12-coordinate face-centered cubic pylatt.'''
    moves=np.array([[1,1,0],
                    [1,-1,0],
                    [1,0,1],
                    [1,0,-1],
                    [0,1,1],
                    [0,1,-1],
                    [0,-1,1],
                    [0,-1,-1],
                    [-1,1,0],
                    [-1,-1,0],
                    [-1,0,1],
                    [-1,0,-1]])
    contact_length=2
    
    def get_moves(self, point):
        return self.moves
    
class DiamondLattice(Lattice):
    '''A 4-coordinate diamond pylatt.'''
    even_moves=np.array([[1,1,1],
                         [1,-1,-1],
                         [-1,-1,1],
                         [-1,1,-1]])
    odd_moves=np.array([[1,1,-1],
                        [1,-1,1],
                        [-1,-1,-1],
                        [-1,1,1]])
    contact_length=3
    
    def get_moves(self,point):
        if (sum(point) % 2) ==0:
            return self.even_moves
        else:
            return self.odd_moves