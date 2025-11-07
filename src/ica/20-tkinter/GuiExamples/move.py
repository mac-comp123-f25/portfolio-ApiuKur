import tkinter as tk


# ------------------ Second section: class and methods ----------------

class BasicGui:

    def __init__(self):
        self.rootWin = tk.Tk()
        self.mycanvas=tk.Canvas(self.rootWin)
        self.mycanvas["width"]=400
        self.mycanvas["height"]=300
        self.mycanvas["bg"] = "yellow"
        self.mycanvas["bd"] = 5
        self.mycanvas["relief"] = tk.SUNKEN
        self.mycanvas.grid(row=10, column=0)
        tittle=self.mycanvas.create_text(50,40,text="Mycanvas",fill="darkblue",font=("Arial", 16, "bold"))
        self.my_name=self.mycanvas.create_text(60,60,text="Daai",fill="blue",font=("Arial"))
        self.rootWin.bind("<Return>", self.move_callback)
        self.rootWin.bind("<w>", self.move_callback)
        self.rootWin.bind("<a>", self.move_callback)
        self.rootWin.bind("<s>", self.move_callback)
        self.rootWin.bind("<d>", self.move_callback)
        self.rootWin.bind("<Up>", self.move_callback)
        self.rootWin.bind("<Down>", self.move_callback)
        self.rootWin.bind("<Left>", self.move_callback)
        self.rootWin.bind("<Right>", self.move_callback)

        # Force focus to root window
        self.rootWin.focus_set()


    def move_callback(self,event):
       value=event.keysym
       print(value)

       if value=="<w>" or value=="<Up>":
           self.mycanvas.move(self.my_name,20,30)
       elif value=="<d>" or value=="<down>":
           self.mycanvas.move(self.my_name, 50, 80)
       else:
           self.mycanvas.move(self.my_name, 70, 100)














    def run(self):
        self.rootWin.mainloop()


# ------------------ Third section: main program ----------------------

myGui = BasicGui()
myGui.run()
