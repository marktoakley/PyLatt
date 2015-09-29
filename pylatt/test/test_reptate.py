'''
@author:  Mark Oakley
'''
import unittest
from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.reptate import Reptator
from pylatt.lattice import SquareLattice

class ReptateTest(unittest.TestCase):
    
    def test_reptate(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        factory = LatticeStructureFactory(len(sequence), lattice = SquareLattice())
        structure = factory.random_avoid()
        reptator = Reptator()
        for i in range (1, 1000):
            print i
            structure = reptator.move(structure)
            self.assertEqual(0,len(structure.overlap_map))
        
    
if __name__ == "__main__":
    unittest.main()