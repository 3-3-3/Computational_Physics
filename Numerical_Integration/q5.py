import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import matplotlib.pyplot as plt

def gauss(x, mean=0, sigma=1):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-1*((x - mean)**2/(2*sigma**2)))



def probability_in(a,b,mean=0, sigma=1):
    return quad(gauss, a, b, args=(mean,sigma,))[0]

if __name__ == '__main__':
    #The probability that v is in [-sigma, sigma] is:
    print(f'The probability that v is in [-sigma, sigma] is:{probability_in(-1,1,sigma=1)}')
    x = np.linspace(0,3)
    y = np.array([probability_in(-i, i) for i in x])
    plt.plot(x,y)
    plt.show()
