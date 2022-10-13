# dung thu vien turtle
import turtle
import math
# tao man hinh ve
screen = turtle.Screen()
screen.setup(500,500)

t = turtle.Turtle()

khoangcach = int(input("nhap khoang cach xoan oc: "))
d = 0
while turtle.distance(t) < khoangcach:
    t.fd(d)
    t.left(5)
    d += 0.01

turtle.done()