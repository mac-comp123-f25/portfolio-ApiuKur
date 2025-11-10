import random
import turtle

screen=turtle.Screen()
screen.bgcolor("purple")
screen.setup(width=800, height=600)
turtle1=turtle.Turtle()
turtle2=turtle.Turtle()
turtle3=turtle.Turtle()
turtle4=turtle.Turtle()
#turtle speeds
# turtle speeds
turtle1.speed(0)
turtle2.speed(0)
turtle3.speed(0)
turtle4.speed(0)
#turtle colors
turtle1.color("red")

turtle1.pendown()
turtle2.color("yellow")
turtle2.pendown()

turtle3.color("black")
turtle3.pendown()

turtle4.color("pink")

turtle_list =[turtle1, turtle2, turtle3, turtle4]
colors = "red", "blue", "yellow", "pink", "maroon"
colorzz = random.choice(colors)
choice_of_turtles = random.choice(turtle_list)





finish_x = 300
line = turtle.Turtle(visible=False)
line.penup()
line.goto(finish_x, 200)
line.right(90)
line.pendown()
line.forward(400)

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
