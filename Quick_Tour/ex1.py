import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

r = np.linspace(0.1e-9, 0.5e-9, 100)
f = sc.e**2/(4 * sc.pi * sc.epsilon_0 * r**2)

plt.title('Force Between Electrons At Distances 0.1 nm to 0.5 nm')
plt.xlabel('Distance')
plt.ylabel('Force')

plt.plot(r,f)
plt.show()
