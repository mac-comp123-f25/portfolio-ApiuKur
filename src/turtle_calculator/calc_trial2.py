import turtle
import tkinter as tk
root=tk.Tk()
root.geometry("400x450")
main_frame=tk.Frame(root)#main frame where the canvas and the buttons are attached
main_frame.pack()
root.title("turtle calculator")
canvas=tk.Canvas(main_frame,width=400,height=400)
canvas.pack(in_=main_frame, side="left", padx=10)#attach the canvas to main frame
#attaching the turtle screen to canvas
win=turtle.TurtleScreen(canvas)
#the display turtle
display_turtle = turtle.RawTurtle(win)
display_turtle.hideturtle()
display_turtle.penup()
display_turtle.speed(0)
win.bgcolor("purple")
current_expression=" "

current_expression=eval(current_expression)
def  update_display():
    display_turtle.clear()
    display_turtle.goto(-150,150)
    display_turtle.write(current_expression,font=("Arial", 24, "bold"))
def button_click(value):
    global current_expression

    if value == "AC":
        current_expression = ""          # Clear the screen
    elif value == "=":
        current_expression = str(eval(current_expression))  # Calculate result
    else:
        current_expression += value      # Add number or operator

    update_display()                     # Refresh the display



def add(a,b):
    result=int(a+b)
    return result
def subtract(a,b):
    result1 = int(a - b)
    return result1
def multiply(a,b):
    result2 = int(a * b)
    return result2
def division(a,b):
    result3 = int(a / b)
    return result3


row1_frame=tk.Frame(main_frame)
row1_frame.pack(in_=main_frame,pady = 20,side="left",padx=80)


#tk.Label(key1_frame, text="Calculator").grid(row=0, column=0)
tk.Button(row1_frame, text="2", width=10
, command=lambda :("2")).grid(row=0, column=1,pady=10)
tk.Button(row1_frame, text="AC", width=10
, command=lambda :("AC")).grid(row=0, column=2,pady=10)
tk.Button(row1_frame, text="3", width=10
, command=lambda :("3")).grid(row=0, column=3,pady=10)
tk.Button(row1_frame, text="=", width=10
, command=lambda :button_click("=")).grid(row=0, column=4,pady=10)
#row 2 frame
#holds the values for the calculator


#tk.Label(row2_frame, text="Calculator").grid(row=1, column=0)
"""tk.Button(row1_frame, text="7", width=10
, command=calculator).grid(row=1, column=1,pady=10)
tk.Button(row1_frame, text="8", width=10
, command=calculator).grid(row=1, column=2,pady=10)
tk.Button(row1_frame, text="9", width=10
, command=calculator).grid(row=1, column=3,pady=10)
tk.Button(row1_frame, text="x", width=10
, command=calculator).grid(row=1, column=4,pady=10)"""
#row three frame

#tk.Label(row3_frame, text="Calculator").grid(row=1, column=0)
"""tk.Button(row1_frame, text="4", width=10
, command=calculator).grid(row=2, column=1,pady=10)
tk.Button(row1_frame, text="5", width=10
, command=calculator).grid(row=2, column=2,pady=10)
tk.Button(row1_frame, text="6", width=10
, command=calculator).grid(row=2, column=3,pady=10)
tk.Button(row1_frame, text="-", width=10
, command=calculator).grid(row=2, column=4,pady=10)"""

#row four frame

#tk.Label(row4_frame, text="Calculator").grid(row=1, column=0)
"""tk.Button(row1_frame, text="1", width=10
, command=calculator).grid(row=3, column=1,pady=10)
tk.Button(row1_frame, text="2", width=10
, command=calculator).grid(row=3, column=2,pady=10)
tk.Button(row1_frame, text="3", width=10
, command=calculator).grid(row=3, column=3,pady=10)
tk.Button(row1_frame, text="+", width=10
, command=calculator).grid(row=3, column=4,pady=10)"""

#row five frame

#tk.Label(row4_frame, text="Calculator").grid(row=1, column=0)
"""tk.Button(row1_frame, text="0", width=10
, command=calculator,bg="lightblue").grid(row=4, column=1,pady=10)
tk.Button(row1_frame, text=".", width=10
, command=calculator).grid(row=4, column=2,pady=10)
tk.Button(row1_frame, text="=", width=10
, command=calculator).grid(row=4, column=3)"""


win.mainloop()