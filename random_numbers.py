"""
Generates a randomized ordering of numbers between a given max and min. It
can be run standalone with command-line arguments (see --help for details).

By Alex Shaver
"""
import random

import argparse

def get_random_numbers(min_number, max_number):
	"""
	Returns a randomized ordering of all of the numbers between a given
	minimum and maximium (inclusive).

	Args:
		min_number: the number to start the range at
		max_number: the number to end the range with

	Returns:
		a Python list containing the numbers in a randomized order
	"""
	
	if min_number > max_number:
		raise ValueError('max must be > min')
	
	random.seed()
	count = min_number
	numbers = []
	while count <= max_number:
		num = random.randint(min_number, max_number)
		if not num in numbers:
			numbers.append(num)
			count += 1
	return numbers

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--max",type=int, help="max number to generate")
	parser.add_argument("-n", "--min",type=int, help="min number to generate",
									  			default=0)
	args = parser.parse_args()

	print get_random_numbers(args.min, args.max)
