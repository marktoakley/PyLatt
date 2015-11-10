'''
Created on 22 Sep 2015

@author: mark
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_2d(structure, model = None):
    '''Display a 2D representation of a structure.
    
    Parameters
    ----------
    structure: A LatticeStructure
    model(optional): a Potential object (used to colour provide coloured residue types). ''' 
    x = structure.coords[:,0]
    y = structure.coords[:,1]
    plot_range = max ((max(x) - min(x)),
                          (max(y) - min(y)))
    xmin = float((max(x)+min(x)-plot_range))/2
    ymin = float((max(y)+min(y)-plot_range))/2
    plt.figure(figsize=(5,5))
    #plt.title("Energy = "+str(structure.energy))
    plt.xlim(xmin-.5, xmin+plot_range+.5)
    plt.ylim(ymin-.5, ymin+plot_range+.5)
    for i in range(0, len(structure.termini)//2):
        start = structure.termini[2*i]
        end = structure.termini[2*i+1]+1
        x = structure.coords[start:end,0]
        y = structure.coords[start:end,1]
        if model is None:
            colours = [0] *(end-start)
        else:
            colours = model.isequence[start:end]
        plt.scatter(x,y,s=100,c=colours)
        plt.plot(x,y)

    #plt.show()
    return plt
    
def plot_3d(structure, model = None):
    '''Display a 3D representation of a structure.
    
    Parameters
    ----------
    structure: A LatticeStructure
    model(optional): a Potential object (used to colour provide coloured residue types).''' 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = structure.coords[:,0]
    ys = structure.coords[:,1]
    zs = structure.coords[:,2]
    plot_range = max ((max(xs) - min(xs)),
                      (max(ys) - min(ys)),
                      (max(zs) - min(zs)))
    xmin = float((max(xs)+min(xs)-plot_range))/2
    ymin = float((max(ys)+min(ys)-plot_range))/2
    zmin = float((max(zs)+min(zs)-plot_range))/2
    ax.set_xlim3d((xmin-.5), (xmin+plot_range+.5))
    ax.set_ylim3d((ymin-.5), (ymin+plot_range+.5))
    ax.set_zlim3d((zmin-.5), (zmin+plot_range+.5))
    ax.set_axis_off()
    for i in range(0, len(structure.termini)//2):
        start = structure.termini[2*i]
        end = structure.termini[2*i+1]+1
        xs = structure.coords[start:end,0]
        ys = structure.coords[start:end,1]
        zs = structure.coords[start:end,2]    
        if model is None:
            colours = [0] *(end-start)
        else:
            colours = model.isequence[start:end]
        ax.scatter(xs,ys,zs,s=100,c=colours)
        ax.plot(xs,ys,zs)
    #plt.title("Energy = "+str(structure.energy))
    #plt.show()
    return plt
    
