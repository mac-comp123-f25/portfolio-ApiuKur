import test
import turtle
#def distance(x1, y1, x2, y2):
   # return 0.0
#test.testEqual(distance(1, 2, 1, 2), 0)


def distance(x1, y1, x2, y2):
    "this function returns the distance between two points"

    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    "This line returns a aquare of the two distances added as squares"
    result = dsquared ** 0.5
    "finds the suareroot of the distance"
    return result

def area(radius):
    "this function returns the area of a circle using radius"
    b = 3.14159 * radius**2
    "returns area of circle by multiplying by 3.14159"
    return b
def area2(xc,yc,xp,yp) :
    radius=distance(xp,yc,xc,yc)
    result=area(radius)
    return result
print(area2(0,0,1,1))



def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)               # Point up
    t.forward(height)        # Draw up the left side
    t.right(90)
    t.forward(40)            # width of bar, along the top
    t.right(90)
    t.forward(height)        # And down again!
    t.left(90)               # put the turtle facing the way we found it.

xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)



for a in xs:
    drawBar(tess, a)

wn.exitonclick()


#print(area2(0,0,1,1))