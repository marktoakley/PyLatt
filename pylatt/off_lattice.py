'''
@author:  Mark Oakley
'''

import numpy as np
import urllib2

def read_from_pdb(PDB_ID):
    '''Generate an OffLatticeStructure by downloading its properties
    from the Protein Data Bank (http://www.rcsb.org/).
    
    Parameters
    ----------
    PDB_ID: A 4-character PDB ID (e.g. 4ins for insulin)
    '''
    url = "http://www.rcsb.org/pdb/files/"+PDB_ID+".pdb"
    print url
    f = urllib2.urlopen(url)
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
    termini = [0]
    for i in range(0, len(chains)-1):
        if chains[i] != chains[i+1]:
            termini.append(i)
            termini.append(i+1)
    termini.append(len(chains)-1)
    coords = np.array(coords)
    return OffLatticeStructure(coords, termini)
    
class OffLatticeStructure:
    def __init__(self, coords, termini):
        self.coords = coords
        self.natoms = len(coords)
        self.termini = termini
                
                
                
                