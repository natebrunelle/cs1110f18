friends = {}    # create an empty dictionary

print('----- create a dictionary -----')
friends = {
    'friend1': 'friend1@virginia.edu',
    'friend2': 'friend2@virginia.edu',
    'friend3': 'friend3@virginia.edu',
    'friend4': 'friend4@virginia.edu',
    'friend5': 'friend5@virginia.edu'
}

print(friends)  # notice that items are printed in any order

print('\n ----- retrieve value using [key] -----')
print(friends['friend3'])
print(friends['friend2'])
# print(friends['friendnotexist'])  # what's wrong?

print('\n ----- add more items -----')
friends['friend91'] = 'friend91@virginia.edu'
friends['friend92'] = 'friend92@virginia.edu'
print(friends)

print('\n ----- reassign value to the key -----')
friends['friend2'] = 'friend-new2@virginia.edu'
print(friends)


print('\n ----- del item -----')
del friends['friend3']
# del friends['nonexistent']     # what's wrong?
print(friends)

print('\n ----- pop an item (and also remove it) -----')
friend4_info = friends.pop('friend4')   # return value and remove item
print('friend4 info =', friend4_info)
print(friends)

# nonexist_friend = friends.pop('noone')   # what's wrong?
# nonexist_friend = friends.pop('noone', 'KeyError - return default msg')


print('\n ----- get number of items -----')
print(len(friends))


print('\n ----- retrieve value with get(key) -----')
print(friends.get('friend5'))   # return value
print(friends.get('friend6'))   # not found, get() returns None
print(friends.get('friend7', 'friend7 cannot be found'))   # if not found, returns default value


print('\n ----- retrieve all keys,values with items() -----')
print(friends.items())


print('\n ----- retrieve all keys with keys() -----')
print(friends.keys())


print('\n ----- retrieve all values with values() -----')
print(friends.values())


print('\n ----- work with dictionary with mixed types of content -----')
favoritefriends = {}
favoritefriends['friend1'] = ['Naruto', 'Pokemon', 'Dragon ball']
favoritefriends['friend2'] = ['Curious George', 'Pokemon']
favoritefriends['friend3'] = ['SpongeBob SquarePants', 'Pokemon']
print(favoritefriends)
print(favoritefriends['friend2'])
print(favoritefriends['friend3'])
# print(favoritefriends['noone'])
# another way to get the item's value
print(favoritefriends.get('friend2'))
print(favoritefriends.get('friend3'))

print('\n -- loop through a list of values --')
list_of_values = favoritefriends.values()
for v in list_of_values:
    print(v)

print('\n -- loop through a list of keys --')
list_of_keys = favoritefriends.keys()
for k in list_of_keys:
    print(k)

print('\n -- loop through a list of key-value pairs --')
list_of_items = favoritefriends.items()
for pair in list_of_items:
    print(pair)

print('\n -- loop through a list of key-value pairs, print key and value --')
# list_of_items = favoritefriends.items()
for somevarforkey, somevarforvalue in favoritefriends.items():
    print('key =', somevarforkey, ':', 'value =', somevarforvalue)


print('\n ----- empty the dictionary -----')
favoritefriends.clear()
print(favoritefriends)



####################

# more examples for Dictionaries

# creating a dictionary
phonebook = {'upsorn': '111-1111', 'Chris':'222-2222', 'Tom':'333-3333'}
print(phonebook)


# accessing / retrieving an item from a dictionary
print('phonebook[\'Tom\'] =', phonebook['Tom'])


# adding items to an existing dictionary
phonebook = {'upsorn': '111-1111', 'Chris':'222-2222', 'Tom':'333-3333'}
phonebook['Joe'] = '444-4444'
print('add \'Joe\', phonebook =', phonebook)

print('print phonebook -->', phonebook)

# deleting items from a dictionary
del phonebook['Chris']
print('delete \'Chris\', phonebook =', phonebook)

