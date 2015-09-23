'''
Created on 22 Sep 2015

@author: mark
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_2d(structure, model):
    '''Display a 2D representation of a structure.''' 
    x = structure.coords[:,0]
    y = structure.coords[:,1]
    plot_range = max ((max(x) - min(x)),
                      (max(y) - min(y)))
    xmin = float((max(x)+min(x)-plot_range))/2
    ymin = float((max(y)+min(y)-plot_range))/2
    colours = model.isequence
    plt.figure(figsize=(5,5))
    plt.scatter(x,y,s=100,c=colours)
    plt.plot(x,y)
    plt.title("Energy = "+str(structure.energy))
    plt.xlim(xmin-.5, xmin+plot_range+.5)
    plt.ylim(ymin-.5, ymin+plot_range+.5)
    plt.show()
    
def plot_3d(structure, model):
    '''Display a 3D representation of a structure.'''
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
    colours = model.isequence
    ax.scatter(xs,ys,zs,s=100,c=colours)
    ax.plot(xs,ys,zs)
    plt.title("Energy = "+str(structure.energy))
    plt.show()
    
