import time
import turtle
import random

win=turtle.Screen()
win.bgcolor("black")
turt1=turtle.Turtle()
turt2=turtle.Turtle()
turt2.color("brown")
turt3=turtle.Turtle()
turt3.color("red")
turt4=turtle.Turtle()
turt4.color("yellow")
turt5=turtle.Turtle()
turt5.color("red")
turt6=turtle.Turtle()



def draw_rhombus(turt,center,width,color):
 """takes four inputs turt,center,width,color and draws it"""


 turt.color(color)
 turt.penup()
 turt.goto(center[0],center[1])
 turt.pendown()
 for i in range(2):
   turt.begin_fill()
   turt.left(60)
   turt.forward(width)
   turt.left(120)
   turt1.forward(width)
   turt.end_fill()


nmbeoftimes = 50



for z in range(nmbeoftimes):
#draws random rhombus with the defined inputs of color,x and y,width

  x=random.randint(0,100)
  y=random.randint(0,100)















  #draw_rhombus(turt1,center=(x,y),width=random.randint(10,20),color=random.choice(['red','green','blue']))

def draw_hexagon(turtt,length,angle):
  for i in range(6):
    turtt.left(angle)
    turtt.forward(length)
#draw_hexagon(turt2,100,60)

def draw_isoscles(turt,centerx,centery):
    turt.penup()
    turt.goto(centerx,centery)
    turt.pendown()
   #circle
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

    turt.penup()
    turt.goto(150, 150)
    turt.pendown()


    for w in range(6):
        turt.penup()
        turt.goto(random.randint(0,100),random.randint(0,100))


        turt.pendown()

        for i in range(3):
#iscosles triangle
         turt.begin_fill()
         turt.left(150)
         turt.forward(30)
         turt.end_fill()
         turt.hideturtle()




#draw_isoscles(turt3,100,100)
def draw_wheel_animation(turt,radius):



    turt.penup()

    turt.goto(40, 27)
    turt.pendown()

    for i in range(5):
         turt.begin_fill()
         turt.left(144)
         turt.forward(80)
         turt.end_fill()

    turt.penup()
    turt.goto(0, 0)
    turt.pendown()
    turt.circle(radius)

    

draw_wheel_animation(turt3,50)





win.exitonclick()