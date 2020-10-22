"""
File: rocket.py
name: Wilson
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 3


def main():
	"""
	This program should implement a console program
	that draws ASCII art - a rocket.
	The size of rocket is determined by a constant
	defined as SIZE at top of the file.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function draws an equilateral triangle at the center position and draws two opposite right triangles
	at right and left side
	"""
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end='')
		for k in range(i+1):
			print('/',end="")
		for h in range(i+1):
			print('\\',end='')
		print('')


def belt():
	"""
	This function draws a string line that both left and right side is '+' and the rest parts is '=' determine by SIZE
	"""
	print('+',end='')
	for i in range(SIZE*2):
		print('=',end='')
	print('+', end='')
	print('')


def upper():
	"""
	This function draws by roles:
	1.draw'/\' at the center position, the quantity should determine by SIZE
	2.draw'|' at both left and right side
	3.the rest blank should be filled by '.'
	"""
	for i in range(SIZE):
		print('|',end='')
		for j in range(SIZE-(i+1)):
			print('.',end='')
		for k in range(i+1):
			print('/',end='\\')
		for j in range(SIZE-(i+1)):
			print('.',end='')
		print('|',end='')
		print('')


def lower():
	"""
	This function draws by roles:
	1.draw'\/' at the center position, the quantity should determine by SIZE
	2.draw'|' at both left and right side
	3.the rest blank should be filled by '.'
	"""
	for i in range(SIZE):
		print('|',end='')
		for j in range(i):
			print('.',end='')
		for k in range(SIZE-i):
			print('\\',end='/')
		for j in range(i):
			print('.',end='')
		print('|',end='')
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()