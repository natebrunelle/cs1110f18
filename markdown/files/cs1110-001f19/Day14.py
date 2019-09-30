

# # Practice with evaluating boolean expressions
# x = 7
# a = (x == 7)  # T
# b = (x != 7)  # F
# c = (x < 7)  # F
# d = (x <= (3 + 4))  # T
# e = (x < 0 or x > 10)  # F
# f = (x > 0 or x < 100)  # T
# g = (x > 0 and x < 100)  # T
# h = (x == 2 or 5)  # Expected F, produced something else
# i = (x == 3 or 7.3)  # Expected T, produced something else
# # For variables i and h above, the right side of the <or> statement
# # is not a boolean expression and gives unexpected results
# # Make sure to use <and> <or> <not> with boolean expressions,
# # not ints, floats, strings, etc.
#
# print("Variable a:", a, type(a))
# print("Variable b:", b, type(b))
# print("Variable c:", c, type(c))
# print("Variable d:", d, type(d))
# print("Variable e:", e, type(e))
# print("Variable f:", f, type(f))
# print("Variable g:", g, type(g))
# print("Variable h:", h, type(h))
# print("Variable i:", i, type(i))



###############################################################################



# Given below are several versions of a function that calculates if a given
# year is a leap year. Although each function produces the correct answer,
# they are written very differently.


# # These are some test cases that you can use for all of the leap year
# # functions. Make sure to put them after the function definition.
# print(is_leap_year(2019))  # 2019 - no
# print(is_leap_year(2020))  # 2020 - yes
# print(is_leap_year(2100))  # 2100 - no
# print(is_leap_year(2000))  # 2000 - yes
# print(is_leap_year(0))  # 0 - yes


# # In this first version of the function, we have taken our text description
# #    "If a year is divisible by 4, it is a leap year, unless it is also
# #    divisible by 100, then it’s not, unless it is also divisible by 400,
# #    then it is."
# # and converted it to a an equivalent <if> statement.
# def is_leap_year(x):
#   # We use these 3 variables to hold True/False values for divisibility
# 	div4 = ((x % 4) == 0)  # a year is evenly divisible by 4 - True or False
# 	div100 = ((x % 100) == 0)  # a year is divisible by 100 - True or False
# 	div400 = ((x % 400) == 0)  # a year is divisible by 400 - True or False
#
# 	if div4:
# 		if div100:
# 			if div400:
# 				return True
# 			else:
# 				return False
# 		else:
# 			return True
# 	else:
#		return False


# # In this version of the function, we started with the most constrained case,
# # which was any year divisible by 400 - we know that is a leap year and the
# # other calculations won't matter for that year. Then we take the next most
# # constrained case and continue on until all cases have been considered.
# #
#def is_leap_year(x):
	# # if a year is divisible by 4
	# div4 = ((x % 4) == 0)
	# div100 = ((x % 100) == 0)
	# div400 = ((x % 400) == 0)
	#
	# if div400:
	# 	return True
	# elif div100:
	# 	return False
	# elif div4:
	# 	return True
	# else:
	# 	return False



# # this version reduces the if statement in to one boolean expression that
# # uses boolean operators
# def is_leap_year(x):
# 	div4 = ((x % 4) == 0)
# 	div100 = ((x % 100) == 0)
# 	div400 = ((x % 400) == 0)
#
#   # In the following line, if div400 is True, then it doesn't matter is on
#   # the other side of the <or>, the whole expression will be True.
#   # But if div400 is not True, both div4 and (not div100) must be True to
#   # make the expression True.
# 	return (div400 or ((not div100) and div4))



# # This version takes the previous version and replace the variables with the
# # expressions that they were assigned to. This version works correctly and is
# # extremely short, but I would not use it because it is difficult to read, and
# # would be difficult to debug if it contained an error
# def is_leap_year(x):
# 	return (((x % 400) == 0) or ((not ((x % 100) == 0)) and ((x % 4) == 0)))



# # These are some test cases that you can use for all of the leap year
# # functions. Make sure to put them after the function definition.
# print(is_leap_year(2019))  # 2019 - no
# print(is_leap_year(2020))  # 2020 - yes
# print(is_leap_year(2100))  # 2100 - no
# print(is_leap_year(2000))  # 2000 - yes
# print(is_leap_year(0))  # 0 - yes


###############################################################################

