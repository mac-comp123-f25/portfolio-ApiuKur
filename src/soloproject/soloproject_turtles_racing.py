import random
import turtle
#truck drawer

start_x = -300
truck_drawer=turtle.Turtle(visible=False)
truck_drawer.color("yellow")
#truck_drawer.hideturtle()
truck_drawer.penup()
truck_drawer.goto(start_x, 350)
truck_drawer.right(90)
truck_drawer.pendown()
truck_drawer.forward(600)

#turtle title
title_writer = turtle.Turtle(visible=False)
title_writer.penup()
title_writer.goto(0, 270)
title_writer.color("white")
title_writer.write("THE GREAT TURTLE RACE", align="center", font=("Arial", 24, "bold"))
screen=turtle.Screen()
screen.addshape("_-ezgif.com-resize.gif")
screen.bgcolor("purple")
screen.setup(width=500, height=600)
turtle1=turtle.Turtle()
screen.title("THE GREAT TURTLE RACE")

turtle1.shape("_-ezgif.com-resize.gif")
turtle1.turtlesize(stretch_wid=0.5, stretch_len=0.5)
turtle1.penup()
turtle1.goto(-300,50)

turtle2=turtle.Turtle()
turtle2.shape("_-ezgif.com-resize.gif")
turtle2.turtlesize(stretch_wid=0.5, stretch_len=0.5)
turtle2.penup()
turtle2.goto(-300,100)


turtle3=turtle.Turtle()
turtle3.shape("_-ezgif.com-resize.gif")
turtle3.turtlesize(stretch_wid=0.5, stretch_len=0.5)
turtle3.penup()
turtle3.goto(-300,150)

turtle4=turtle.Turtle()
turtle4.shape("_-ezgif.com-resize.gif")
turtle4.turtlesize(stretch_wid=0.5, stretch_len=0.5)
turtle4.penup()
turtle4.goto(-300,200)
#turtle speeds
# turtle speeds
turtle1.speed(0)
turtle2.speed(0)
turtle3.speed(0)
turtle4.speed(0)
#turtle colors
turtle1.color("red")

#turtle1.pendown()
turtle2.color("yellow")
#turtle2.pendown()

turtle3.color("black")
#turtle3.pendown()

turtle4.color("pink")

turtle_list =[turtle1, turtle2, turtle3, turtle4]
colors = "red", "blue", "yellow", "pink", "maroon"
colorzz = random.choice(colors)
choice_of_turtles = random.choice(turtle_list)

finish_x = 300
line = turtle.Turtle(visible=False)
line.color("yellow")
line.penup()
line.goto(finish_x, 350)
line.right(90)
line.pendown()
line.forward(600)

def turtle_race(turtle_list, finish_x):
    racing = True
    winner = None
    while racing==True:
        for t in turtle_list:
            step = random.randint(1, 10)
            t.forward(step)
            if t.xcor() >= finish_x:
                winner = t.pencolor()
                racing = False
                break

    return winner





print(turtle_race(turtle_list,finish_x))
screen.exitonclick()
