'''
Unit tests for structure plotters using matplotlib

@author: Mark Oakley
'''
import unittest

from pylatt.lattice import CubicLattice, SquareLattice
from pylatt.lattice_structure import random_avoid
from pylatt.plotter import plot_contact_map, plot_2d, plot_3d, plot_fit
from pylatt.off_lattice import read_from_iterable, to_lattice

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
        
    def test_fit(self):
        pdb = ["ATOM      1  N   GLY A   1      -8.863  16.944  14.289  1.00 21.88", 
               "ATOM      2  CA  GLY A   1      -9.929  17.026  13.244  1.00 22.85",
               "ATOM      3  C   GLY A   1     -10.051  15.625  12.618  1.00 43.92",
               "ATOM      4  O   GLY A   1      -9.782  14.728  13.407  1.00 25.22",
               "ATOM      5  N   ILE A   2     -10.333  15.531  11.332  1.00 26.28",
               "ATOM      6  CA  ILE A   2     -10.488  14.266  10.600  1.00 20.84",
               "ATOM      7  C   ILE A   2      -9.367  13.302  10.658  1.00 11.81",
               "ATOM      8  O   ILE A   2      -9.580  12.092  10.969  1.00 20.31",
               "ATOM      9  CB  ILE A   2     -10.883  14.493   9.095  1.00 40.00",
               "ATOM     10  CG1 ILE A   2     -11.579  13.146   8.697  1.00 36.74",
               "ATOM     11  CG2 ILE A   2      -9.741  14.794   8.140  1.00 23.02",
               "ATOM     12  CD1 ILE A   2     -12.813  13.031   9.640  1.00 26.69",
               "ATOM     13  N   VAL A   3      -8.133  13.759  10.483  1.00 16.57",
               "ATOM     14  CA  VAL A   3      -6.966  12.901  10.576  1.00 15.75",
               "ATOM     15  C   VAL A   3      -6.892  12.161  11.922  1.00 22.09",
               "ATOM     16  O   VAL A   3      -6.547  10.990  12.037  1.00 24.52",
               "ATOM     17  CB  VAL A   3      -5.697  13.708  10.225  1.00 21.34",
               "ATOM     18  CG1 VAL A   3      -4.382  12.960  10.448  1.00 32.48",
               "ATOM     19  CG2 VAL A   3      -5.842  14.209   8.777  1.00 26.35",]
        off_latt = read_from_iterable(pdb)
        on_latt = to_lattice(off_latt, CubicLattice())
        self.assertIsNotNone(plot_fit(on_latt))
        
if __name__ == "__main__":
    unittest.main()