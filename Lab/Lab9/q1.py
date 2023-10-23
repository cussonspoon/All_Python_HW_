from tkinter import *

class Spinner:
    def __init__(self):
        self.window = Tk()
        self.window.title("Spinner")
        self.num = 0
        self.text = Label(self.window, text = self.num)
        self.text.pack(side = LEFT)
        Button(self.window, text="+", command=self.add).pack()
        Button(self.window, text="-", command=self.sub).pack()
        Button(self.window, text= "RESET", command = self.reset).pack()
        self.window.mainloop()
    def add(self):
        self.num += 1
        self.text.config(text = self.num)
    def sub(self):
        self.num -= 1
        self.text.config(text = self.num)
    def reset(self):
        self.num = 0
        self.text.config(text = self.num)

Spinner()
