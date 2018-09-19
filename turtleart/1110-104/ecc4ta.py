import turtle

screen = turtle.Screen()
screen.bgcolor('lightcyan')

red = turtle.Turtle()
red.color('red')
red.pensize(40)

orange = turtle.Turtle()
orange.color('orange')
orange.pensize(40)

yellow = turtle.Turtle()
yellow.color('yellow')
yellow.pensize(40)

green = turtle.Turtle()
green.color('green')
green.pensize(40)

blue = turtle.Turtle()
blue.color('blue')
blue.pensize(40)

purple = turtle.Turtle()
purple.color('purple')
purple.pensize(40)


def rainbow(t,distance, size):
    t.speed('fastest')
    t.pensize(40)
    t.penup()
    t.forward(distance)
    t.left(90)
    t.pendown()
    t.circle(distance, 180)
    t.color('gray')
    t.dot(size, 'gray')
    t.penup()
    t.left(90)
    t.forward(2*distance)
    t.pendown()
    t.dot(size, 'gray')

rainbow(red,280, 80)
rainbow(orange,240, 120)
rainbow(yellow,200, 80)
rainbow(green,160, 120)
rainbow(blue,120, 80)
rainbow(purple,80, 120)



turtle.mainloop()
