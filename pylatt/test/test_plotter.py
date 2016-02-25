'''
Unit tests for structure plotters using matplotlib

@author: Mark Oakley
'''
import unittest
from pylatt.lattice import CubicLattice, SquareLattice
from pylatt.lattice_structure import random_avoid
from pylatt.plotter import plot_contact_map, plot_2d, plot_3d

class plotterTest(unittest.TestCase):
        
    def test_2d(self):
        structure=random_avoid(100, SquareLattice())
        self.assertIsNotNone(plot_2d(structure))
        self.assertIsNotNone(plot_contact_map(structure))
    
    def test_3d(self):
        structure=random_avoid(150, CubicLattice())
        self.assertIsNotNone(plot_3d(structure))
    
    def test_multidomain(self):
        structure=random_avoid(20, CubicLattice(), chain_list=[10,10])
        self.assertIsNotNone(plot_3d(structure))
        self.assertIsNotNone(plot_contact_map(structure))
        
if __name__ == "__main__":
    unittest.main()