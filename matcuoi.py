# dung thu vien turtle
import turtle

# tao man hinh ve
screen = turtle.Screen()
screen.setup(500,500)

#ve mat cuoi
t = turtle.Turtle()

#ve mat
facesize = 200

t.pensize(5)
t.speed(5)
t.fillcolor("yellow")
t.penup()
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.circle(facesize)
t.end_fill()

#ve mat
eyesize = 25
t.fillcolor("black")
t.penup()
t.goto(-100,50)
t.pendown()
t.begin_fill()
t.circle(eyesize)
t.end_fill()

t.penup()
t.goto(100,50)
t.pendown()
t.begin_fill()
t.circle(eyesize)
t.end_fill()

#ve mui
t.penup()
t.goto(0,30)
t.pendown()
t.begin_fill()
t.circle(-30, steps = 3)
t.end_fill()

#ve mieng
t.penup()
t.goto(-100,-70)
t.pendown()
t.right(90)
t.circle(100,180)
t.mainloop()

turtle.done()
