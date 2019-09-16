
# # using the input function
# user1 = input("Please enter a number: ")  # input always returns a value of type string
# print("You typed in", user1)
# print(user1+user1)
#
# # this is "type-casting", user1 will now be of integer type
# user1 = int(user1)

# # example code demonstrating string concatenation
# str1 = "bubble"
# str2 = "will"
#
# print(str1, str2)  # by default, the print function will add a space between arguments
#
# str3 = str1 + " " + str2  # concatenation
# print(str3)  # the plus sign is an "overloaded" operator, it adds numbers and concatenates strings
#
# x = 2
# y = 5
# # the * will perform string repetition when the left operand is a string, and the right operand is an integer
# print(str1*8)


# # assignment statements
# x = 1  # this is an assignment statement
# x = 2  # read  this as "x is assigned the value 2"
# x = 3  # some languages use a different symbol, such as <-
# print(x)

# # this won't work
# 7 = x  # the value on the right will be assigned to the variable on the right???
# print(x)

# # operations with integers and floats
# num1 = 3
# num2 = 4
# num3 = 5.2
# num4 = 7.1
# answer1 = num1 - num2
# answer2 = num2 - num3
# answer3 = num3 - num4
# print("The value of answer1 is", answer1)
# print("The value of answer2 is", answer2)
# print("The value of answer3 is", answer3)


# # Decimal values (we usually call these "floats") can not be represented exactly by a computer,
# # so we need to be careful to not expect them to be exact
# a = 0.15 + 0.15
# b = 0.1 + 0.2
# if a==b:
# 	print(a, "equals", b)
# else:
# 	print(a, "does not equal", b)


# # remember that the input() function always produces/returns a string
# # try this code with two words, then try it again with two numbers
# x = input("Enter something: ")
# y = input("Enter something else: ")
# print(x + ' + ' + y + ' = ' + (x+y))


# # We will learn more about string functions later, but for now ...
# rays_word = "racecar"
# backwards_word = "".join(reversed(rays_word))
# if rays_word == backwards_word:
# 	print(rays_word, "is a palindrome")
# else:
# 	print(rays_word, "is NOT a palindrome")


