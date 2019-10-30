# # revisiting mystery2 function from Monday's class
# def mystery(x, y):
#     z = 0
#     while x >= y:
#         x -= y
#         z += 1
#     return z#
#
# #print(mystery(563,10))
# #print(mystery(0,0)) # infinite loop!

# def mystery2(x, y):
#     z = 0
#     while x >= y:
#         x = mystery(x, y) # x // y
#         z += 1
#     return z
#
# print(mystery2(10,2))
# print(mystery2(100,2))
# print(mystery2(1000,2))  # logarithim

# # create a function to convert a number to it's absolute value
#
# def av(x):
#     ''' receive a number and return its absolute value '''
#     #x**2 x**0.5
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(av(8))
# print(av(13))
# print(av(-8))
# print(av(-13))
# print(av(14.6))
# print(av(6.11111))
# print(av(-9282.262))
# print(av(-3.121))
# print(av(0))
# print(av(-8.0))
# print(av(8.0))



# equivalence classes for av()?
# positive
# negative
# float
# integer


# median of 3 function

# equivalence classes?
# orderings?



# [ collections slide ]
# looking at sets and dictionaries -
# order doesn't matter -
# sets
# dictionaries
#
# show difference between sets and lists
#

my_list = [2, 5.6, "hello", 17, "a", 52332.26457]
my_set = {2, 5.6, "hello", 17, "a", 52332.26457}
print(my_list)
print(my_set)

my_list.append(999)
my_list.append(2)
print(my_list)
print(my_set)

my_set.add(999)
my_set.add(2)
print(my_list)
print(my_set)
