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
        testentry=tk.Entry(self.rootWin,bg="pink",
                           bd=5,
                           font="Times 12",
                           justify=tk.CENTER,
                           relief=tk.GROOVE,width=40)
        testentry.grid(row=2, column=2)
        self.newLabel["text"]="0"
        txt= self.newLabel["text"]
        num = int(txt)
        self.newLabel["text"] = str(num + 1)
        self.newLabel.grid(row=3, column=0)





        self.rootWin.title("First example")
        self.rootWin.config(bg="blue")
    def run(self):
        self.rootWin.mainloop()
    def testButtonResponse(self):
        print("clicked")
    def destroybutton(self):
        #self.rootWin.destroy()
        txt=self.testentry.get()
        self.newLabel["text"]=txt



myGui = BasicGui()
myGui.run()







