"""
Computes the volume of water in the tank described in Exercise 5.
"""

# Import the needed modules
from pylab import *

# Prompt the user for the height of the water in the tank.
h = float(input("Enter the water height from bottom of tank in meters: "))

# Set the dimensions of the tank
r_1 = 8.0/2  # radius of the small bottom portion of the tank
r_2 = 12.0/2 # radius of the large top portion of the tank
h_1 = 6.0    # height of smaller bottom portion of the tank
h_max = 10.0 # height of the top of the tank

# Compute the volume of water and print the result
if (h < 0.0):
	print("Sorry, the height of the tank can't be less than 0.")
elif (h <= h_1):
	vol = pi*r_1**2*h
	print("The volume of the water in the tank is %g m^3" % vol)
elif (h <= h_max):
	vol = pi*r_1**2*h_1 + pi*r_2**2*(h - h_1)
	print("The volume of the water in the tank is %g m^3" % vol)
else:
	print("Sorry, the max height of the tank is %g m." % h_max)
