"""
File: quadratic_solver.py
Name: Wilson Wang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program should implement a console program
	that asks 3 inputs (a, b, and c)
	from users to compute the roots of equation
	ax^2 + bx + c = 0
	Output format should match with 3 conditions, which have different number of root .
	"""
	print('stanCode Quadratic Solver')
	a = int(input('Enter a:'))
	b = int(input('Enter b:'))
	c = int(input('Enter c:'))

	if b*b - 4*a*c > 0:
		# This equation should compute the roots of ax^2 + bx + c = 0
		d = math.sqrt(b ** 2 - 4 * a * c)
		# answer1 and answer3 are for the condition of 2 roots (d>0)
		answer1 = (-b + d) / (2 * a)
		answer3 = (-b - d) / (2 * a)
		# this code should show two roots when d > 0
		print('two roots: '+str(answer1)+' , '+str(answer3))
	elif b*b - 4*a*c == 0:
		# answer2 is for the condition of 1 root(d=0)
		answer2 = -b / (2 * a)
		# this code should show one roots when d = 0
		print('one roots: '+str(answer2))
	else:
		# this condition shoe when d < 0
		print('no real roots')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
