import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

p = np.array([1.769,3.552,7.155,16.689])
a = np.array([421.6e6, 670.9e6,1070.4e6,1882.7e6])

l_p = np.log10(p)
l_a = np.log10(a)

x = np.linspace(0,np.max(l_p),100)
y = (3/2)*x
plt.plot(x,y)
plt.plot(l_p, l_a)
plt.show()
