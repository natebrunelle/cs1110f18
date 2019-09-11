import turtle
import random  # we will get access to the random library, so that we can generate random numbers

number_of_turtles=10


# this creates a variable called turtle, of type list
# a list is a collection that we can add and remove members from
# we will use this list to add several turtles in to a common group
# then we can just go through the list one-by-one and do some action to each turtle
turtles=[]  # this creates a variable called turtle, of type list


# each time through this loop, we will create a new turtle, and add it to the group
# all of the turtle are named ron, but we will be referring to them as:
# the first turtle in the list, the second turtle in the list, etc.
for i in range(number_of_turtles):
	ron=turtle.Turtle()
	ron.color('teal')
	ron.shape('turtle')
	ron.speed('normal')
	ron.right(90)  # turn each turtle to the right
	ron.forward(20 * i)  # move the turtle down 20 pixels more than the last turtle
	ron.left(90)  # turn each turtle so there are all facing to the right
	turtles.append(ron)  # add the newly created turtle to the end of the list


for i in range(60):  # move each turtle 60 times
	# variable j is assigned to the first turtle in the list the first time through the loop,
	# and then j is assigned to the second turtle in the list the second time through the loop,
	# the loop knows how many items it has in it, and will stop after using the last item
	for j in turtles:
		j.forward(random.randint(1,5))  # since j is a turtle, we can call any turtle action on it
		# we are using the randint function above, to generate a random number from 1-5

turtle.done()
