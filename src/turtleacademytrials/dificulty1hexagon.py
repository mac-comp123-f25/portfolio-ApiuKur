import turtle
win=turtle.Screen()
tt1=turtle.Turtle()
tt1.color("red")

def drawhexagon(turtle,length,angle):

    for i in range(5):
        turtle.forward(length)
        turtle.left(angle)







drawhexagon(tt1,100,72)

def fiveponitedstar(turtle,length,angle):

    for i in range(5):
        turtle.forward(length)
        turtle.left(angle)







fiveponitedstar(tt1,100,144)
win.exitonclick()