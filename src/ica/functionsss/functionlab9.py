
import turtle
import math
def drawAll():
    win = turtle.Screen()
    win.bgcolor("light sky blue")

    sepalTurtle = turtle.Turtle()  # sepal turtle
    sepalTurtle.speed(0)
    sepalTurtle.color("dark green", "spring green")
    sepalTurtle.hideturtle()

    petalTurtle = turtle.Turtle()  # petal turtle
    petalTurtle.speed(0)
    petalTurtle.color('dark red', 'light coral')
    petalTurtle.hideturtle()

    centerTurtle = turtle.Turtle()  # center turtle
    centerTurtle.speed(0)
    centerTurtle.color('purple4')
    centerTurtle.hideturtle()

    stampTurtle = turtle.Turtle()  # stamp turtle
    stampTurtle.color("gold")
    stampTurtle.speed(0)
    stampTurtle.shape("turtle")
    stampTurtle.hideturtle()

    """middle flower"""
    draw_fivecircles(sepalTurtle, 50, 0, 0)
    draw_fivecircles(petalTurtle, 25, 0, 0)
    """first flower"""
    draw_fivecircles(sepalTurtle, 50, 0, 220)
    draw_fivecircles(petalTurtle, 25, 0, 220)
    """Right flower"""
    draw_fivecircles(sepalTurtle, 50, 220, 0)
    draw_fivecircles(petalTurtle, 25, 220, 0)
    """bottom flower"""
    draw_fivecircles(sepalTurtle, 50, 0, -220)
    draw_fivecircles(petalTurtle, 25, 0, -220)
    """left flower"""
    draw_fivecircles(sepalTurtle, 50, -220, 0)
    draw_fivecircles(petalTurtle, 25, -220, 0)

    draw_center(centerTurtle, 0, -15)
    draw_center(centerTurtle, 0, 205)
    draw_center(centerTurtle, 220, -15)
    draw_center(centerTurtle, 0, -235)
    draw_center(centerTurtle, -220, -15)

    draw_bee(stampTurtle, -2, 0)
    draw_bee(stampTurtle, -2, 220)
    draw_bee(stampTurtle, 218, 0)
    draw_bee(stampTurtle, -2, -220)
    draw_bee(stampTurtle, -222, 0)

    win.exitonclick()


def drawcircle(turt,centerx,centery):
    """In this code above calls the functions that draws the various sections of the flower in the five of them"""


"""This function draws a complete flower and takes in four turles and center x and y"""

def draw_fivecircles(turt,radius,centerx,centery):
    """This code has four turtles that draw the five flowers
    """
    """This code will draw the five circles and placing diffrent variables as parameters"""
    "The function above I have replaced the variables mentioned to variables that are parameters.The input radius gives radius of the circle,center x is the x coodinate and y is the y coodinate and turt is the turtle "
    turt.up()  # TODO: Step 2: start here
    turt.goto(centerx, centery)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

"""The code below drws the purple bee stamp that takes in turt which is turtle,center x which is the xcoodinate and center y which is the y coodinate"""
def draw_bee(turt,centerx,centery):
    turt.up()
    turt.goto(centerx, centery)
    turt.down()
    turt.stamp()
def draw_center(turt,centerx,centery):
    turt.up()
    turt.up()
    turt.goto(centerx, centery)
    turt.down()

    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()
drawAll()




