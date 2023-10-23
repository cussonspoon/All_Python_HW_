from tkinter import *

class Draw:
    def __init__(self):
        window = Tk()
        window.title("A simple paint program")
        self.canvas = Canvas(window, bg="white", width=400, height=400)
        self.canvas.pack(fill=BOTH, expand=True)
        self.pen_color = "black"
        self.canvas.bind("<Button-1>", self.startdraw)
        button1 = Button(window, text="RESET", command=self.reset)
        button1.pack()
        window.mainloop()

    def startdraw(self, event):
        self.x, self.y = event.x, event.y
        self.canvas.bind("<B1-Motion>", self.draw)
    
    def draw(self, event):
        x2, y2 = event.x, event.y
        self.canvas.create_line(self.x, self.y, x2, y2, fill=self.pen_color, width=2)
        self.x, self.y = x2, y2

    def reset(self):
        self.canvas.delete("all")

Draw()
