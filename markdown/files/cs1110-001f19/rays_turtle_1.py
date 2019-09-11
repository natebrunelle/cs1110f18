import turtle  # this gives us access to python's turtle graphics library

# create the turtle and assign to variable
sara = turtle.Turtle()  # the name sara was chosen as the variable name for the turtle, but any
						#   legal variable name could be used

# make the turtle blue
sara.color('blue')  # see https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.color

# set the drawling speed
sara.speed('normal')  # see https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.speed

# set the shape of the turtle cursor
sara.shape('turtle')  # see https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.shape


# this first *for* statement ensures that the indented statements will be executed 8 times.
#   each time this loop advances, we draw a different shape (triangle, square, pentagon, ...)
for current_sides in range(8):  # assign the variable current_sides to the numbers: 0,1,2,3,4,5,6, and 7
	sides=current_sides+3  # add 3 to each of those numbers
	print(current_sides+3)  # check to make sure we get: 3,4,5,6,7,8,9, and 10

	# this second *for* statement will cause 3 repetitions the first time, then 4 ... up to 10
	for i in range(sides):  # for each side length (3-10) draw some lines

		# move forward 50 pixels, this is executed once per *sides*
		sara.forward(50)

		# rotate left the by the correct amount (in degrees) for a polygon with *sides* number of sides
		sara.left(360/sides)  # for example: 4 sides would be 90 degrees, 3 sides would be 120

# draw a triangle
# for j in range(3):
# 	sara.forward(200)
# 	sara.left(120)
#                                 #   <- this is earlier code that we have "commented out".
# draw a pentagon                 #        we can remove the #'s to see the code run again.
# for k in range(5):              #        instead of deleting code that is no longer needed,
# 	sara.forward(200)             #        it can be useful to comment it out until you know for sure
# 	sara.left(72)

# turn off the turtle drawing functionality
turtle.done()
