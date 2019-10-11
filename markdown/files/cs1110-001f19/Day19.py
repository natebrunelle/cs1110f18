


# # review range() function
# # range can be used with 1, 2, or 3 arguments
# #
# for i in range(10):  # i will be 1,2,3,4,5,6,7,8,9
# 	print("variable 'i' is now equal to", i)
#
# for i in range(3, 8):  # i will be 3,4,5,6,7
# 	print("variable 'i' is now equal to", i)
#
# for i in range(3, 12, 2):  # i will be 3,5,7,9,11
# 	print("variable 'i' is now equal to", i)



# # we can use a for loop to interate through characters in a string
# #
# def spell(word):
# 	message = "The word '" + word + "' is spelled "
# 	for letter in word:
# 		message += "'" + letter + "' - "
# 	return message
# print(spell("monkey"))




# # we can use square brackets [] to extract one item
# # For s[0], this is usually read as: "s sub 0", "s at 0", or "s index 0"
# word = "monkey"
# print(word[0])
# print(word[2])


# # how would we get the last letter?
# #
# # We could do this if we knew how long the word is
# # the len() function gives the length of a collection
# word = "monkey"
# last = (len(word))-1
# print(word[last])


# # we can also use negative indexes
# word = "monkey"
# print(word[-1])
# print(word[-3])

# # what about -0 ?
# word = "monkey"
# print(word[-0])


# # how could we change the spell function to return only every-other letter ?
# #
# # manually go through range with index values
# #
#
# def spell2(word):
# 	message = ""
# 	#for letter in word:
# 	for i in range(len(word)):
# 		letter = word[i]
# 		message += "'" + letter + "' - "
# 	return message
# print(spell2("monkey"))



# # now to choose only the even index values
# #
#
# def spell3(word):
# 	message = ""
# 	#for i in range(len(word)):
# 	for i in range(len(word)):
# 		if i%2==0:
# 			letter = word[i]
# 			message += "'" + letter + "' - "
# 	return message
# print(spell3("monkey"))


#
# # what if we use the range function with 3 arguments ... a step size
# def spell4(word):
# 	message = ""
# 	# for i in range(len(word)):
# 	for i in range(0, len(word), 2):
# 		# if i%2==0:
# 		letter = word[i]
# 		message += "'" + letter + "' - "
# 	return message
# print(spell4("monkey"))




# # String Slicing
# # we could also use string slicing to see every other letter
# def spell5(word):
# 	message = word[::2]
# 	return message
# print(spell5("monkey"))
#
#


# # iterate through a list
# #
# # let's make a list of animals
# zoo = ['owl','sloth','zebra','giraffe','cheetah']
#
# def feed(animal):
# 	print("Here " + animal + ", I have some food for you!", sep="")
#
# feed("tiger")
#
# for each in zoo:
# 	feed(each)


# # let's add a list of different foods
# # we need a list for animals and a list for food
# zoo = ['owl','sloth','zebra','giraffe','cheetah']
# meals = ['mice','hibiscus leaves and beans','grass','tasty trees','zebra']
#
# def feed(animal, food):
# 	print("Here " + animal + ", I have some " + food + " for you!")
#
# feed("tiger", "steak")
#
# for i in range(len(zoo)):
# 	feed(zoo[i], meals[i])



# # What about a function for singing Old MacDonald?
# def old_macdonald(animal, sound):
# 	print('Old MacDonald had a farm, E-I-E-I-O')
# 	print('And on that farm he had a ' + animal + ', E-I-E-I-O')
# 	print('With a ' + sound + ', ' + sound + ', here')
# 	print('And a ' + sound + ', ' + sound + ', there')
# 	print('Here a ' + sound + ', there a ' + sound \
# 		  + ', everywhere a ' + sound + ', ' + sound)
# 	print('Old MacDonald had a farm, E-I-E-I-O' + '\n')
# 
# zoo = ['owl','sloth','zebra','giraffe','cheetah']
# noises = ['hoot', 'slow', 'neigh', 'chew', 'roar']
# for i in range(len(zoo)):
# 	old_macdonald(zoo[i], noises[i])
