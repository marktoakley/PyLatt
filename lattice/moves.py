'''
@author: Mark Oakley
'''
import numpy as np

class LatticeMoves():
    
    def get_random_move(self):
        return self.moves[np.random.randint(0,len(self.moves))]

class CubicLattice(LatticeMoves):
    moves=np.array([[0,0,1],
                    [0,0,-1],
                    [0,1,0],
                    [0,-1,0],
                    [1,0,0],
                    [-1,0,0]])
    contact_length=1

class SquareLattice(LatticeMoves):
    moves=np.array([[1,0,0],
                    [-1,0,0],
                    [0,1,0],
                    [0,-1,0]])
    contact_length=1

class BCCLattice(LatticeMoves):
    moves=np.array([[1,1,1],
                    [1,1,-1],
                    [1,-1,1],
                    [1,-1,-1],
                    [-1,1,1],
                    [-1,1,-1],
                    [-1,-1,1],
                    [-1,-1,-1]])
    contact_length=3
    
class FCCLattice(LatticeMoves):
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