import turtle
#wn=turtle.Screen()
#alex=turtle.Turtle()
#alex.forward(150)
#alex.left(90)
#alex.forward(75)
import turtle

import turtle
"""wn=turtle.Screen()
alex = turtle.Turtle()
for i in ["yellow","red","blue","green","purple"]:
    alex.color(i)
    alex.forward(50)
    alex.left(90)



wn.exitonclick()"""
def drawRectangle(t,w,h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawsquare(tx,sz):
    drawRectangle(tx,sz,sz)
wn=turtle.Screen()
wn.bgcolor("black")
tess=turtle.Turtle()
tess.color("white")
drawsquare(tess,100)
drawRectangle(tess,150,10)
wn.exitonclick()






