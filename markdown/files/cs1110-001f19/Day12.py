# # Thinking about scope - In this example, the variable name b is used both for
# # a local variable inside of function f, and for a global variable. These are
# # two different variables that are independent of each other.
# def f(a):
# 	b = a + 5  # this b is a local variable, it's scope is function f
# 	#  On the next line of python code, python will use the local variable b,
# 	#  since a local variable of that name exists. But if the line above,
# 	#  is commented out, python will use the global variable b, since no local
# 	#  version exists.
# 	print("Statement D: The value of b is", b)
# 	return b
#
#
# b = 4  # this b is a global variable, it has global scope
# print("Statement A: The value of b is", b)
# y = f(7)
# print("Statement B: The value of y is", y)
# print("Statement C: The value of b is", b)


# #  In this example, the find_tip function has 3 parameters. The last 2
# #  parameters each have default values assigned to them. When this function is
# #  called, arguments do not need to be sent for parameters that already have
# #  default values assigned. But if arguments are sent in, they will be assigned
# #  to these parameters instead of using the default values.
# def find_tip(bill, percentage=.20, msg="Thank you for the excellent service"):
# 	amount_of_tip = bill * percentage
# 	print(msg)
# 	return amount_of_tip
#
#
# bill_amount = float(input("How much was your bill? "))
# #  Only 1 argument is sent. So the last 2 parameters will be their defaults
# tip_amount = find_tip(bill_amount)
# print("For a bill of", bill_amount, "you should tip", round(tip_amount, 2))
# #  The same function is called, but here 3 arguments are sent
# customized_tip_amount = find_tip(bill_amount, .45, "THANKS!!!!!!!!")
# print("For a bill of", bill_amount, "your customized tip", round(customized_tip_amount, 2))
# #  When calling a function that has some default arguments, the arguments that
# #  have defaults can be skipped and later ones assigned by using the parameter
# #  names of the ones that you want to assign. In this example, the 2nd
# #  argument, percentage is skipped and the parameter msg is assigned by name
# find_tip(4, msg="This is a new message")
# print("For a bill of", bill_amount, "your customized tip", round(customized_tip_amount, 2))


# #  The print function that we've been using has several parameters with default
# #  arguments. The sep parameter assigns the value of the string that will be
# #  printed between the arguments. If not specified, this value is one space.
# #  The end parameter assigns the value of the string that will be printed
# #  at the end of the print statements. If not specified, this value is one a
# #  new line character. That's why print statements usually separate multiple
# #  arguments by spaces and move the cursor position to the next line.
# print("one", "two", "three")
# print("one", "two", "three", sep="")
# print("one", "two", "three", sep="___")
# print("one", "two", "three", sep="this is the area in between")
# 
# print("Hello1")
# print("Hello2", end="")
# print("Hello3", end="")
# print("Hello4", end="")
# print("Hello5", end="!!!???")
# print("Hello6", end=".\n")
# print("Hello7")
# print("Hello8")


