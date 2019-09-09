# variable = name that represents stored in
#            the computer's memory

# create a variable with assignment operator
number = 5       # type is int

# python is dynamic typed language
# type may change when a variable is reassigned
number = "5"     # type is string

# these are all different variables
variable = 5
Variable = 6
vArIaBlE = 7


############################

# Data type = specify the kind of data

# Built-in data types commonly used (in Python)
#   int   -- integer numbers
#   float -- decimal or floating point numbers
#   str   -- strings (= sequence of characters)
#   bool  -- boolean value (True or False)
#   list  -- a collection of ordered, sequence
#   set   -- a collection of unordered, no duplicate sequence
#   dict  -- a collection of key-value pairs (key must be unique and of primitive type)


number = 5
number = "5"
number = [5, "5"]
word = "python"
number = word

list1 = [1,2,3]
list2 = ['a','b','c','d']
list3 = list1
list1 = list2
list4 = list(word)
list1 = list(word)
list2 *= 2    # allow duplicate

set1 = {1, 2, 3}
# set1 += set1      # error, set doesn't allow duplicate


############################

# To see the type of a variable, use type()

number1 = 5
number2 = 5.0
word = 'python'
list1 = [number1, number2, word, True]
print(type(number1))
print(type(number2))
print(type(word))
print(type(list1))


############################

# To convert from one type to another type,
# use the type's name then ()
# For example,
#   int(something_that_look_like_int)
#   float(something_that_look_like_number)
#   str(something)

number1 = 5
number2 = 5.0
word = 'python'

print(str(number1), type(str(number1)))
print(float(number1), type(float(number1)))
print(int(number2), type(int(number2)))
print(str(number2), type(str(number2)))

number3 = '5.0'
print(float(number3), type(float(number3)))
# print(int(number3), type(int(number3)))
# ValueError: invalid literal for int() with base 10: '5.0'

print(int(float(number3)), type(int(float(number3))))

print(list(word), type(list(word)))



############################

# In every programming languages, data types may be
# categorized based on whether their values can change
# (note: change the value,
#        not reassign a variable's value)
# (1) Immutable data type: value cannot be changed
# (2) Mutable data type: value can be changed


# Immutable data type

# Consider the following assignment statement,
# 5 is int (which is a primitive data type),
# it cannot be changed to any variation of int of 5.
# Therefore, int cannot be changed
#   --> "immutable data type"
number = 5

# The same reason applies to str of "5"
# str is a primitive type and cannot be changed
#   --> "immutable data type"
number = "5"

# Let's consider another str example
word = "python"
word = "pothon"
# attempt to replace index 0 of word with "a"
# word[0] = "a"        # error, str is immutable


# Mutable data type

# Consider a variable number of type list,
# containing 2 elements: the first element is an int of 5
# and the second element is a str of "5"
number = [5, "5"]
# To access an element of a list, use [index]
number[0] = 10       # reassign index 0 of number with 10
number[1] = word     # reassign index 1 of number with the value of word variable
list3[1] = list2[1]  # reassign index 1 of list3 with the value of index 1 of list2
print(number)        # observe the elements in number
print(list3)         # observe the elements in list3
# Notice that we can change value of elements of a list
# --> list is mutable data type

# Let's consider a dict (dictionary)
# Create a variable dict1 which is of dict type,
# containing 2 elements.
# Each element is a key-value pair.
# The first element is 'a':'apple'
#     where 'a' is key and 'apple' is value.
# The second element is 'b':'banana'
#     where 'b' is key and 'banana' is value.
dict1 = {'a':'apple', 'b':'banana'}
print(dict1)
# Note: key is used to access an element of a dict
# (unlike list when we can access an element of a list using an index)
# Therefore, key of a dict must be
#    - unique,
#    - primitive data type, and
#    - immutable

dict1['a'] = 'alligator'    # reassign value that is associated with key = 'a'
print(dict1)      # observe key-value pairs
# Notice that we can change value of elements of a dict
# --> dict is mutable data type


############################

# Extra example
# Please note: set is not covered in CS1110/1111;
# set has never been tested, not included in exams.
# Therefore, we will not discuss set in details.
# This is simply to point out another immutable data type.

set1 = {'abc', 'def'}
print(set1)
# set1[0] = 'zzz'    # TypeError: 'set' object does not support item assignment
# print(set1)
# Notice that we cannot change value of elements of a set
# --> set is immutable data type


############################

# Expression

print(15 + 2)
print(15 - 2)
print(15 * 2)
print(15 / 2)
print(15 // 2)
print(15 ** 2)
print(15 % 2)

print(15.0 + 2)
print(float(15) + 2)

print("hello" + "world")
print("hello" * 3)
print("hello" * -3)
print("hello" * 0)
print("hello" * 1)
# print("hello" * 3.5)

a = "".join(['aaa', 'bbb', 'ccc'])
print(a)

b = "@".join(['aaa', 'bbb', 'ccc'])
print(b)

