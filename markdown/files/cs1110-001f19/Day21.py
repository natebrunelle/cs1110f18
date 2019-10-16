
# # example of hard to understand function and bad docstring
#
# """An example of a function that is hard to understand because
# it has bad style."""
#
# def hs(llI):
#     """Returns ll1 made in a "for lI1 in llI" loop"""
#     ll1 =llI[ 0 ]
#     for lI1 in llI :
#         if lI1 >ll1:
#             ll1 =lI1
#     return ll1
#
# consider = '''
# What type of value does hs expect as an argument?
#
# What type of value does it return?
#
# What's a better docstring?
#
# What are better names for variables and the function?
# '''


# introduce PEP8
#


# # other kinds of collections
# # tuples - pronounced either: too-ple or tuh-ple
# # range vs. strings vs. lists vs. tuples
# # mutability: lists vs. tuples vs. strings
#
# my_list = [1,2,3,4,5]
# def change2(collection):
#  collection[2] = 'hello'
#
# print(my_list)
#
#
# # what if the list is changed to a tuple?



# # view change2 in pythontutor
# # pass in a list, then pass in a tuple



# # let's look at modifying a single value in a collection
#
# my_list = [1,2,3,4,5]
#
#
# def change2(collection):
#     collection[2] = 'hello'
#
# def double(collection):
#     for i in range(len(collection)):
#         collection[i] *= 2
#
# print(my_list)
# double(my_list)
# print(my_list)



# # another list vs. tuple comparison
#
# my_list = [1, 2.7, 'hello', True]
# my_tuple = (1, 2.7, 'hello', True)
#
# for thing in my_list:
#     print(thing)
#
# for thing in my_tuple:
#     print(thing)
#
# print(my_list[2])
# print(my_tuple[2])
#
# print(my_list)
# my_list[0] = 100
# print(my_list)
#
# print(my_tuple)
# my_tuple[0] = 100
# print(my_tuple)



