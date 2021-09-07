"""
exercise06.py Program to sum the series given in Exercise 6.
"""

# Prompt the user for the value of n
n = int(input('Enter the value of n: '))

# Sum the series with a for statement
sum = 0  # initialize the value of the sum
for k in range(1,n+1):
	sum = sum + (-1.0)**k * k / 2.0**k
	
# Display the result
print("\nThe sum of (-1.0)**k * k / 2.0**k from k = 1 to k = %d = %g" % (n,sum))
	