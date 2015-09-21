'''
@author: Mark Oakley
'''

import unittest
from lattice.hp import HPPotential
from lattice.lattice_structure import LatticeStructure
from lattice.moves import CubicLattice

class HPPotentialTest(unittest.TestCase):
    def setUp(self):
        self.potential = HPPotential("HHPPHH")
        
    def test_energy_hairpin(self):
        structure = LatticeStructure(CubicLattice(),
                                     [[0,0,0],
                                      [0,0,1],
                                      [0,0,2],
                                      [0,1,2],
                                      [0,1,1],
                                      [0,1,0]])
        structure.make_contact_map()
        self.assertEqual(-2,self.potential.calculate_energy(structure))
        
            
    def test_energy_s(self):
        structure = LatticeStructure(CubicLattice(),
                                     [[0,0,0],
                                      [0,0,1],
                                      [0,1,1],
                                      [0,1,0],
                                      [0,2,0],
                                      [0,2,1]])
        structure.make_contact_map()
        self.assertEqual(0,self.potential.calculate_energy(structure))

if __name__ == "__main__":
    unittest.main()