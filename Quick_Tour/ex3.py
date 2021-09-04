import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

p = (24*60**2)*np.array([1.769,3.552,7.155,16.689])
a = np.array([421.6e6, 670.9e6,1070.4e6,1882.7e6])

l_p = np.log10(p) #y-axis
l_a = np.log10(a) #x-axis

print('Slopes dlog(p)/dlog(a)')
print([(l_p[i]-l_p[i-1])/(l_a[i]-l_a[i-1]) for i in range(1,len(l_p))])
x = np.linspace(0,np.max(l_a),100)

b = l_p-(3/2)*l_a
print(b)
y_int = np.mean(b)
print(y_int)
y = 3/2*x + y_int

print(f'The mass of Jupiter is {1/sc.G*((2*sc.pi)/10**y_int)**2}')
plt.plot(x,y)
plt.plot(l_a, l_p)
plt.show()
