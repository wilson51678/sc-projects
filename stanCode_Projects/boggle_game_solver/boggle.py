"""
File: boggle.py
Name: Wilson Wang
----------------------------------------
This program recursively finds all the vocabs for the word input by user in boggle.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global various

result = []				# a list to storage boggle answers


def main():
	"""
	This program let user enter 4 strings of words and use those string to start boggle game.
	"""
	lst = []
	for i in range(4):
		row = input(str(i+1)+' row of letters: ').lower()
		if not check_form(row):
			print("Illegal input")
			return
		new_row = simplify(row)
		lst.append(new_row)

	dictionary = read_dictionary()

	# These double for-loop should target the coordinate of character and start recursion
	for i in range(4):
		for j in range(4):
			find_ans(lst, [(i, j)], dictionary, '', (i, j))

	print('There are '+str(len(result))+' words in total.')


def find_ans(lst, index, d, chosen, coordinate):
	"""
	This function should start back tracking answer in boggle. During back tracking, the function must follow
	"neighbor" rule which means the back tracking could only go left, right, top, down, up-right, up-left,down-right and
	down-left.
	:param lst: list, storage all the strings which users enter in
	:param index: list, storage the coordinate in boggle
	:param d: list, storage all the vocab in dictionary
	:param chosen: string, a string translate from index as the answer of boggle
	:param coordinate: tuple, the coordinate of character at boggle
	:return: none
	"""
	global result

	chosen = ''
	# get characters from list
	for tuple in index:
		chosen += lst[tuple[0]][tuple[1]]

	# base_case
	if len(chosen) >= 4 and chosen in d and chosen not in result:
		print(f"Found \"{chosen}\" ")
		result.append(chosen)

	# recursive_case
	# These double for-loops should limit back tracking in 'neighbor' rule
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			# check the coordinate of tuple is in area
			if 0 <= coordinate[0]+i < 4 and 0 <= coordinate[1]+j < 4:
				# check the coordinate is in list and found in dictionary
				if (coordinate[0]+i, coordinate[1]+j) not in index and has_prefix(index, d, lst):
					# if has_prefix(index, d, lst):
					# choose
					index.append((coordinate[0]+i, coordinate[1]+j))
					# explore
					find_ans(lst, index, d, chosen, (coordinate[0]+i, coordinate[1]+j))
					# un-choose
					index.pop()


def has_prefix(sub_s, dictionary, lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	check_word = ''

	# translate index into string
	for tuple in sub_s:
		check_word += lst[tuple[0]][tuple[1]]

	# get every vocab from dictionary
	for vocab in dictionary:
		# check the sub_s in vocab
		if vocab.startswith(check_word):
			return True
	return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		dictionary = []
		# separate file into lines
		for line in f:
			# separate line into list
			word_list = line.split()
			# separate vocab in list
			for word in word_list:
				dictionary.append(word)
	return dictionary


def check_form(row):
	"""
	This function check the string that user entered is regulated.
	:param row: string, a string of words
	:return: boolean
	"""
	# check the length of row is regulated
	if len(row) < 6 or len(row) > 7:
		return False
	else:
		for i in range(len(row)):
			ch = row[i]
			# check the user enter space between every character
			if i % 2 == 1:
				if ch != ' ':
					return False
			else:
				if not ch.isalpha():
					return False
		return True


def simplify(row):
	"""
	This function simplify a string which has few space between characters.
	:param row: string, a string of words
	:return: ans, a string without space between characters
	"""
	ans = ''
	for ch in row:
		if ch.isalpha():
			ans += ch
	return ans


if __name__ == '__main__':
	main()
