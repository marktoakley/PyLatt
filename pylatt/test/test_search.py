'''
@author:  Mark Oakley
'''
import unittest
from pylatt.model import HP
from pylatt.lattice import SquareLattice
from pylatt.search import *

class RandomTest(unittest.TestCase):
    
    def test_restart(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        model = HP(sequence)
        lattice = SquareLattice()
        search = RandomSearch(lattice, model)
        search.run(10)
        self.assertEqual(10, search.step)
        energy1 = search.best_energy
        search.run(10)
        self.assertEqual(20, search.step)
        energy2 = search.best_energy
        self.assertLessEqual(energy2, energy1)
        

class MonteCarloTest(unittest.TestCase):
    
    def test_restart(self):
        sequence = "PHPPHPHHHPHHPHHHHH"
        model = HP(sequence)
        lattice = SquareLattice()
        search = MonteCarlo(lattice, model)
        search.run(10)
        self.assertEqual(10, search.step)
        energy1 = search.best_energy
        search.run(10)
        self.assertEqual(20, search.step)
        energy2 = search.best_energy
        self.assertLessEqual(energy2, energy1)
        
class MetropolisTest(unittest.TestCase):
    
    def test_metropolis(self):
        self.assertAlmostEqual(0.368, metropolis_probability(1.0, 2.0), delta=0.001)
        self.assertAlmostEqual(1.0, metropolis_probability(2.0, 1.0), delta=0.001)
        
if __name__ == "__main__":
    unittest.main()