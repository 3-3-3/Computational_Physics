import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

def func(x):
    return np.sin(x)/x

x = np.linspace(-5*sc.pi, 5*sc.pi,100)
y = [func(i) for i in x]

plt.plot(x,y)
plt.show()
