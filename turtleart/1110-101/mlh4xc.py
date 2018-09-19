import turtle

def circle(size, color):
    t.color("black", color)
    t.begin_fill()
    for i in range(360):
        t.forward(size)
        t.right(1)
    t.end_fill()

def tricircle(c1, c2, c3):
    circle(3, c1)
    circle(2, c2)
    circle(1, c3)
    t.right(60)

r1 = ["red", "orange", "yellow"]
r2 = ["#00FF00", "blue", "#8000FF"]

t=turtle.Turtle()
t.speed('fastest')
t.shape('turtle')
t.right(180)


for i in range(3):
    tricircle(r1[0],r1[1],r1[2])
    tricircle(r2[0],r2[1],r2[2])
    
t.color('white')
turtle.mainloop()