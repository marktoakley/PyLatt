'''
Created on 22 Sep 2015

@author: mark
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np    
    
def plot_fit(structure, fig = None):
    '''Compare a fitted lattice structure to its parent off-lattice structure.
    This returns a matplotlib figure object. The optional argument, fig,
    adds the plot as a subplot to an existing matplotlib figure.
    Parameters:
    -----------
    structure: A LatticeStructure generated by off_lattice.to_lattice()
    fig - A matplotlib figure object
    '''
    if (fig is None):
            fig = plt.figure(figsize=(5,5))
    coords = np.concatenate((structure.coords, structure.off_latt_coords), axis=0)
    termini = structure.termini+[x+len(structure.coords) for x in structure.termini]
    isequence = [0] * len(coords)
    ax = fig.add_subplot(111, projection='3d')
    ax.clear()
    _make_plot(coords, termini, isequence, ax)
    return fig

def plot_2d(structure, fig=None):
    '''Draw a 2D representation of a structure.
    This returns a matplotlib figure object. The optional argument, fig,
    adds the plot as a subplot to an existing matplotlib figure.
    Parameters:
    -----------
    structure: A LatticeStructure
    fig - A matplotlib figure object'''
    if (fig is None):
        fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.clear()
    #fig = plt.figure(figsize=(5,5))
    #plt.title("Energy = "+str(structure.energy))
    limits = get_range(structure.coords)
    ax.set_xlim(limits[0][0], limits[0][1])
    ax.set_ylim(limits[1][0], limits[1][1])
    
    for i in range(0, len(structure.termini)//2):
        start = structure.termini[2*i]
        end = structure.termini[2*i+1]+1
        x = structure.coords[start:end,0]
        y = structure.coords[start:end,1]
    if structure.model is None:
        colours = [0] *(end-start)
    else:
        colours = structure.model.isequence[start:end]
    ax.scatter(x,y,s=100,c=colours)
    ax.plot(x,y)
    
    return fig

def plot_3d(structure, fig=None):
    '''Draw a 3D representation of a structure.
    This returns a matplotlib figure object. The optional argument, fig,
    adds the plot as a subplot to an existing matplotlib figure.
    Parameters:
    -----------
    structure: A LatticeStructure
    fig - A matplotlib figure object'''
    if (fig is None):
        fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, projection='3d')
    ax.clear()
    coords=structure.coords
    termini=structure.termini
    if structure.model is None:
        isequence = [0]*len(coords)
    else:
        isequence = structure.model.isequence
    
    ax = _make_plot(coords, termini, isequence, ax)
    return fig

def plot_contact_map(structure, fig=None):
    '''Draw a 2D representation of a structure's contact map.
    This returns a matplotlib figure object. The optional argument, fig,
    adds the plot as a subplot to an existing matplotlib figure.
    Parameters:
    -----------
    structure: A LatticeStructure
    fig - A matplotlib figure object'''
    if (fig is None):
        fig = plt.figure(figsize=(5,5))
    x = []
    y = []
    for pair in structure.contact_map:
        x.append(pair[0]+1)
        y.append(pair[1]+1)
        y.append(pair[0]+1)
        x.append(pair[1]+1)
    ax = fig.add_subplot(111)
    ax.clear()
    ax.set_xlim(1,structure.natoms)
    ax.set_ylim(1,structure.natoms)
    ax.scatter(x,y,s=100)
    return fig

def _make_plot(coords, termini, isequence, ax):
    limits = get_range(coords)
    ax.set_xlim3d(limits[0][0], limits[0][1])
    ax.set_ylim3d(limits[1][0], limits[1][1])
    ax.set_zlim3d(limits[2][0], limits[2][1])
    ax.set_axis_off()
    for i in range(0, len(termini)//2):
        start = termini[2*i]
        end = termini[2*i+1]+1
        xs = coords[start:end,0]
        ys = coords[start:end,1]
        zs = coords[start:end,2]    
        colours = isequence[start:end]
        ax.scatter(xs,ys,zs,s=10,c=colours)
        ax.plot(xs,ys,zs)
    #plt.title("Energy = "+str(structure.energy))
    #plt.show()
    return ax

def get_range(coords):
    xs = coords[:,0]
    ys = coords[:,1]
    zs = coords[:,2]
    plot_range = max ((max(xs) - min(xs)),
                      (max(ys) - min(ys)),
                      (max(zs) - min(zs)))
    xmin = float((max(xs)+min(xs)-plot_range))/2 -.5
    xmax = xmin+plot_range+1.
    ymin = float((max(ys)+min(ys)-plot_range))/2 -.5
    ymax = ymin+plot_range+1.
    zmin = float((max(zs)+min(zs)-plot_range))/2 -.5
    zmax = zmin+plot_range+1.
    
    return[[xmin, xmax], [ymin, ymax], [zmin, zmax]]
