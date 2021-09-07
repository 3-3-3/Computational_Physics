"""
This is a module contains functions to convert to and from cartesian to
cylindrical polar coordinates.

"""

# The functions below need these sqrt and trig functions, so lets import them.
from pylab import sqrt,arctan,cos,sin
import scipy.constants as sc


def xy2rth(x,y):
    r = sqrt(x**2+y**2)

    if x == 0:
        if y > 0:
            theta = sc.pi/2
        elif y < 0:
            theta = 3*sc.pi/2
        else:
            theta = 0
    elif x > 0:
        theta = arctan(y/x)
    else:
        theta = arctan(y/x) + sc.pi
    return [r, theta]

def rth2xy(r,theta):
	"""Converts the polar coordinates r and theta to x and y."""
	x = r*cos(theta)
	y = r*sin(theta)
	return [x, y]
