'''
Created on 22 Sep 2015

@author: mark
'''
import matplotlib.pyplot as plt
import numpy as np

def plot_2d(structure, potential):
    '''Display a 2D representation of a structure.''' 
    x = structure.coords[:,0]
    y = structure.coords[:,1]
    #colours = np.array(potential.isequence,dtype=float)
    colours = potential.isequence
    plt.scatter(x,y,s=100,c=colours)
    plt.plot(x,y)
    plt.show()
