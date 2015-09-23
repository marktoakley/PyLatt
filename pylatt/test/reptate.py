'''
@author:  Mark Oakley
'''
import unittest
from pylatt.lattice_structure import LatticeStructureFactory
from pylatt.reptate import Reptator

class ReptateTest(unittest.TestCase):
    
    def test_reptate(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        factory = LatticeStructureFactory(len(sequence))
        structure = factory.random_avoid()
        reptator = Reptator()
        new_structure = reptator.move(structure)
        self.assertEqual(0,len(new_structure.overlaps))
        
    
if __name__ == "__main__":
    unittest.main()