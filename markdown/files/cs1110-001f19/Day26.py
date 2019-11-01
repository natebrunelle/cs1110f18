# Comparing and contrasting 5 different types of collections:
# string, tuple, list, set, dict
#
# my_string = 'abcdefg'
# my_tuple = (2, 7, 9, 13)
# my_list = [2, 7, 9]
# my_set = {2, 7, 9}
# my_dict = {2: 'abc', 7: 'def', 9: 'ghi'}
#
# print('---------- After Initial Assignment ----------')
# print(type(my_string), my_string)
# print(type(my_tuple), my_tuple)
# print(type(my_list), my_list)
# print(type(my_set), my_set)
# print(type(my_dict), my_dict)
#
# # add an item to the collection
# my_string += 'hij'
# my_tuple += (12, 15)
# my_list.append(12)
# my_set.add(12)
# my_dict[12] = 'jkl'
#
# print('\n---------- After Adding ----------')
# print(type(my_string), my_string)
# print(type(my_tuple), my_tuple)
# print(type(my_list), my_list)
# print(type(my_set), my_set)
# print(type(my_dict), my_dict)
#
# # remove an item from the collection
# my_string = my_string[:2] + my_string[3:]
# my_tuple = my_tuple[:2] + my_tuple[3:]
# my_list.remove(9) # can also use pop
# my_set.remove(9)
# my_dict.pop(9)  # can also use popitem
#
# print('\n---------- After Removing ----------')
# print(type(my_string), my_string)
# print(type(my_tuple), my_tuple)
# print(type(my_list), my_list)
# print(type(my_set), my_set)
# print(type(my_dict), my_dict)
#
#
# # change an item in the collection
# my_string = my_string[:4] + 'Z' + my_string[5:]
# my_tuple = my_tuple[:1] + (97, 98) + my_tuple[3:]
# my_list[1] = 99
# # my_set  # this doesn't make sense for sets
# my_dict[7] = 'ZZZZZ'
#
# print('\n---------- After Changing ----------')
# print(type(my_string), my_string)
# print(type(my_tuple), my_tuple)
# print(type(my_list), my_list)
# print(type(my_set), my_set)
# print(type(my_dict), my_dict)
#
#
# # looping through a collection
#
# print('\n---------- Looping Through a String ----------')
# for each in my_string:
# 	print(each)
#
# print('\n---------- Looping Through a Tuple ----------')
# for each in my_tuple:
# 	print(each)
#
# print('\n---------- Looping Through a List ----------')
# for each in my_list:
# 	print(each)
# print('')
#
# # loop through the list using index numbers
# for i in range(len(my_list)):
# 	print(my_list[i])
#
# print('\n---------- Looping Through a Set ----------')
# for each in my_set:  # not sure of the order
# 	print(each)
#
# print('\n---------- Looping Through a Dict ----------')
# for each in my_dict:  # not sure of the order
# 	print(each)
# print('')
#
# for key in my_dict.keys():
# 	print(key)
# print('')
#
# for value in my_dict.values():
# 	print(value)
# print('')
#
# for pair in my_dict.items():
# 	key = pair[0]
# 	value = pair[1]
# 	print(key, value, pair)
# print('')
#
# for key, value in my_dict.items(): # Python calls this 'unpacking'
# 	print(key, value)
#



# Example program: take votes for which restaurant to eat at, and
#   list out the winner
#
#   each restaurant has a related global variable, initialized to 0,
#   the vote function compares the string to related strings and
#      records a vote if it finds a match

