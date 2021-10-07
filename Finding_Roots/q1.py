import scipy.constants as sc
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

a = 0.529e-10
v_0 = 1*1.60218e-16 #convert from kev to Joules
k_exp2 = 2*sc.electron_mass*a**2*(v_0/sc.hbar**2)
print(k_exp2)

e_1 = lambda s : s*(1/np.tan(s)) + np.sqrt(k_exp2 - s**2)

#Guess 1: 1.76
#Guess 2: 5.43
#Guess 3: 4.7
s_1, s_2, s_3 = fsolve(e_1, [2.8,5.5,8.1])
print((s_1, s_2, s_3))
v_1 = -v_0*(s_1**2/k_exp2-1)
v_2 = -v_0*(s_2**2/k_exp2-1)
v_3 = -v_0*(s_3**2/k_exp2-1)
print(f'Allowed energy state 1: {v_1/1.60218e-16}, Allowed energy state 2: {v_2/1.60218e-16}, Allowed energy state 3: {v_3/1.60218e-16}')

x = np.linspace(0,10,200)
y = e_1(x)
plt.plot(x,y)
plt.plot(x, np.zeros(200))
plt.show()
