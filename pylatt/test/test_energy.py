'''
@author: Mark Oakley
'''

import unittest
from pylatt.model import *
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
        self.assertEqual(-2,self.model.calculate_energy(structure))
        
            
    def test_energy_s(self):
        structure = LatticeStructure(CubicLattice(),
                                     [[0,0,0],
                                      [0,0,1],
                                      [0,1,1],
                                      [0,1,0],
                                      [0,2,0],
                                      [0,2,1]])
        self.assertEqual(0,self.model.calculate_energy(structure))
        
class MJPotentialTest(unittest.TestCase):
    def setUp(self):
        self.model = MJ("AGAGGG")
        
    def test_energy_hairpin(self):
        structure = LatticeStructure(CubicLattice(),
                                     [[0,0,0],
                                      [0,0,1],
                                      [0,0,2],
                                      [0,1,2],
                                      [0,1,1],
                                      [0,1,0]])
        self.assertAlmostEqual(-4.55,
                               self.model.calculate_energy(structure),
                               delta = 0.001)

class BadResidueTest(unittest.TestCase):
    
    def test_HP(self):
        with self.assertRaises(ValueError):
            self.model = HP("QWERTY")
            
    def test_MJ(self):
        with self.assertRaises(ValueError):
            self.model = MJ("AAGBA")

if __name__ == "__main__":
    unittest.main()