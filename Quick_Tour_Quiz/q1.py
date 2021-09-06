import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
import random

ppm_mauna = np.load("Mauna_CO2.npy")
s = ppm_mauna.size

#Let t=0 be January 1st. Then, the last date that data was collected is s*14, where s is the number
#Of measurements taken and 14 is the days between measurements.
t_array = np.linspace(0,s*14,s)

#Use a least-squares line to fit the data
#Let b = [b_0, b1], where b_0 is the y-intercept and b1 is the slope
#Let X = [[1, t_array[0]]...[1, t_array[len(t_array)]]]
#Let y = ppm_mauna. Then, the least squares line is the best fit to Xb = y

def ls_a_x_sinx(x, y, a=1):
    #Can we get a better fit? There is clearly a cyclical nature to the readings in addition to the upward trend.
    #So consider the function space spanned by {1,x,sin(ax)} instead of {1,x}
    #Fit the equation y=b_0f_0(x) + b_1f_1(x) + b_2f_2(x)
    #Such that f_0(x) = 1, f_2(x) = 2, and f_3(x) = sin(ax)
    #With a = 2pi/365
    #x and y are numpy arrays.
    #Define the matrix A where each row is [1, x_n, sin(a*x_n)] for all x_n in x
    #a is the period of the sin function which is to be fitted
    A = np.array([[1, x_n, np.sin(a*x_n)] for x_n in x])
    AT = np.transpose(A)
    #Let B=[b_0, b_1, b_2]. Then, return the solution to [AT.A].B = [AT].y
    print(f'A transpose dot A: {np.dot(AT, A)}')
    print(f'A transpose dot y: {np.dot(AT, y)}')
    return np.linalg.solve(np.dot(AT, A), np.dot(AT, y))




#dummy data
x = np.array([sc.pi/2*i for i in range(10)])
y = np.array([5-2*i+4*np.sin(1.2*i)+0.1*random.randrange(1,10) for i in x])


#x_b = np.linspace(0,4*sc.pi,100)
a = 2*sc.pi/365.25
b = ls_a_x_sinx(t_array,ppm_mauna,a)
print(f'b (solution to AT.A.[b] = AT.y): {b}')
y_b = np.array([b[0] + b[1]*i + b[2]*np.sin(a*i) for i in t_array])

plt.title(f'CO2 Levels In Mauna Loa (Average increase of {np.round(b[1]*365, decimals=2)} ppm per year)')
plt.ylabel('CO2 Levels (Parts Per Million)')
plt.xlabel('Days Since 1981')
#plt.scatter(x,y)
text_kwargs = dict(ha='center', va='center', fontsize=28, color='C1')
plt.plot(t_array, y_b)
plt.scatter(t_array, ppm_mauna, c=['orange'], marker='.')
#note that b[1] is the average increase per day. Multiply by 365 to obtain average increase per day.

#plt.plot(t_array, y_2)
plt.savefig('Mauna_CO2.png')
plt.show()
