def find(chainID):
    termini = [0]
    natoms = len(chainID)
    for i in range(1, natoms-1):
        if (chainID[i] != chainID[i+1]):
            termini.append(i)
            termini.append(i+1)
    termini.append(natoms-1)
    return termini