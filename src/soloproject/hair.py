
import turtle
win=turtle.Screen()
def draw_face(color):
    face_turt.penup()
    face_turt.goto(0, 0)
    face_turt.setheading(0)
    face_turt.right(90)
    face_turt.forward(150)
    face_turt.left(90)
    face_turt.pendown()
    face_turt.pencolor(color)
    face_turt.fillcolor(color)
    face_turt.begin_fill()
    for x in range(2):
        face_turt.circle(120, 45)
        face_turt.circle(200, 90)
        face_turt.circle(120, 45)
    face_turt.end_fill()
    face_turt.penup()
    face_turt.goto(0, 0)
    face_turt.pendown()
def draw_hair():
    hair_turtle.pensize(20)
    hair_turtle.hideturtle()
    hair_turtle.penup()
    hair_turtle.goto(65,200)
    hair_turtle.pendown()
    hair_turtle.setheading(310)
    hair_turtle.begin_fill()
    hair_turtle.circle(-410,25)
    #hair_turtle.forward(50)
    hair_turtle.end_fill()

    # left hair
    right_hair.penup()
    right_hair.pensize(20)
    right_hair.hideturtle()
    right_hair.goto(-50,194)
    right_hair.pendown()
    right_hair.begin_fill()
    right_hair.setheading(220)
    right_hair.circle(410,25)
    right_hair.end_fill()
    #center piece
    center_hair.pensize(30)
    center_hair.penup()
    center_hair.hideturtle()
    center_hair.goto(-70, 195)  # moved slightly right from -85 → -70
    center_hair.pendown()
    center_hair.begin_fill()
    center_hair.setheading(5)  # 375 is same as 15°; 350 keeps it tighter
    center_hair.circle(-420, 20)  # slightly longer arc to overlap
    center_hair.end_fill()


face_turt=turtle.Turtle()
hair_turtle=turtle.Turtle()
right_hair=turtle.Turtle()
center_hair=turtle.Turtle()
draw_face("red")
draw_hair()
win.exitonclick()
