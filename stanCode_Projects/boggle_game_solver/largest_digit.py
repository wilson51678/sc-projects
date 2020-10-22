"""
File: largest_digit.py
Name: Wilson Wang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: None
	"""
	return find_largest_digit_helper(n, 0, 0, 10)


def find_largest_digit_helper(n, ans, count, divisor):
	"""
	This function is a recursion, it should compute the biggest digit in num 'n'.

	:param n: int, the int which set to find the biggest digit
	:param ans: int, the biggest digit in 'n'
	:param count: int, the int represent every digit number
	:param divisor: int, 10
	:return: None
	"""
	# base_case
	if n == 0:
		return ans
	# recursive_case
	else:
		if n > 0:
			count = n % divisor
			if count > ans:
				ans = count
			n = (n-count)//divisor
			return find_largest_digit_helper(n, ans, count, divisor)

		if n < 0:
			count = -(n % -divisor)
			if count > ans:
				ans = count
			n = (n+count)//divisor
			return find_largest_digit_helper(n, ans, count, divisor)


if __name__ == '__main__':
	main()
