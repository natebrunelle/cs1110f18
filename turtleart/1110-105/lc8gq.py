import turtle


t = turtle. Turtle()
t.speed('fastest')
color = ["blue", "orange"]

t.pencolor('blue')
for i in range (115):
    t.left(180)
    t.forward(115)
    t.left(65)
    t.backward(115)

t.penup()
t.right(90)
t.forward(50)
t.pendown()
t.pencolor('orange')

for i in range (150):
    t.left(180)
    t.forward(115)
    t.left(65)
    t.backward(115)

t.penup()
t.right(270)
t.forward(22)
t.left(90)
t.forward(70)
t.pendown()
t.pencolor('blue')

for i in range (150):
    t.left(180)
    t.forward(115)
    t.left(65)
    t.backward(115)

t.penup()
t.forward(54)
t.right(75)
t.forward(7)
t.pendown()
t.pencolor('orange')

for i in range (150):
    t.left(180)
    t.forward(115)
    t.left(65)
    t.backward(115)

t. color('white')
turtle.mainloop()