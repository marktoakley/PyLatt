'''
@author:  Mark Oakley
'''
import unittest
from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.move import *
from pylatt.lattice import *

class MoveTest(unittest.TestCase):

    
    def test_corner_flip(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        factory = LatticeStructureFactory(len(sequence), lattice = FCCLattice())
        structure = factory.random_avoid()
        mover = CornerFlip()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))

    def test_end_flip(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        factory = LatticeStructureFactory(len(sequence), lattice = FCCLattice())
        structure = factory.random_avoid()
        mover = EndFlip()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))

    def test_reptate(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        factory = LatticeStructureFactory(len(sequence), lattice = SquareLattice())
        structure = factory.random_avoid()
        mover = Reptate()
        for i in range (1, 1000):
            structure = mover.move(structure)
            self.assertEqual(0,len(structure.overlap_map))        
    
if __name__ == "__main__":
    unittest.main()