# intitalize the variables that store the number of votes for each
# chipotle = 0
# bodos = 0
# mellow = 0
#
# def vote(restaurant, num_votes=1):
# 	'''
# 	given the name of a restaurant and a number of votes,
# 	add those votes to the total for that restaurant
# 	'''
# 	global chipotle, bodos, mellow
# 	if restaurant.lower() in ['chipotle', 'burrito']:
# 		chipotle += num_votes
# 	elif restaurant.lower() in ['bodos', 'bodo\'s', 'bagels']:
# 		bodos += num_votes
# 	elif restaurant.lower() in ['mellow', 'mellow mushroom', 'pizza']:
# 		mellow += num_votes
#
#
#def vote_totals():
#	'''
#	print out the restaurant with the most votes and show
#	how many votes each restaurant received
#	'''
# 	highest = max(chipotle, bodos, mellow)
# 	if chipotle == highest:
# 		print('Chipotle wins!')
# 	if bodos == highest:
# 		print('Bodo\'s wins!')
# 	if mellow == highest:
# 		print('Mellow Mushroom wins!')
# 	print('The total vote was:')
# 	print('\tChipotle -', chipotle)
# 	print('\tBodo\'s -', bodos)
# 	print('\tMellow Mushroom -', mellow)
#
# # accept votes, then compute the total
# vote('Mellow Mushroom')
# vote('Bodos')
# vote('Pizza')
# vote('Chipotle', 3)
# vote_totals()





# # Let's improve the restaurant voting by using dict's
# # We we are finished, we won't need specific variable names for
# # restaurants. We won't even need to have any names of restaurants
# # to start.
# #
# # We don't need these variable anymore
# # chipotle = 0
# # bodos = 0
# # mellow = 0
#
# # restaurant dict - restaurant name is key, number of votes is value
# r = {
# 	'chipotle': 0,
# 	'bodos': 0,
# 	'mellow': 0,
# 	}
# # we can use a dict to store alternate forms of a restaurant name
# alt_names = {
# 	'burrito':'chipotle',
# 	'bodo\'s': 'bodos',
# 	'bagels': 'bodos',
# 	'mellow mushroom': 'mellow',
# 	'pizza': 'mellow',
# }
#
# def vote(restaurant, num_votes=1):
# 	# global r
#	# determine if the restaurant name is an alternate name
# 	restaurant = restaurant.lower()
# 	if restaurant in alt_names:
# 		restaurant = alt_names[restaurant]
#
#   # this isn't needed anymore
# 	# if restaurant == 'chipotle':
# 	# 	r['chipotle'] += num_votes
# 	# elif restaurant == 'bodos':
# 	# 	r['bodos'] += num_votes
# 	# elif restaurant == 'mellow':
# 	# 	r['mellow'] += num_votes
# 	# else:
# 	# 	print('Restaurant name "' + restaurant + '" not recognized.')
#
#	# if the restaurant already exists, add the votes in
# 	if restaurant in r.keys():
# 		r[restaurant] += num_votes
# 	else: # otherwise ask the user to ignore it or add it
# 		new_r = input('Restaurant name "' + restaurant
# 					  + '" not recognized. Do you want to add it? ')
# 		if new_r.lower() in ['y', 'yes']:
# 			r[restaurant] = num_votes
#
# def get_vote():
#	'''
#	prompt the user to enter a restaurant and number of votes
#	'''
# 	name = input('Who are you voting for? ')
# 	num1 = int(input('How many votes for ' + name + '? '))
# 	vote(name, num1)
#
# def vote_totals():
# 	highest = max(r.values())
#	# these if statements can be replaced by a loop
# 	# if r['chipotle'] == highest:
# 	# 	print('Chipotle wins!')
# 	# if r['bodos'] == highest:
# 	# 	print('Bodo\'s wins!')
# 	# if r['mellow'] == highest:
# 	# 	print('Mellow Mushroom wins!')
# 	for key in r.keys():
# 		if r[key] == highest:
# 			print(key.capitalize(), 'wins!')
# 	print('The total vote was:')
#   # These print statement can be placed in a loop
# 	# print('\tChipotle -', r['chipotle'])
# 	# print('\tBodo\'s -', r['bodos'])
# 	# print('\tMellow Mushroom -', r['mellow'])
# 	for key in r.keys():
# 		print('\t', key.capitalize(), '-', r[key])
#
# vote('Mellow Mushroom')
# vote('Bodos', 3)
# #vote('roots')
# vote('pizza')
# vote('Chipotle', 3)
# vote('Chipotle')
# vote('bagels')
# #vote('Roots')
# get_vote()
# vote_totals()
#
#
