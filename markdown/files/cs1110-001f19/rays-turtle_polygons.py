import turtle  # this gives us access to python's turtle graphics library

# create the turtle and assign to variable
ron = turtle.Turtle()

ron.color('teal')
ron.speed('normal')
ron.shape('turtle')

# this 'def' line is establishing a new named action (also called a function)
def polygon(sides, size):
	for i in range(sides):  # execute the body of this loop once per side
		# move forward <value of size> pixels
		ron.forward(size)
		# rotate left the by the correct amount (in degrees) for a polygon with *sides* number of sides
		ron.left(360 / sides)  # for example: 4 sides would be 90 degrees, 3 sides would be 120

# since we have defined what 'polygon' means, we can now use it
polygon(4, 100)  # draw a polygon with 4 sides, where each side is 100 pixels long
polygon(8, 50)
polygon(20, 30)

turtle.done()  # turn off the turtle drawing functionality
