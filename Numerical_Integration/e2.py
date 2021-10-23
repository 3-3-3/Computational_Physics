from scipy.integrate import quad
from scipy.optimize import fsolve
import scipy.constants as sc
import numpy as np
import matplotlib.pyplot as plt

l = 0.5 #length of pendulum

f = lambda x, x_0 : 1/np.sqrt(np.sin(x_0/2)**2 - np.sin(x/2)**2)

def error(x_0, l, target=0):
    t = 2*np.sqrt(l/sc.g)*quad(f,0,x_0,args=(x_0,))[0]
    t_aprox = 2*sc.pi*np.sqrt(l/sc.g)
    return np.abs(t-t_aprox)/t*100-target

if __name__ == '__main__':
    n = 100
    x_array = np.linspace(0, np.pi, n)
    t_aprox_array = [2*sc.pi*np.sqrt(l/sc.g) for i in range(n)]
    t_array = 2*np.sqrt(l/sc.g)*np.array([quad(f, 0, i, args=(i,))[0] for i in x_array])
    e_array = (np.abs((t_aprox_array-t_array))/t_array)*100

    fig, (ax1, ax2) = plt.subplots(2,1)
    ax1.set_title('Aproximate Period and Actual Period For Simple Plane Pendulum')
    ax1.set_ylabel('Period')
    ax1.plot(x_array, t_array)
    ax1.plot(x_array,t_aprox_array)

    print(f'Error of one occurs at: {fsolve(error, 0.4, args=(0.5,1))}')

    ax2.plot(x_array, e_array)
    ax2.set_ylabel('Percent Error')
    ax2.set_xlabel('Amplitude of Oscilation')
    plt.show()
