'''
Created on 22 Sep 2015

@author: mark
'''
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_2d(structure, potential):
    '''Display a 2D representation of a structure.''' 
    x = structure.coords[:,0]
    y = structure.coords[:,1]
    #colours = np.array(potential.isequence,dtype=float)
    colours = potential.isequence
    plt.scatter(x,y,s=100,c=colours)
    plt.plot(x,y)
    plt.show()
    
def plot_3d(structure, potential):
    '''Display a 3D representation of a structure.'''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = structure.coords[:,0]
    ys = structure.coords[:,1]
    zs = structure.coords[:,2]
    colours = potential.isequence
    ax.scatter(xs,ys,zs,s=100,c=colours)
    ax.plot(xs,ys,zs)
    plt.show()
    
