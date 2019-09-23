# # This import statement was part of a class example showing how to import
# # functions from other files. If you are having trouble importing a python
# # file that you created, try to put the imported file and the source file that
# # you will be using (in this example: "rays_utilities.py" and "day11.py") both
# # in the project directory. To do this, you can click and drag files on the
# # left from a subdirectory and drop them directly on the project name, which
# # should be the top line in the window. PyCharm usually highlights the project
# # directory with a red outline when you drag files to drop in it.

# # Use the name of the file (without including the .py extension) that contains
# # the function that you want to import.
import rays_utilities

# # During the in-class example, this function was moved to a different file
# # (titled "rays_utilities.py") to show how to import a function that we
# # wrote and have saved in a different python file
# def double_this_num(x, y):  #  x = 3   y = 2
# 	# The next line is a Python docstring. This text will be shown to a
# 	# when they ask for help for this function.
# 	"""double_this_num receives two values, and returns the first value raised
# 	to the power of the second one"""
# 
# 	sum1 = x ** y
# 	# this next line is a side effect
# 	print("inside the function...",sum1)
# 	return sum1
# 
# 
# 
# # These next several lines demonstrate how Python's comparison operators work.
# # The 6 comparison operators are: <  >  <=  >=  ==  !=
# # Run the following and type in values for x and y
# # Make x larger than y, then smaller than y, then the same
# x=int(input("Please enter a number: "))
# y=int(input("Please enter another number: "))
# print(x, ">?", y, x > y)
# print(x, "<?", y, x < y)
# print(x, ">=?", y, x >= y)
# print(x, "<=?", y, x <= y)
# print(x, "==?", y, x == y)
# print(x, "!=?", y, x!= y)
# 
# 
# 
# # Scope is the area where a variable is recognized (or has meaning)
# # Variables can have either local scope within a certain function,
# # or global scope, inside ALL functions AND outside any function 
# # In the following function, x, z, are all local variables, their scope is local
# # to the double_num function. These variables can not be used after the function
# # finishes.
# def double_num(x):
# 	print("3:", x)
# 	print("4:", num1)
# 	z = 1001
# 	result = x + x
# 
# 	return result
# 
# # The variables num1 and y are global variables. They exist outside the scope
# # of any particular function. They can be used here, or inside of the
# # double_num function, or any other function in this file. But trying to use
# # the variables x, z, or result in this area will cause an area, because those
# # variable only exist within the scope of the double_num function
# y = 0
# num1 = 3
# print("1:", num1)
# num1 = double_num(num1)
# print("2:", num1)
# # print("5:", result) # this is an error, python can't access a local variable
# # from global space
# 
# 
