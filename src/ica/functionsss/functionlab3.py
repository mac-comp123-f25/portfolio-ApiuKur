
import turtle
import math
"""This code has four turtles that draw the five flowers
"""
"""This code will draw the five circles and placing diffrent variables as parameters"""
"The function above I have replaced the variables mentioned to variables that are parameters.The input radius gives radius of the circle,center x is the x coodinate and y is the y coodinate and turt is the turtle "
def draw_fivecircles(turt,radius,centerx,centery):
    turt.up()  # TODO: Step 2: start here
    turt.goto(centerx, centery)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

        def draw_fivecircles(turt, radius, centerx, centery):
            turt.up()  # TODO: Step 2: start here
            turt.goto(centerx, centery)
            turt.down()
            for i in range(5):
                turt.begin_fill()
                turt.circle(radius)
                turt.end_fill()
                turt.left(72)

                def draw_fivecircles(turt, radius, centerx, centery):
                    turt.up()  # TODO: Step 2: start here
                    turt.goto(centerx, centery)
                    turt.down()
                    for i in range(5):
                        turt.begin_fill()
                        turt.circle(radius)
                        turt.end_fill()
                        turt.left(72)

                        def draw_fivecircles(turt, radius, centerx, centery):
                            turt.up()  # TODO: Step 2: start here
                            turt.goto(centerx, centery)
                            turt.down()
                            for i in range(5):
                                turt.begin_fill()
                                turt.circle(radius)
                                turt.end_fill()
                                turt.left(72)

                                """code for the right hand circle sepals"""

                                def draw_fivecircles(turt, radius, centerx, centery):
                                    turt.up()  # TODO: Step 2: start here
                                    turt.goto(centerx, centery)
                                    turt.down()
                                    for i in range(5):
                                        turt.begin_fill()
                                        turt.circle(radius)
                                        turt.end_fill()
                                        turt.left(72)
                                        """code for the red petals right hand side code """
def draw_fivecircles(turt, radius, centerx, centery):
     turt.up()  # TODO: Step 2: start here
     turt.goto(centerx, centery)
     turt.down()
     for i in range(5):
         turt.begin_fill()
         turt.circle(radius)
         turt.end_fill()
         turt.left(72)



def draw_fivecircles(turt, radius, centerx, centery):
                                            turt.up()  # TODO: Step 2: start here
                                            turt.goto(centerx, centery)
                                            turt.down()
                                            for i in range(5):
                                                turt.begin_fill()
                                                turt.circle(radius)
                                                turt.end_fill()
                                                turt.left(72)
"""this code draws the lower pink flower"""


def draw_fivecircles(turt, radius, centerx, centery):
    turt.up()  # TODO: Step 2: start here
    turt.goto(centerx, centery)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
def draw_fivecircles(turt, radius, centerx, centery):
    turt.up()  # TODO: Step 2: start here
    turt.goto(centerx, centery)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)
        """last pink sepal lower flower"""
def draw_fivecircles(turt, radius, centerx, centery):
    turt.up()  # TODO: Step 2: start here
    turt.goto(centerx, centery)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

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
"""this one up is the confused one next to right sepals green"""

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

draw_fivecircles(sepalTurtle,50,0,0)
draw_fivecircles(petalTurtle,25,0,0)
draw_fivecircles(sepalTurtle,50,0,220)
draw_fivecircles(petalTurtle,25,0,220)
draw_fivecircles(sepalTurtle,50,220,0)
draw_fivecircles(petalTurtle,25,220,0)
draw_fivecircles(sepalTurtle,50,0,-220)
draw_fivecircles(petalTurtle,25,0,-220)
draw_fivecircles(sepalTurtle,50,-220,0)
draw_fivecircles(petalTurtle,25,-220,0)



win.exitonclick()
