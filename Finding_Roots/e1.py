from scipy.optimize import fsolve
import scipy.constants as sc
import matplotlib.pyplot as plt
import numpy as np

d_planck = lambda x : x*np.exp(x)/(np.exp(x)-1)-5

if  __name__ == '__main__':
    x_max = fsolve(d_planck, 5)
    print(f'Better solution: {x_max}')
    print(f'Calculated Wien constant: {sc.h*sc.c/(sc.k*x_max)}')
    print(f'Scipy.constants Wien constant: {sc.Wien}')
    x = np.linspace(-2,6,100)
    y = d_planck(x)

    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('d_planck')

    plt.plot(x, np.zeros(100))
    plt.show()
