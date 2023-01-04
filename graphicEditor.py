from turtle import *

# config
speed = 100
brush = Turtle()
brush.color("black")
brush.shape("circle")
brush.width(5)
brush.pendown()
brush.speed(speed)
scr = brush.getscreen()
scr.listen()
#####################



def setRed():
    brush.color("red")
def setGreen():
    brush.color("green")
def setBlue():
    brush.color("blue")
def setYellow():
    brush.color("yellow")
def setBlack():
    brush.color("black")        

def draw(x, y):
    brush.goto(x,y)

def move(x, y):
    brush.penup()
    brush.goto(x,y)
    brush.pendown()

def goUp():
    x = brush.xcor()
    y = brush.ycor()
    brush.goto(x,y+5)
def goDown():
    x = brush.xcor()
    y = brush.ycor()
    brush.goto(x,y-5)
def goLeft():
    x = brush.xcor()
    y = brush.ycor()
    brush.goto(x-5,y)
def goRight():
    x = brush.xcor()
    y = brush.ycor()
    brush.goto(x+5,y)

def begin():
    brush.begin_fill()
def end():
    brush.end_fill()

brush.ondrag(draw)

scr.onscreenclick(move)

#keys
scr.onkey(setRed, 1)
scr.onkey(setGreen, 2)
scr.onkey(setBlue, 3)
scr.onkey(setYellow, 4)
scr.onkey(setBlack, 5)

scr.onkey(goUp, "Up")
scr.onkey(goDown, "Down")
scr.onkey(goLeft, "Left")
scr.onkey(goRight, "Right")

scr.onkey(begin, "b")
scr.onkey(end, "e")

#Coded by filin