# Multiple functions: function calls function

# Write a function that takes a number from a user (i.e., from a keyboard)
# then computes and the return the result of
#    ((((number + 9) * 2) - 4) / 2) - number


def magic_number(number):
    # number = int(input("Enter your favorite number: "))
    return ((((number + 9) * 2) - 4) / 2) - number     # make use of parentheses


print(magic_number(9))
print(magic_number(0))
print(magic_number(1))
print(magic_number(-1))
print(magic_number(-15))
print(magic_number(999))


##################################################

# write function
# return vs. print
# variables
# input()
# casting: int()
# global and local scoping
# multiple functions: function calls function

# write a function that takes a number from a user (i.e., from a keyboard)
# calls a magic_number with the given number
# and accumulate the result of running a magic_number function


def accumulate_result():
    pass
    # write your code here








###########
# write code that call accumulate_result 3 times
# and print the final sum

sum_number = 0
accumulate_result()
accumulate_result()
accumulate_result()
print(sum)
