"""
for_test.py
Program to illustrate how for statements work. The program prints the x and y 
positions of a projectile launched at a 45 deg angle.
"""

vx = 50.0
vy = 50.0
g = 9.8

print(' x \t y ')
for t in range(1,11):  # range(1,11) creates the list [1,2,3,4,5,6,7,8,9,10]
	x = vx*t
	y = vy*t - 0.5*g*t**2
	print('%g \t %g' % (x,y))
print('\n')

# Here is another way to generate an idential output using numpy
# arrays
from pylab import *

t = linspace(1,10,10) # creates a numpy array
x = vx*t
y = vy*t - 0.5*g*t**2

print(' x \t y ')
for idx in range(0,10):
	print('%g \t %g' % (x[idx], y[idx]))
