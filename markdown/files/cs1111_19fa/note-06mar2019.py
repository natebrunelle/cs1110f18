# review range
x = range(5)
print('assign range(5) to x', x)
print('cast x to list', list(x))
print('access element of x', x[1])

print('---- try range up to negative integer ---')
x = range(-5)
print('assign range(-5) to x', x)
# no element in a collection
# because range start from index 0, can't increment to -5
print('cast x to list', list(x))
# when iterating over an empty collection
# statements inside the loop won't be executed

print('---- try range of negative integers ---')
x = range(0, -30, -5)
print('assign range(0, -30, -3) to x', x)
print('cast x to list', list(x))

# slice collection created by range
print('x[2::2] =', x[2::2])
print('list(range(-10,-30, -10)) =', list(range(-10,-30, -10)))
print('list(x[2::2]) =', list(x[2::2]))
print('len(x) =', len(x), '= len(list(x)) =', len(list(x)))

print('---- reverse order of elements in the collection ---')
print('x[::-1] =', x[::-1])
print('list(range(-25, 5, 5)) =', list(range(-25, 5, 5)))
print('list(x[::-1]) =', list(x[::-1]))

print('---- what type do we get ----')
print('type(x[::-1]) =', type(x[::-1]))
print('type(list(range(-25, 5, 5))) =', type(list(range(-25, 5, 5))))
print('type(list(x[::-1])) =', type(list(x[::-1])))

print('\n===========================\n')

# slides 2-3
# transition from range and string to list
# almost all operations we can do with string and range
# can be done with list (plus the mutability)

# slide 4
# create a list, using [ ]
animals = ['cow', 'dog', 'horse', 'sheep', 'pig']
print('create a list', animals)

# we can concept the list
animals2 = ['goat', 'duck']
animals += animals2
print('concat lists =', animals)

# we can repeat elements in list
animals3 = animals2 * 2
print('repeated elements in list =', animals3)

# slide 5
print('--- check if a certain element is in (or not in) a list ---')
print('horse in animals?', 'horse' in animals)
print('bird in animals?', 'bird' in animals)
print('bird not in animals?', 'bird' not in animals)

# slide 6
print('--- access element in list ---')
print('animals[2] =', animals[2])    # access element at index 2
print('animals[-2] =', animals[-2])  # access element, 2 backward index, for end of list

# slide 7
print('--- get the number of elements in list ---')
print('len(animals) =', len(animals))

# slide 8
print('--- add element to list ---')
print(animals.append('bird'))    # append element to the end of the list, return (or evaluate to) None
print('after append, animals =', animals)

print(animals.insert(2, 'cat'))  # insert element at a given position (index), return (or evaluate to) None
print('after insert, animals =', animals)

# slide 9
print('--- remove element from list ---')
# del is a keyword, can't print it
del animals[3]        		     # remove by index, do not have return value
print(animals)
print(animals.pop())             # remove the last element, return its value
print(animals.pop(1))            # remove element at index 1, return its value
print(animals)
print(animals.remove('sheep'))   # remove by element, return (or evaluate to) None
print(animals)

# slide 10
print('--- sort elements (ascending order) in list ---')
print(animals.sort())    # sort a list in ascending order, return None
print('sorted animals =', animals)
# another way to print (notice a space after "=")
print('sorted animals = ' + str(animals))

print('--- sort elements (descending order) in list ---')
print(animals.reverse())  # reverse order of elements in a list, return None
print('reversed animals = ', animals)

# slide 11
print('--- get index of a particular element ---')
print(animals.index('cow'))  # return the lowest index of element
# If element is not in the list, raise ValueError
# the index() behaves the same when using with string

# slide 12
print('--- casting a collection into a list ---')
letters = 'ABCDEFG'
print(list(letters))

# numbers = 1234567
# print(list(numbers))   # can't cast integer to list, integer is not a collection

# slide 13
print('--- slice a list ---')
lst = [5, '7', True, ['a', 'b'], 15, False, '1111']
print('lst =', lst)
print('lst[1:4] =', lst[1:4])
print('lst[1:] =', lst[1:])
print('lst[:4] =', lst[:4])
print('lst[:-1] =', lst[:-1])
print('lst[::-1] =', lst[::-1])
print('lst[1:5:2] =', lst[1:5:2])
# works the same way as slicing in string and range

# slides 14-16
# trace through code
#  - by hand (refer to slides for reference)
#  - use http://pythontutor.com/visualize.html


print('\n---- let\'s use loop and list ----')
my_colors = ['blue', 'green', 'brown']
friend_colors = ['pink', 'red', 'blue', 'white', 'green']
print('my favorite colors =', my_colors)
print('friend\'s favorite colors =' + str(friend_colors))

# count how many colors that both my friend and I like
number_both_like = 0
for i in friend_colors:
    if i in my_colors:
        number_both_like += 1
print('There are', number_both_like, 'colors we both like')


# slide 17
# 2D list is similar to table (or grid)





