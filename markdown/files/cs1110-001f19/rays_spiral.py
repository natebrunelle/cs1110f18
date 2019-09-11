import turtle

sara=turtle.Turtle()
sara.speed('fastest')
length=4
angle=20

# in these 2 spiral example, notice how we have a variable that is increased (or decreased)
# in value each time thought the loop. the variables are being set to their old value

#
# # draw a "square" spiral.
# for i in range(30):  # draw 30 segments
# 	sara.forward(length)
# 	sara.left(90)
#   # the length should increase with each new segment drawn
# 	length=length+10  # the new value of length is set to the old value of length plus 10


# draw a "curved" spiral
for i in range(200):
	sara.forward(length) # the length of each side won't change
	sara.left(angle)  # the angle needs to get smaller and smaller with each segment drawn
	angle=angle*0.99  # so the shape will not *close*, but open wider and wider

turtle.done()
