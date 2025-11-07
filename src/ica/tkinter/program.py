# ------------------ First section: import statements -----------------
"""import tkinter as tk


# ------------------ Second section: class and methods ----------------

class BasicGui:

    def __init__(self):
        self.rootWin = tk.Tk()

    def run(self):
        self.rootWin.mainloop()


# ------------------ Third section: main program ----------------------

myGui = BasicGui()
myGui.run()"""
import tkinter as tk
from tkinter import ttk

class BasicGui:
    def __init__(self):
        self.rootWin=tk.Tk()
        testLabel = tk.Label(self.rootWin)
        self.newLabel=tk.Label(self.rootWin)
        testButton = tk.Button(self.rootWin)
        quitbutton = tk.Button(self.rootWin)
        testLabel.config(text="Hello world!",
                         font="Arial 18 bold",
                         bg="#DD10C1",
                         relief=tk.RIDGE)
        testLabel.grid(row=0, column=0)

        testButton["text"] = "Next Number"
        testButton["font"] = "Arial 12"
        testButton["bg"] = "#997711"
        testButton["fg"] = "blue"
        testButton["command"]=self.testButtonResponse


        testButton.grid(row=1, column=0)






        quitbutton["text"] = "quit"
        quitbutton["font"] = "Arial 12"
        quitbutton.grid(row=2,column=0)
        quitbutton["command"]=self.destroybutton
        self.testentry=tk.Entry(self.rootWin,bg="white",
                           bd=5,
                           font="Times 12",
                           justify=tk.CENTER,
                           relief=tk.GROOVE,width=40)
        self.testentry.grid(row=2, column=2)
        self.testentry.bind("<Return>", self.testButtonResponse)

        self.newLabel["text"]="0"
        txt= self.newLabel["text"]
        num = int(txt)
        self.newLabel["text"] = str(num + 1)
        self.newLabel.grid(row=3, column=0)





        self.rootWin.title("First example")
        self.rootWin.config(bg="blue")

        self.testentry.bind("<Return>", self.testButtonResponse)
    def run(self):
        self.rootWin.mainloop()
    def testButtonResponse(self,event=None):
        print("clicked")
        text=self.newLabel["text"]
        num=int(text)
        self.newLabel["text"]=num+1
    def destroybutton(self):
        #self.rootWin.destroy()
        txt=self.testentry.get()
        self.newLabel["text"]=txt

    def entryResponse(self, event):
        if event.keysm=="Return":
             print("return pressed")
        elif event.keysm=="Tab"  :
            print("tab pressed")
        txt=self.testentry.get()
        revtext=txt[::1]
        self.testentry.delete(0,tk.END)
        self.testentry.insert(0,revtext)






myGui = BasicGui()
myGui.run()


class FrameExample:
    def __init__(self):
        self.rootWin=tk.Tk
        self.rootWin.title("Frame example")
        f1=tk.Frame(self.rootWin,bg="lightblue", bd=5,
                      relief=tk.SUNKEN, padx = 10, pady = 10)
        f1.grid(row=1,column=2)
        self.frame1Buttons = []
        self.frame2Buttons = []
        for i in range(3):
            bName = "F1 Button" + str(i)
            button = ttk.Button(f1, text=bName)  # font="Arial 14")
            button.grid(row=i, column=1, padx=10, pady=10)
            self.frame1Buttons.append(button)
        for i in range(3):
            bName = "F2 Button" + str(i)
            button = ttk.Button(f2, text=bName)  # font="Arial 14")
            button.grid(row=1, column=i, padx=10, pady=10)
            self.frame2Buttons.append(button)

    def run(self):
        self.rootWin.mainloop(self)

    # Main program:
frameGui = FrameExample()
frameGui.run()









