'''
@author:  Mark Oakley
'''
import unittest

from pylatt.lattice_structure import *
from pylatt.move import *
from pylatt.lattice import *

class MoveTest(unittest.TestCase):
    def setUp(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        self.structure = random_avoid(len(sequence), CubicLattice())
        
    def test_corner_flip(self):      
        mover = CornerFlip()
        for i in range (1, 1000):
            self.structure = mover.move(self.structure)
            self.assertEqual(0,len(self.structure.overlap_map))
            self.assertFalse(self.structure.broken_chain())

    def test_end_flip(self):
        mover = EndFlip()
        for i in range (1, 1000):
            self.structure = mover.move(self.structure)
            self.assertEqual(0,len(self.structure.overlap_map))
            self.assertFalse(self.structure.broken_chain())
            
    def test_reptate(self):
        mover = Reptate()
        for i in range (1, 1000):
            self.structure = mover.move(self.structure)
            self.assertEqual(0,len(self.structure.overlap_map))        
            self.assertFalse(self.structure.broken_chain())

class MultiDomainTest(unittest.TestCase):
    def setUp(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        chain_list = [9, 9]
        self.structure = random_avoid(len(sequence),lattice = CubicLattice(),chain_list = chain_list)
        
    def test_corner_flip(self):
        mover = CornerFlip()
        for i in range (1, 1000):
            self.structure = mover.move(self.structure)
            self.assertEqual(0,len(self.structure.overlap_map))
            self.assertFalse(self.structure.broken_chain())
            self.assertEqual(2,self.structure.num_chains)

    def test_end_flip(self):
        mover = EndFlip()
        for i in range (1, 1000):
            self.structure = mover.move(self.structure)
            self.assertEqual(0,len(self.structure.overlap_map))
            self.assertFalse(self.structure.broken_chain())
            self.assertEqual(2,self.structure.num_chains)
                        
    def test_reptate(self):
        mover = Reptate()
        for i in range (1, 1000):
            self.structure = mover.move(self.structure)
            self.assertEqual(0,len(self.structure.overlap_map))        
            self.assertFalse(self.structure.broken_chain())
            self.assertEqual(2,self.structure.num_chains)
                        
if __name__ == "__main__":
    unittest.main()