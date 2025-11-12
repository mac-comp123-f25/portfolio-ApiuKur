from platform import system

from lsystem import LSystem
import turtle
def draw_koch_curve():
 system = LSystem("F", {"F": "F+F--F+F"})

 instructions = system.generate(4)


 turtle.reset()
 turtle.speed(0)
 turtle.title("Koch Curve (n=4)")

 for cmd in instructions:
        if cmd == "F":
            turtle.forward(5)
        elif cmd == "+":
            turtle.left(60)
        elif cmd == "-":
            turtle.right(60)
def quadratic_Koch_curve():
    system2 = LSystem("F", {"F": "F+F-F-F+F"})
    instructions2 = system2.generate(4)

    for cmd in instructions2:
        if cmd == "F":
            turtle.forward(5)
        elif cmd == "+":
            turtle.left(90)
        elif cmd == "-":
            turtle.right(90)




quadratic_Koch_curve()
#draw_koch_curve()
turtle.done()
turtle.exitonclick()
