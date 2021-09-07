"""
while_test.py
Program to illustrate how a while statement works.
"""

passwd = ''     # set the initial value of the password to an incorrect result

while (passwd != 'swordfish'):
	passwd = input('What is the secret password: ')
	
print('\nYeah! You know the secret password.')