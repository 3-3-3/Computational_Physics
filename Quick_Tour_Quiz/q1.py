import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

ppm_mauna = np.load("Mauna_CO2.npy")
s = ppm_mauna.size

#Let t=0 be January 1st. Then, the last date that data was collected is s*14, where s is the number
#Of measurements taken and 14 is the days between measurements.
t_array = np.linspace(0,s*14,s)

#Use a least-squares line to fit the data
#Let b = [b_0, b1], where b_0 is the y-intercept and b1 is the slope
#Let X = [[1, t_array[0]]...[1, t_array[len(t_array)]]]
#Let y = ppm_mauna. Then, the least squares line is the best fit to Xb = y

X = np.array([[1, t_array[i]] for i in range(len(t_array))])

#solve for b.

XXT = np.dot(np.transpose(X),X)
XTy = np.dot(np.transpose(X), ppm_mauna)

#b is the the inverse of XXT times XTy
b = np.linalg.solve(XXT, XTy)
print(b)

#Create the best fit
y = np.array([b[0] + b[1]*t_array[i] for i in range(len(t_array))])

#Can we get a better fit? There is clearly a cyclical nature to the readings in addition to the upward trend.
#Fit the equation y=b_0f_0(x) + b_1f_1(x) + b_2f_2(x)
#Such that f_0(x) = 1, f_2(x) = 2, and f_3(x) = sin(ax)
#With a = 2pi/365

a = (2*sc.pi)/185

X_2 = np.array([[1, i, np.sin(a*i), np.cos(a*i)] for i in t_array])
X_2X_2T = np.dot(np.transpose(X_2), X_2)
X_2Ty = np.dot(np.transpose(X_2), y)

b_2 = np.linalg.solve(X_2X_2T, X_2Ty)

y_2 = np.array([b_2[0] + b_2[1]*i + b_2[2]*i for i in t_array])
print('b_2')
print(b_2)

plt.title('CO2 Levels In Mauna Loa')
plt.ylabel('CO2 Levels (Parts Per Million)')
plt.xlabel('Days Since 1981')
plt.scatter(t_array, ppm_mauna)
plt.plot(t_array, y)
plt.plot(t_array, y_2)
plt.show()
