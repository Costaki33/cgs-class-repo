# This program reads in a dictionary and prints the last 10 lines of the file

words = []

# Reads in the dict
def read():
	with open('/usr/share/dict/words', 'r') as r:
		words = r.read().splitlines()

	for i in range(10):
		print(words[i])

# This function reads in words and only prints words that start with 'pyt'
def pyt(words):
	x = words.startswith("pyt")
	print(x)
