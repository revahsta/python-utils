"""
Takes a word and generates a number of versions of that word with the
characters shifted around. The word must be at more than two characters
long. It is intended to be used on single words, but could also work
phrases.

 By Alex Shaver
"""
import argparse
import random
import sys

def SwapWord(word, num_words):
	"""
	Swaps a word around to produce a number of other "words".

	Args:
		word: the word you want to swap around
		num_words: the number of "words" to produce
	
	Returns:
		a list containing the words produced
	"""
	
	if len(word) <= 2:
		raise ValueError('word must have length > 2')
	if num_words <= 0:
		raise ValueError('num_words must be > 0')

	random.seed()

	words = []
	# make the requested number of randomized words
	for i in range(0, num_words):
		positions = [] # list of positions already chosen
		# iterate through the string
		newWord = list(word)
		for char in word:
			# create a list to contain the letters of the new word
			while(True):
				# choose a position in the string
				position = random.randint(0,len(word) - 1)
				# check if the position hasn't already been chosen
				if position not in positions:
					# add position to the list
					positions.append(position)
					# put the character in the new word
					newWord[position] = char
					break
				else:
					continue
		word = "".join(newWord)
		
		words.append(word)
	return words

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("word", help="word to swap around(length > 2)")
	parser.add_argument("-n", "--num", help="number of swapped words to produce",
							  default=5,type=int)
	args = parser.parse_args()
	
	try:
		word_list = SwapWord(args.word, args.num)
	except ValueError as e:
		print "Invalid Input: " + str(e)
		sys.exit(1)

	for word in word_list:
		print word
