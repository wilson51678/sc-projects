"""
File: weather_master.py
Name: Wilson Wang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# The value to stop program
EXIT = -100


def main():
	"""
	This program should implement a console program
	that asks weather data from user to compute the
	average, highest, lowest, cold days among the inputs.
	"""

	print("stanCode \"weather master 4.0")
	new_data = int(input('Next temperature: (or '+str(EXIT)+' to quit)?'))
	# no temperature enter
	if new_data == EXIT:
		print('No temperature were entered')
	# first temperature enter
	else:
		maximum = new_data
		minimum = new_data
		total = new_data
		days = 0
		# determine whether first temperature is cold day
		if new_data	< 16:
			days = 1
		times = 1
		while True:
			# second temperature enter
			new_data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)?'))
			# no temperature enter
			if new_data == EXIT:
				break
			# new temperature would become maximum
			if new_data > maximum:
				maximum = new_data
			# new temperature would counts as cold day
			if new_data < 16:
				days += 1
			# new temperature would become minimum
			if new_data < minimum:
				minimum = new_data
			# total and times are made for counting average of all temperatures
			total = new_data + total
			times += 1

		average = total / times

		print('Highest temperature = '+str(maximum))
		print('Lowest temperature ='+str(minimum))
		print('Average ='+str(average))
		print(str(days)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
