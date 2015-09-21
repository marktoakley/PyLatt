'''
@author: Mark Oakley
'''
import unittest
from lattice.moves import CubicLattice
from lattice.lattice_structure import LatticeStructure,LatticeStructureFactory

class StructureTest(unittest.TestCase):

    def test_contact_map(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,1,1],
                [0,1,0]]
        structure=LatticeStructure(lattice,coords)
        structure.make_contact_map()
        self.assertEqual(1,len(structure.map))
        self.assertEqual(0,len(structure.overlaps))
        
        def test_overlap(self):
            lattice=CubicLattice()
            coords=[[0,0,0],
                    [0,0,1],
                    [0,0,0]]
            structure=LatticeStructure(lattice,coords)
            structure.make_contact_map()
            self.assertEqual(0,len(structure.overlaps))

class FactoryTest(unittest.TestCase):
    
    def test_random(self):
        factory=LatticeStructureFactory("HHHPPPHHHP",CubicLattice())
        structure=factory.random()
        self.assertEqual(10,structure.natoms)
        
    def test_avoid(self):
        factory=LatticeStructureFactory(("H"*100),CubicLattice())
        structure=factory.random_avoid()
        self.assertEqual(0,len(structure.overlaps))
        
        
if __name__ == "__main__":
    unittest.main()