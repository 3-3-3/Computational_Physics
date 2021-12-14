import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

def in_circle(x, y, r=1):
    return np.sqrt(x**2 + y**2) <= r

def pi_estimate(n):
    points = rand(n,2)
    in_circ = len([True for x, y in points if in_circle(x, y)])
    out = len(points)
    return 4*in_circ/out

if __name__ == '__main__':
    estimates = np.array([pi_estimate(n) for n in range(10, 1*10**5)])
    plt.semilogx(np.arange(len(estimates)), np.pi)
    print('Plotted Pi')
    plt.semilogx(np.arange(len(estimates)), estimates)
    plt.ylabel(r'$\pi_{est}$')
    plt.xlabel('Number of Points')
    plt.savefig('pi_est.jpg')
    plt.show()
