
import turtle
import math
win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()# sepal turtle
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle() #petal turtle
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()#center turtle
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()#stamp turtle
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()
"""This code is for the middle flower green petals the sepal turtle"""

def draw_five_petals(turt, radius, centerx, centery):
    turt.up()              # lift the pen
    turt.goto(centerx, centery)  # go to the center provided by input
    turt.down()            # put the pen down
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
"""This is the code for the middle flower that draws the pink petals"""

def draw_five_petals(turt, radius, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
"""This code draws the purple petals of the middle flower centerturtle"""
def draw_four_petals(turt, radius, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

"""This code draws the middle stump yellow in color for the middle flower centerturtle"""
def draw_stamp_petals(turt, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.stamp()

"""THis code drwas the aroon petals for the first flower"""
def draw_four_petals(turt, radius, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

"""This is the purple petlas code for the first flower centerturtle"""
def draw_four_petals(turt, radius, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()


stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(220, 0)
sepalTurtle.down()

for i in range(5):
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)
"""This code draws the maroon petals for the right hand flower turtle petal stump"""
petalTurtle.up()
petalTurtle.goto(220, 0)
petalTurtle.down()
for i in range(5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()


"""This code drws the green outer petals for the last flower sepal turtle"""
centerTurtle.up()
def draw_five_petals(turt, radius, centerx, centery):
    turt.up()              # lift the pen
    turt.goto(centerx, centery)  # go to the center provided by input
    turt.down()            # put the pen down
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
"""This code draws the maroon petals for the last fower flower petalturtle"""
def draw_four_petals(turt, radius, centerx, centery):
            turt.up()
            turt.goto(centerx, centery)
            turt.down()
            turt.begin_fill()
            turt.circle(radius)
            turt.end_fill()


"""This code draws the middle  purple stamp for the last flower by centreturtle"""

def draw_four_petals(turt, radius, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()
"""this code drawss the yeloow stamp for the last fower flower stampturtle"""

def draw_stamp_petals(turt, centerx, centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.stamp()

sepalTurtle.up()
sepalTurtle.goto(-220, 0)
sepalTurtle.down()
for i in range(5):
   sepalTurtle.begin_fill()
   sepalTurtle.circle(50)
   sepalTurtle.end_fill()
   sepalTurtle.left(72)

petalTurtle.up()
petalTurtle.goto(-220, 0)
petalTurtle.down()
for i in range(5):#code that draws the middle pink petals
  petalTurtle.begin_fill()
  petalTurtle.circle(25)
  petalTurtle.end_fill()
  petalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()
draw_five_petals(sepalTurtle,50,0,0)
draw_five_petals(petalTurtle,25,0,0)
draw_five_petals(centerTurtle,15,0,-15)
draw_stamp_petals(stampTurtle,-2,0)
draw_five_petals(sepalTurtle,50,0,-220)
draw_five_petals(petalTurtle,25,0,-220)
draw_four_petals(centerTurtle,15,0,-235)
draw_stamp_petals(stampTurtle,-2,-220)
draw_five_petals(sepalTurtle,50,0,220)
draw_four_petals(centerTurtle,15,0,220)
draw_five_petals(petalTurtle,25,0,220)
draw_stamp_petals(stampTurtle,-2,-220)
win.exitonclick()
