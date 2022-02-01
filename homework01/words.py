# This program reads in a dictionary and prints the last 10 lines of the file

words = []


# Reads in the dict
def read():
	with open('/usr/share/dict/words', 'r') as f:
		words = f.read().splitlines()
	
	listlength = len(words)
	
	for i in range(listlength - 10, listlength):
		print(words[i])

# This function reads in words and only prints words that start with 'pyt'
def pyt(words):
	with open('/usr/share/dict/words', 'r') as f:
		words = f.read().splitlines()

	listlength = len(words)

	for i in range(listlength): 	
		if(words[i].startswith("pyt")):
			print(words[i])

read()
pyt(words)
