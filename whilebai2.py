# dung thu vien turtle
import turtle
import math
import random as r
# tao man hinh ve
screen = turtle.Screen()
screen.setup(500,500)

t = turtle.Turtle()
# bankinh = int(input("nhap ban kinh: "))
bankinh = 150
turtle.bgcolor("black")
colors = ["red","yellow","green","pink","blue","purple"]
t.hideturtle()
do = 0
i =0
while do<360:
    t.pencolor(r.choice(colors))
    for i in range(2):
        t.circle(bankinh,90)
        t.circle(bankinh/2,90)
    t.right(10)
    do+=10
turtle.done()