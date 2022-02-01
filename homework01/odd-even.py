# Creating a function to determin if a list of integers is either even or odd

# A list of integers 
nums = [33, 2, 7, 9, 4, 100, 254, 1329, 96, 24]

# Function to see if the nums of index [i] is either even or odd
def even_odd(nums):
	for i in range(len(nums)):
		# Checks to see if the remainder is 1, if it 1, tbe value is odd, else 			it is even 
		if nums[i] % 2 == 1:
			print("Odd: ", nums[i])
		else:
			print("Even: ", nums[i])
even_odd(nums) 

