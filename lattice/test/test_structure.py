'''
@author: Mark Oakley
'''
import unittest
from lattice.moves import CubicLattice
from lattice.lattice_structure import Lattice_Structure,\
    Lattice_Structure_Factory

class StructureTest(unittest.TestCase):

    def test_contact_map(self):
        lattice=CubicLattice()
        coords=[[0,0,0],
                [0,0,1],
                [0,1,1],
                [0,1,0]]
        structure=Lattice_Structure(lattice,coords)
        structure.make_contact_map()
        self.assertEqual(1,len(structure.map))
        self.assertEqual(0,len(structure.overlaps))
        
        def test_overlap(self):
            lattice=CubicLattice()
            coords=[[0,0,0],
                    [0,0,1],
                    [0,0,0]]
            structure=Lattice_Structure(lattice,coords)
            structure.make_contact_map()
            self.assertEqual(0,len(structure.overlaps))

class FactoryTest(unittest.TestCase):
    
    def test_random(self):
        #No tests on output. Just run to ensure no exceptions
        factory=Lattice_Structure_Factory("HHHPPPHHP",CubicLattice())
        structure=factory.random()
        
    def test_avoid(self):
        factory=Lattice_Structure_Factory(("H"*100),CubicLattice())
        structure=factory.random_avoid()
        self.assertEqual(0,len(structure.overlaps))
        
        
if __name__ == "__main__":
    unittest.main()