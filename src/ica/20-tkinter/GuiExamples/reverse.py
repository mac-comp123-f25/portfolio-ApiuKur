import tkinter as tk
import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.geometry("400x200")
        self.label1=tk.Label(self.mainWin)
        self.label1["text"]="label1"
        self.label1["bg"]="#DD10C1"
        self.label1.grid(row=0,column=0)

        self.label2 = tk.Label(self.mainWin)
        self.label2["text"] = "label2"
        self.label2["bg"] = "#DD10C1"
        self.label2.grid(row=1,column=0)
        self.entry=tk.Entry(self.mainWin)
        self.entry["text"] = "entry1"
        self.entry["bg"] = "#DD10C1"
        self.entry.grid(row=2,column=0)
        self.entry.bind("<Return>",self.entry_response)

    def run(self):
        self.mainWin.mainloop()
    def entry_response(self,event):
        new_entry=self.entry.get()
        reversed_string=new_entry[::-1]
        self.entry.delete(0,tk.END)
        self.entry.insert(0,reversed_string)







# ----- Main program -----
myGui = BasicGui()
myGui.run()