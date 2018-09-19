import turtle


t = turtle.Turtle()
t.speed('fastest')

win = turtle.Screen()
win.bgcolor("#0000F0")

# repeat 20 times:
for i in range(300):
    t.forward(0.05*i)  # varying distances
    t.right(15)  # fixed angle
    t.pendown()
    t.color('brown')
t.penup()
t.forward(100)
t.pendown()


def polygon(t, sides, length):
    for i in range(sides):
        t.forward(length)
        t.right(360/sides)
        t.color('yellow')

polygon(t, 20, 15)
t.penup()
t.right(100)
t.backward(30)
t.pendown()
polygon(t, 20, 15)
t.penup()
t.right(60)
t.forward(140)
t.pendown()
polygon(t, 20, 15)
t.penup()
t.forward(110)
t.left(200)
t.pendown()
polygon(t, 20, 15)
t.penup()
t.right(70)
t.forward(135)
t.pendown()
polygon(t, 20, 15)
t.penup()
t.left(50)
t.forward(70)
t.pendown()
polygon(t, 20, 15)

t.color("white")
turtle.mainloop()