# pop()
phone_number = phonebook.pop('upsorn') # return the value associated with a specified key
print('pop(\'upsorn\') =', phone_number, ', phonebook =', phonebook)
print('randomly selected with popitem():' + str(phonebook.popitem())) # remove and return a randomly selected key-value pair
print('phonebook =', phonebook)

# length of dictionaries
num_items = len(phonebook)
print('len(phonebook) =', num_items, ', phonebook =', phonebook)


# let's re-assign our phonebook before trying other examples
phonebook = {'upsorn': '111-1111', 'Chris':'222-2222', 'Tom':'333-3333'}
print('re-assign phonebook =,', phonebook)

# retrieve a value for a particular key
print('phonebook[\'Tom\'] =', phonebook['Tom'])
print('phonebook.get(\'Tom\') =', phonebook.get('Tom'))

# print(phonebook['Tim'])  # - Throws a KeyError exception since it's not there!

# no default value, a non-existent key results in "None"
print('access a non-existent key, phonebook.get(\'Tim\') =',
      phonebook.get('Tim'))

# set default value, a non-existent key results in a default value
print('access a non-existent key, phonebook.get(\'Tim\', \'Key not in phonebook\') =',
      phonebook.get('Tim', 'Key not in phonebook'))

# retrieve all the keys and values
print('phonebook.items() =', phonebook.items())

# retrieve all the available keys
print('phonebook.keys() =', phonebook.keys())

# retrieve all the values
print('phonebook.values() =', phonebook.values())


# in
print('check if \'Tom\' in phonebook =', 'Tom' in phonebook)
print('check if \'Tom\' not in phonebook =', 'Tom' not in phonebook)
print('check if \'Tom\' in phonebook.keys() =', 'Tom' in phonebook.keys())
print('check if \'333-3333\' in phonebook.values() =', '333-3333' in phonebook.values())


# empty the dictionary
phonebook.clear()
print('clear phonebook =', phonebook)

print('-----------------')

# mix data types in a dictionary
test_scores = {'Tom' : [88, 92, 100],
               'John' : [95, 88, 81],
               'Ethan' : [70, 75, 78]}

print('mix data type, test_scores =', test_scores)
print('John\'s scores : ', test_scores['John'])
Ethan_scores = test_scores['Ethan']
print('Ethan\'s scores : ' + str(Ethan_scores))   # notice: why do we need str()?

print('-----------------')

# wrap up
dict = {}
dict[1] = 'cat'
dict['dog'] = -8
dict[False] = 'squirrel'

print(dict.keys())
print(dict.values())
print(dict)

if 'dog' in dict.keys():
    print('dog has a mapping!')
if 'cat' in dict.keys():
    print('cat has a mapping!')

dict['dog'] = 5
print(dict)


print("==== let's do an exercise ====")
# exercise
experience = {}
more_input = 'Y'
# You can do input validation to check if more_input is entered properly.
# However, let's skip that for now.
while more_input == 'Y' or  more_input == 'y':
    name_of_experience = input('Enter name of experience : ')
    company = input('Enter company : ')
    year = input('Enter year : ') # let's make this a string
    experience[year] = [name_of_experience, company]
    #print(experience)
    more_input = input('Do you want to enter more experience ? (Y/N) :')

print(experience)

# What happens if a user enters
# 'software engineer', 'IBM', '1996'
# 'manager', 'Target', '1996'


#-----------------------------------#

experience[1990] = ['sale', 'Walmart']
experience[1996] = ['software engineer', 'IBM']
experience[1995] = ['manager', 'Target']
experience[2000] = ['senior software engineer', 'Microsoft']

print("==== example for pair in dict ====")
for k in experience:
    print("key=", k, "value=", experience[k])

print("==== example for k in dict.keys() ====")
for k in experience.keys():
    print("key=", k, "value=", experience[k])

print("==== example for v in dict.values() ====")
for v in experience.values():
    print("value=", v)

print("==== example for k,v in dict.items() ====")
for k, v in experience.items():
    print("key=", k, "value=", v)

print("==== example nested loops ====")
for k, v in experience.items():     # v is a list 
    print("key =", k)
    for ele in v:
        print("   element in value =", ele)
