'''
@author:  Mark Oakley
'''
import unittest
from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.move import *
from pylatt.lattice import *

class MoveTest(unittest.TestCase):
    def setUp(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        self.factory = LatticeStructureFactory(len(sequence), lattice = CubicLattice())
        
    def test_corner_flip(self):
        structure = self.factory.random_avoid()
        mover = CornerFlip()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))
            self.assertFalse(structure.broken_chain())

    def test_end_flip(self):
        structure = self.factory.random_avoid()
        mover = EndFlip()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))
            self.assertFalse(structure.broken_chain())
            
    def test_reptate(self):
        structure = self.factory.random_avoid()
        mover = Reptate()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))        
            self.assertFalse(structure.broken_chain())

class MultiDomainTest(unittest.TestCase):
    def setUp(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        termini = [0, 8, 9, 17]
        self.factory = LatticeStructureFactory(len(sequence),
                                               lattice = CubicLattice(),
                                               termini = termini)
        
    def test_corner_flip(self):
        structure = self.factory.random_avoid()
        mover = CornerFlip()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))
            self.assertFalse(structure.broken_chain())
            self.assertEqual(2,structure.num_chains)

    def test_end_flip(self):
        structure = self.factory.random_avoid()
        mover = EndFlip()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))
            self.assertFalse(structure.broken_chain())
            self.assertEqual(2,structure.num_chains)
                        
    def test_reptate(self):
        structure = self.factory.random_avoid()
        mover = Reptate()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))        
            self.assertFalse(structure.broken_chain())
            self.assertEqual(2,structure.num_chains)
                        
if __name__ == "__main__":
    unittest.main()