import numpy as np
import matplotlib.pyplot as plt

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

plt.scatter(t_array, ppm_mauna)
plt.plot(t_array, y)
plt.show()
