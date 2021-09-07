"""
if_test.py
Program to illustrate how if statements work. It uses input() to read strings from
the keyboard then tests the input string with an if statement to determine the output.
"""

colour = input("What is your favorite color? ")
warm_colours = ["red","yellow","orange"]
cool_colours = ["blue", "green", "purple"]
if (colour == "black"):
	print("Your favorite color is Black.")
	print(" That is an unusual favorite color.")	
elif (colour == "white"):
	print("Is white really a color?")
elif (colour in warm_colours):
	print("You like warm colors.")
elif (colour in cool_colours):
	print("You like cool colors.")
else:
	print("Sorry, I don't know the color '%s'." % colour)	