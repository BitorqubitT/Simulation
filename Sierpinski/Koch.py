import turtle

def startposition(speed,x,y):
    turtle.speed(speed)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


# Draw a Koch snowflake
from turtle import *

def drawkoch(length, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            drawkoch(length, order-1)
            turtle.left(t)
    else:
        turtle.forward(length)


startposition(10,-200,-200)
drawkoch(15, 1)



window = turtle.Screen()
window.exitonclick()



#make this in pygame!