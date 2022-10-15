# dung thu vien turtle
import turtle
import math
# tao man hinh ve
screen = turtle.Screen()
screen.setup(500,500)

t = turtle.Turtle()

def vehcn(chieurong, chieudai):
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(chieurong)
        t.right(90)
        t.fd(chieudai)
        t.right(90)
    t.end_fill()

for n in range(4):
    vehcn(50,100)
    t.fd(50)


turtle.done()
