import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py

if __name__ == '__main__':
    file = h5py.File('test_ssx_particle_trajectory.h5', 'r')
    #file['r'] is data of shape (steps, 3) where each row is a vector position (x,y,z)
    #goal is to plot (xarray,yarray,zarray)
    ax = plt.gcf().add_subplot(111, projection='3d')
    x = file['r'][:,0]
    y = file['r'][:,1]
    z = file['r'][:,2]
    file.close()
    ax.plot(x,y,z)
    plt.savefig('plot.png')
    plt.show()
