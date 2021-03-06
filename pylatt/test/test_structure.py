'''
@author: Mark Oakley
'''
import unittest
from pylatt.lattice import CubicLattice, SquareLattice
from pylatt.lattice_structure import LatticeStructure,random_avoid

class StructureTest(unittest.TestCase):
    
    def test_broken(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,5,1],
                [0,5,0]]
        structure=LatticeStructure(lattice,coords)
        self.assertTrue(structure.broken_chain())
        

    def test_contact_map(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,1,1],
                [0,1,0]]
        structure=LatticeStructure(lattice,coords)
        structure.make_contact_map()
        self.assertEqual(1,len(structure.contact_map))
        self.assertEqual(0,len(structure.overlap_map))
        self.assertEqual(1,structure.num_chains)
        self.assertEqual(1,structure.coordination_no[0])
        self.assertEqual(0,structure.coordination_no[1])
        
    def test_free_moves(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,1,1],
                [0,1,0]]
        structure=LatticeStructure(lattice,coords)
        structure.make_contact_map()
        self.assertEqual(4,len(structure.free_moves(0)))
        
    def test_multidomain(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,0,2],
                [0,0,3],
                [0,1,3],
                [0,1,2],
                [0,1,1],
                [0,1,0]]
        structure=LatticeStructure(lattice,coords, chain_list=[4,4])
        structure.make_contact_map()
        self.assertEqual(4,len(structure.contact_map))
        self.assertEqual(0,len(structure.overlap_map))
        self.assertFalse(structure.broken_chain())
        self.assertEqual(2,structure.num_chains)
        self.assertEqual(1,structure.coordination_no[0])
        self.assertEqual(1,structure.coordination_no[1])
                
    def test_overlap(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,0,0]]
        structure=LatticeStructure(lattice,coords)
        structure.make_contact_map()
        self.assertEqual(0,len(structure.overlap_map))
        self.assertEqual(1,structure.num_chains)

class FactoryTest(unittest.TestCase):
        
    def test_avoid(self):
        structure=random_avoid(100, CubicLattice())
        self.assertEqual(0,len(structure.overlap_map))
        self.assertEqual(1,structure.num_chains)
    
    def test_trapping(self):
        structure=random_avoid(150, SquareLattice())
        self.assertEqual(0,len(structure.overlap_map))
    
    def test_multidomain(self):
        structure=random_avoid(20, CubicLattice(), chain_list=[10,10])
        self.assertEqual(0,len(structure.overlap_map))
        self.assertEqual(2,structure.num_chains)
        
if __name__ == "__main__":
    unittest.main()