# This program iterates over over every integer from 3 to 100 and prints out the number only if it is a prime number

def prime(x, y):

	for num in range(x, y):
		check = 0 
		for i in range(2, (num//2 + 1)):
			if(i % num == 0):
				check = check + 1
				break
		if (check == 0 and num != 1):
			print(" %d" %num, end = " ")

prime(3, 100)

