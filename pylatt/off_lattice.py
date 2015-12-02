'''
@author:  Mark Oakley
'''

import numpy as np
import urllib

from pylatt.lattice_structure import LatticeStructure
import pylatt.termini as termini

def read_from_pdb(PDB_ID):
    '''Generate an OffLatticeStructure by downloading its properties
    from the Protein Data Bank (http://www.rcsb.org/).
    
    Parameters
    ----------
    PDB_ID: A 4-character PDB ID (e.g. 4ins for insulin)
    '''
    url = "http://www.rcsb.org/pdb/files/"+PDB_ID+".pdb"
    print (url)
    f = urllib.urlopen(url)
    return read_from_iterable(f)

def read_from_file(file_name):
    '''Generate an OffLatticeStructure by reading its properties from a PDB file.
    
    Parameters
    ----------
    file_name: a pdb file'''
    with open(file_name,'r') as f:
        return read_from_iterable(f)
    
def read_from_iterable(pdb):
    '''Generate an OffLatticeStructure by reading its properties from an iterable object.
    
    Parameters
    ----------
    pdb: an iterable object containing a pdb file
    '''
    coords=[]
    chains=[]
    for line in pdb:
        if line[0:6]=="ATOM  ":
            atom_no = int(line[6:11])
            atom_name = line[12:16]
            alt_loc = line[16]
            res_name = line[17:20]
            chain_id = line[21]
            res_no = int(line[22:26])
            icode = line[26]
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            if line[13:15]=="CA":
                coords.append([x,y,z])
                chains.append(chain_id)
    coords = np.array(coords)
    return OffLatticeStructure(coords, chainID = chains)

def to_lattice(structure, lattice):
    '''Fit an OffLatticeStrucure to a lattice.
    
    This only performs a quick fit and is intended to generate the
    starting point for the pdb2lattice optimiser.'''
    unit_coords = structure.coords / lattice.angstrom
    unit_coords -= unit_coords[0]
    lattice_structure = LatticeStructure(lattice,
                                         np.zeros((structure.natoms,3),dtype=int),
                                         chainID = structure.chainID)
    for i in range(1,structure.natoms):
        next_move = lattice_structure.free_moves(i-1)
        my_move = closest_move(next_move,unit_coords[i])
        lattice_structure.coords[i] = my_move
    lattice_structure.make_contact_map()
    lattice_structure.off_latt_coords = unit_coords
    return lattice_structure
    
def closest_move(move_list, target):
    '''Return the lattice point from move_list closest to the target
    off-lattice point.'''
    min_distance = 1000000.
    for move in move_list:
        distance=0
        vector = move - target
        for j in range(0, 3):
            distance += vector[j]**2
        if distance < min_distance:
            best = move
            min_distance = distance
    return best
                
    
class OffLatticeStructure:
    def __init__(self, coords, chainID):
        self.coords = coords
        self.natoms = len(coords)
        self.chainID = chainID
        self.termini = termini.find(chainID)
                
                
                
                
