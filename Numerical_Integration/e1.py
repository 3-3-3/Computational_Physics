from scipy.integrate import quad
import scipy.constants as sc
import numpy as np

l = 0.5 #length of pendulum

f = lambda x, x_0 : 1/np.sqrt(np.sin(x_0/2)**2 - np.sin(x/2)**2)

integral, error = quad(f, 0, sc.pi/4, args=(sc.pi/4,))

t_aprox = 2*sc.pi*np.sqrt(l/sc.g)
t = 2*np.sqrt(l/sc.g)*integral

print(f'Approximate period: {t_aprox}, elliptic period: {t}')
