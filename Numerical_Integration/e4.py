from scipy.integrate import dblquad
import scipy.constants as sc
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    m, error = dblquad(lambda y, x : 1.3*np.exp(-x**2), 0, 3, lambda x : 0, lambda x : 2/3*x) #total mass of plate
    cm_x = 1/m*dblquad(lambda y, x : 1.3*x*np.exp(-x**2), 0, 3, lambda x : 0, lambda x : 2/3*x)[0]
    cm_y = 1/m*dblquad(lambda y, x : 1.3*y*np.exp(-x**2), 0, 3, lambda x : 0, lambda x : 2/3*x)[0]

    print(f'Center of mass (x,y) of plate is: ({cm_x}, {cm_y})')
