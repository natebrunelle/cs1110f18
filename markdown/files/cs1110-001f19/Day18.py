#
# repeat a certain number of times        (use a *for* loop)
# vs.
# repeat until a specific thing changes   (use a *while* loop)
#
#
# # example of are we there yet
# # a while loop is like having an infinite number of if statements
#
# # Example 1 - Are we there yet?
# # Keep checking until we are there....
# #
# text = input("Are we there yet? ")
# while text == 'no':
#     text = input("Are we there yet? ")
#
# print("Program Finished")




# use a while loop to count up
#
# How many dozen eggs do I need to buy?
#
# eggs_bought = 0
# target = int(input("How many eggs do you need? "))
# while (eggs_bought * 12) < target:
#     eggs_bought += 1
#
# print("You should buy", eggs_bought, "dozen")






# for loops
# for <variable> in <collection>:
# explain collections
#
# count up
# for i in range(7): # calling range with one argument
#     print(i)

# for i in range(1276, 8512): # calling range with two arguments
#     print(i)

# s = "Exam 1 was awesome!"
# for letter in s: # using a for loop to iterate through a string
#     if letter == " ":
#         print("I found a space")


# lists can hold items of mixed types
# my_list = [2,7.0,"hello",True,9] 
# for each in my_list:  # using a for loop to iterate through a list
#     print(each, "of type", type(each))

# ... thinking about loops and scope
# for i in range(5):
#     x = i  # will x be in scope outside the loop?
#     print(x)
# print("out of loop, i is", i)

