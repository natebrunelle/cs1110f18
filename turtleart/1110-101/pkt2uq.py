#  This program will make the illuminati eye
import turtle
eye = turtle.Turtle()
eye.color('green')
eye.begin_fill()
eye.penup()
eye.setposition(-200,-200)
eye.pendown()
eye.forward(450)
eye.left(120)
eye.forward(450)
eye.left(120)
eye.forward(450)
eye.end_fill()
eye.color('black')
eye.penup()
eye.left(180)
eye.forward(225)
eye.pendown()
eye.begin_fill()
eye.right(130)
eye.circle(120,140)
eye.left(70)
eye.circle(180,80)
eye.end_fill()



turtle.mainloop()


