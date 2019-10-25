# # create a dictionary with existing key-value pairs
# d = {}
# print(type(d), d)
#
# # create an empty dictionary and add to it
# d[24] = 19
# d[323] = 5.7
# print(type(d), d)
#
# d = {4: 7, 6: 56, 0: 34}
# print(type(d), d)
#
# # load a dictionary through input statements
#
# marbles = {}
# quit = 'n'
# while quit != 'y':
# 	id = input("What is the marble's ID? ")
# 	c = input("What is the marble's color? ")
# 	dia = input("What is the marble's diameter? ")
# 	marbles[id] = [c, dia]
#
# 	quit = input("Do you want to quit [y to quit]: ")
# print(type(marbles), marbles)
#
# marbles = {'256': ['green', '14.32'], '9872': ['orange', '87.1'],
#            '76': ['grey', '7.1']}
# print(type(marbles), marbles)
# marbles['256'] = ['teal', '14,32']
# print(type(marbles), marbles)
#
# print(type(marbles), marbles)
# if '9872' in marbles:
# 	print(marbles['9872'])
# else:
# 	print('not there')
# print(type(marbles), marbles)
#
# print(type(marbles), marbles)
#
# # looping to get key and value
# for k in marbles:
# 	print(type(k), k)
# 	print(type(marbles[k]), marbles[k])
#
# for each in marbles.values():
# 	print(type(each), each)
#
# for each in marbles.keys():
# 	print(type(each), each)
#
# for each in marbles.items():
# 	print(type(each), each)
# 	print(each[1])
#
# dictionary with 2 key-value pairs. The keys are 4 and 7
# d = {4: "hi", 7: "bye", 12: "Friday!!!"}
#
# print(type(d), d)
# for x in d:
# 	print(type(x), x)
#
# print('*' * 30)
# print(type(d.keys()), d.keys())
# for x in d.keys():
# 	print(type(x), x)
#
# print('*' * 30)
# print(type(d.values()), d.values())
# for x in d.values():
# 	print(type(x), x)
#
# print('*' * 30)
# print(type(d.items()), d.items())
# for x in d.items():
# 	print(type(x), x)
