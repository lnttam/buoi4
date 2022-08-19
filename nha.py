from copyreg import clear_extension_cache
import turtle
canh = 100
screen = turtle.Screen()
screen.setup(500,500)
t = turtle.Turtle()
t.speed(1)
t.rt(45)
t.circle(-canh,steps = 4)
t.backward(canh)
t.rt(90)
t.fd(canh)
turtle.done()