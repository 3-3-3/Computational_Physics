from scipy.integrate import quad
import scipy.constants as sc
import numpy as np
import matplotlib.pyplot as plt

f = lambda t : np.exp(-t**2)

if __name__ == '__main__':
    x = np.linspace(-3,3,100)
    y = 2/np.sqrt(sc.pi)*np.array([quad(f, i, np.inf)[0] for i in x])
    plt.plot(x,y)
    plt.show()
