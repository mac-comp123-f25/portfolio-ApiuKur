"""myCanvas = tk.Canvas(self.rootWin)

myCanvas["width"] = 400
myCanvas["height"] = 300
myCanvas["bg"] = "pink"
myCanvas["bd"] = 5
#myCanvas["relief"] = tk.SUNKEN
#myCanvas.grid(row=10, column=0)"""
import tkinter as tk

import tkinter as tk

class BasicGui:
    def __init__(self):
        self.rootWin = tk.Tk()

        # Create canvas as part of the class
        self.myCanvas = tk.Canvas(self.rootWin)
        self.myCanvas["width"] = 400
        self.myCanvas["height"] = 300
        self.myCanvas["bg"] = "pink"
        self.myCanvas["bd"] = 5
        self.myCanvas["relief"] = tk.SUNKEN
        self.myCanvas.grid(row=10, column=0)

        self.rootWin.title("Canvas Example")
        l1 = self.myCanvas.create_line(50, 50, 50, 100, fill="blue")
        r1=self.myCanvas.create_rectangle(10,20,30,40)

    def run(self):
        self.rootWin.mainloop()

myGui = BasicGui()
myGui.run()

