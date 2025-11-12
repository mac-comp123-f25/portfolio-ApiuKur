import turtle
def drawSquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn=turtle.Screen()
wn.bgcolor("lightblue")
alex=turtle.Turtle()
drawSquare(alex,50)

alex.penup()
alex.goto(100,100)
alex.pendown()
drawSquare(alex,75)
wn.exitonclick()




