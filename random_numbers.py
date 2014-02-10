import random
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--max",type=int, help="max number to generate")
	parser.add_argument("-n", "--min",type=int, help="min number to generate",
									  			default=0)
	args = parser.parse_args()
	
	random.seed()
	count = args.min
	numbers = []
	while count < args.max:
		num = random.randint(args.min, args.max)
		if not num in numbers:
			print num
			numbers.append(num)
			count += 1



