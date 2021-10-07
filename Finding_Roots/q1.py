import scipy.constants as sc
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

a = 0.529e-10
v_0 = 1*1.60218e-16 #convert from kev to Joules
k_exp2 = 2*sc.electron_mass*a**2*(v_0/sc.hbar**2)
print(k_exp2)

e_1 = lambda s : s*(np.tan(s)) + np.sqrt(k_exp2 - s**2)

#Guess 1: 1.76
#Guess 2: 5.43
#Guess 3: 4.7
s_1, s_2 = fsolve(e_1, [1.76,5.43])
print((s_1, s_2))
v_1 = (1-s_1**2/k_exp2)
v_2 = (1-s_2**2/k_exp2)
print(f'Allowed energy state 1: {v_1}, Allowed energy state 2: {v_2}')

x = np.linspace(0,np.sqrt(k_exp2),200)
y = e_1(x)
plt.plot(x,y)
plt.plot(x, np.zeros(200))
plt.show()
