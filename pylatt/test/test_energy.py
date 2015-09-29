'''
@author: Mark Oakley
'''

import unittest
from pylatt.model import HP
from pylatt.lattice_structure import LatticeStructure
from pylatt.lattice import CubicLattice

class HPPotentialTest(unittest.TestCase):
    def setUp(self):
        self.model = HP("HHPPHH")
        
    def test_energy_hairpin(self):
        structure = LatticeStructure(CubicLattice(),
                                     [[0,0,0],
                                      [0,0,1],
                                      [0,0,2],
                                      [0,1,2],
                                      [0,1,1],
                                      [0,1,0]])
        structure.make_contact_map()
        self.assertEqual(-2,self.model.calculate_energy(structure))
        
            
    def test_energy_s(self):
        structure = LatticeStructure(CubicLattice(),
                                     [[0,0,0],
                                      [0,0,1],
                                      [0,1,1],
                                      [0,1,0],
                                      [0,2,0],
                                      [0,2,1]])
        structure.make_contact_map()
        self.assertEqual(0,self.model.calculate_energy(structure))

if __name__ == "__main__":
    unittest.main()