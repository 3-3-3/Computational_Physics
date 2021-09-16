import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
from scipy.optimize import curve_fit
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
a = 2*sc.pi/365
f = [lambda f_0 : 1, lambda f_1 : f_1, lambda f_3 : np.sin(a*f_1)]


def ls(x, y, f_space):
    #x: x data to fit
    #y: y data to fit
    #f_space: function space. List of python functions representing
    #mathematical functions
    A = np.array([[i(x) for i in f_space] for x_n in x])
    AT = np.transpose(A)
    #Let B=[b_0, b_1, b_2]. Then, return the solution to [AT.A].B = [AT].y
    print(f'A transpose dot A: {np.dot(AT, A)}')
    print(f'A transpose dot y: {np.dot(AT, y)}')
    return np.linalg.solve(np.dot(AT, A), np.dot(AT, y))




if __name__ == '__main__':
    #dummy data
    x = np.array([sc.pi/2*i for i in range(10)])
    y = np.array([5-2*i+4*np.sin(1.2*i)+0.1*random.randrange(1,10) for i in x])


    #x_b = np.linspace(0,4*sc.pi,100)
    b = ls_a_x_sinx(t_array,ppm_mauna,a)
    print(f'b (solution to AT.A.[b] = AT.y): {b}')
    y_b = np.array([b[0] + b[1]*i + b[2]*np.sin(a*i) for i in t_array])



    plt.title(f'$CO_2$ Levels In Mauna Loa (Average increase of {np.round(b[1]*365, decimals=2)} ppm per year)')
    plt.ylabel('$CO_2$ Levels (Parts Per Million)')
    plt.xlabel('Days Since 1981')
    #plt.scatter(x,y)
    text_kwargs = dict(ha='center', va='center', fontsize=28, color='C1')
    plt.plot(t_array, y_b)
    plt.scatter(t_array, ppm_mauna, c=['orange'], marker='.')
    #note that b[1] is the average increase per day. Multiply by 365 to obtain average increase per day.

    #plt.plot(t_array, y_2)
    plt.savefig('Mauna_CO2.png')
    plt.show()
