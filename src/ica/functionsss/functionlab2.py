
import turtle
import math
"""This code has four turtles that draw the five flowers
"""
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
"""This code draws the circle in the middle and starts drawing the green outer circle"""
sepalTurtle.up()                    # TODO: Step 2: start here
sepalTurtle.goto(0, 0)
sepalTurtle.down()
for i in range(5):
   sepalTurtle.begin_fill()
   sepalTurtle.circle(50)
   sepalTurtle.end_fill()
   sepalTurtle.left(72)
"""This code draws the middle maroon circle"""
petalTurtle.up()
petalTurtle.goto(0, 0)
petalTurtle.down()
for i in range(5):
   petalTurtle.begin_fill()
   petalTurtle.circle(25)
   petalTurtle.end_fill()
   petalTurtle.left(72)
"""This code draws the purple circle"""
centerTurtle.up()
centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()

centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()
"""This code draws the yellow stamp of the middle circle"""
stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()
"""The middle circle ends here"""

"""This code draws the upper circle"""
sepalTurtle.up()
sepalTurtle.goto(0, 220)
sepalTurtle.down()

#draws the outer green petals
for i in range(5):
   sepalTurtle.begin_fill()
   sepalTurtle.circle(50)
   sepalTurtle.end_fill()
   sepalTurtle.left(72)

petalTurtle.up()
petalTurtle.goto(0, 220)
petalTurtle.down()

for i in range(5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()
"""circle1ends here"""
"""This code draws the circle in the right side"""
centerTurtle.up()
sepalTurtle.up()
sepalTurtle.goto(220, 0)
sepalTurtle.down()

for i in range(5):
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)

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

"""The right circle ends here"""

"""This code draws the bottom circle"""

sepalTurtle.up()
sepalTurtle.goto(0, -220)
sepalTurtle.down()
for i in range(5):
   sepalTurtle.begin_fill()
   sepalTurtle.circle(50)
   sepalTurtle.end_fill()
   sepalTurtle.left(72)

petalTurtle.up()
petalTurtle.goto(0, -220)
petalTurtle.down()
for i in range(5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

"""The bottom circle ends here"""

"""This last code draws the left circle"""

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




win.exitonclick()
