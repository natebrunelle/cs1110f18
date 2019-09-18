# # goal of this function is to double a number
# # input: the number that I want doubled
# # output (return value): the doubled number
# def double_the_number(x):  # this is assigning the variable x to the value of the argument
# 	x_doubled = x + x
# 	return x_doubled
#
# my_num = float(input("Enter a number: "))  # remember to typecast if you want something other than a string
# doubled_my_num = double_the_number(my_num)
# print("When we double", my_num, "we get", doubled_my_num)


# # in the computer's memory, this is what's going on when storing variables....
# #
# # variable name   |   variable type   | variable address
# #
# #   my_num                float              0xFA724B
# #   name                  string             0xA73D91


# # you can always experiment with Python to learn the language better
# # In this example, we are experimenting with types and operators
# # try various operators on different pairings and orderings of a string and an int
# #
# str1="hello"
# int1=9
# result=str1*int1   # swap the order, use different operators, etc.
# print(type(result))
# print(result)

# # and example of a function that doesn't return anything
# def silly_function():  # no parameters
# 	print("this is just a print line in the silly function")
# 	return
#
# result = silly_function()
# print("the silly function returned:", result) # notice that the return is None


# # since we ask the user to enter an integer often, we could create a function
# # that would allow us to put the call to input, the type casting, and more
# # (in the future, we'll think about input validation) all in one place
# def get_int(the_prompt):
# 	in_num = int(input(the_prompt))
# 	return in_num
#
# large = get_int("Enter a large number: ")
# print(large*2, "is larger than", large)


# # next, we'll discuss putting a function like this in a different file
# # than the one we are currently working on. Then we can call it anytime we
# # want by using import
