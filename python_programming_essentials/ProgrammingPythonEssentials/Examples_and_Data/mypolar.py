"""
This is a module contains functions to convert to and from cartesian to 
cylindrical polar coordinates.

"""

# The functions below need these sqrt and trig functions, so lets import them.
from pylab import sqrt,arctan,cos,sin 

def xy2rth(x, y):
	"""Converts x and y coordinates to polar coordinates, r and theta."""
	r = sqrt(x**2 + y**2)
	theta = arctan(y/x)
	return [r, theta]
	
def rth2xy(r,theta):
	"""Converts the polar coordinates r and theta to x and y."""
	x = r*cos(theta)
	y = r*sin(theta)
	return [x, y]