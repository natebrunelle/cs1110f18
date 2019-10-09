# 10/4/19 Day17. Day15 was Exam1 Review. Day16 was Exam1.

# print("Today we are talking about repetition")
#
# Here are 2 types of repetition (there are others):
#
# 1.) Repeat a certain number of times
# vs.
# 2.) Repeat until something happens (repeat until some condition exists)
#
# while loops are used for the second type above
#
# Define code that runs until a condition is False.
# As long as this condition is True, keep doing these actions.
#



# # Example 1 - Are we there yet?
# # Keep checking until we are there....
# #
# text = input("Are we there yet? ")  # what happens if we do not give answer
# 									  # a value before the loop?
# while text == 'no':   # the condition is - <text == 'no'>
# 	text = input("Are we there yet? ")  # but if we changed text to text1?
# 	print("Whatever...")
#   # This next line is just for debugging. The program prints the input prompt
#   # then waits until the user enters something before continuing
#	input("This is really just to pause my program at this line")
#
# print("Program Finished")




# # Example 2 - Countdown timer
# # Create a function that counts down from a given number to 0.
# # Show each number as the countdown happens, at 0 print "Blastoff!"
# #
# def countdown(seconds):
#	# What condition should we use?
# 	while seconds > 0:  # This is better than using 'seconds != 0' Why?
# 		print(seconds)
# 		seconds-=1  # what if we used seconds+=1
# 	print("Blastoff!!!")
#
# countdown(10)
# print("Program Finished")




# # Example 3 - Fizzbuzz
# # Look at every number in a certain range to see which are fizzbuzz numbers.
# # if the number is divisible by 3, print 'fizz'
# # if the number is divisible by 5, print 'buzz'
# # if the number is divisible by both, print 'fizzbuzz'
# #
# def fizzbuzz(x):
# 	while x >= 0:  # 
# 		print(x," ",end="") # print out each number as we count down
# 		if x % 3 == 0: # if the number is divible by 3
# 			print("fizz",end="") # don't go to a new line yet
# 		if x % 5 == 0:
# 			print("buzz",end="")
# 		print() # move the cursor to the next line
# 		x-=1 # What if we move this back to the left one indention level?
# 
# fizzbuzz(30)
# print("Program Finished")

