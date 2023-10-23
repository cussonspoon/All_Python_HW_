from tkinter import *
import tkinter.messagebox

#Question 1
class Phone:
    def __init__(self):
        window = Tk()
        window.title("KMITL Phone")
        self.text = ""
        self.display = Label(window, text = self.text, width= 20, height= 5)
        self.display.grid(row=0, column=0, columnspan=3, sticky= W)

        self.num1 = Button(window, text = "1", width = 4, command =lambda: self.pushnumber(str(1)))
        self.num1.grid(column = 1, row = 1)

        self.num2 = Button(window, text = "2",width = 4, command =lambda: self.pushnumber(str(2)))
        self.num2.grid(column = 2, row = 1)

        self.num3 = Button(window, text = "3",width = 4, command =lambda: self.pushnumber(str(3)))
        self.num3.grid(column = 3, row = 1)

        self.num4 = Button(window, text = "4",width = 4, command =lambda: self.pushnumber(str(4)))
        self.num4.grid(column = 1, row = 2)

        self.num5 = Button(window, text = "5",width = 4, command =lambda: self.pushnumber(str(5)))
        self.num5.grid(column = 2, row = 2)

        self.num6 = Button(window, text = "6",width = 4, command =lambda: self.pushnumber(str(6)))
        self.num6.grid(column = 3, row = 2)
        
        self.num7 = Button(window, text = "7",width = 4, command =lambda: self.pushnumber(str(7)))
        self.num7.grid(column = 1, row = 3)
        
        self.num8 = Button(window, text = "8",width = 4, command =lambda: self.pushnumber(str(8)))
        self.num8.grid(column = 2, row = 3)

        self.num9 = Button(window, text = "9",width = 4, command =lambda: self.pushnumber(str(9)))
        self.num9.grid(column = 3, row = 3)

        
        self.ast = Button(window, text = "*",width = 4, command =lambda: self.pushnumber("*"))
        self.ast.grid(column = 1, row = 4)

        self.num0 = Button(window, text = "0",width = 4, command =lambda: self.pushnumber(str(0)))
        self.num0.grid(column = 2, row = 4)

        self.sharp = Button(window, text = "#",width = 4, command =lambda: self.pushnumber("#"))
        self.sharp.grid(column = 3, row = 4)

        self.talk_button = Button(window, text = "Talk", width = 8, command =lambda: self.talk())
        self.talk_button.grid(columnspan= 2 , column = 1, row = 5)

        self.backspace_button = Button(window, text = "<", width = 8, command = lambda: self.backspace())
        self.backspace_button.grid(column = 3, row = 5)


        window.mainloop()
    def pushnumber(self, num = ""):
        self.text += num
        self.display.config(text = self.text)
    def talk(self):
        tkinter.messagebox.showinfo("Calling...", "Dialing " + "<<" + self.text + ">>")
    def backspace(self):
        if len(self.text) != 0:
            self.text = self.text[:-1]
            self.display.config(text=self.text)
                

Phone()

#Question 2
class System:
    def __init__(self):
        window = Tk()
        window.title("System status display")
        self.canvas = Canvas(window, width=1000, height=500)
        self.canvas.pack()


        menubar = Menu(window)
        window.config(menu=menubar)


        options_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=options_menu)


        options_menu.add_command(label="Overall", command=self.display_overall)
        options_menu.add_command(label="CPU", command=self.display_cpu)
        options_menu.add_command(label="Memory", command=self.display_memory)
        options_menu.add_command(label="Network", command=self.display_network)
        options_menu.add_command(label="Process", command=self.display_process)
        options_menu.add_command(label="Disk", command=self.display_disk)
        options_menu.add_command(label="Temperature", command=self.display_temperature)
        options_menu.add_command(label="Battery", command=self.display_battery)

        self.display_overall()

        window.mainloop()

    def clear_canvas(self):
        self.canvas.delete("all")

    def display_overall(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Overall Page Content")

    def display_cpu(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="CPU Page Content")

    def display_memory(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Memory Page Content")

    def display_network(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Network Page Content")

    def display_process(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Process Page Content")

    def display_disk(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Disk Page Content")

    def display_temperature(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Temperature Page Content")

    def display_battery(self):
        self.clear_canvas()
        self.canvas.create_text(500, 250, text="Battery Page Content")

System()
import random
#Question 3
class Bob:
    def __init__(self):
        window = Tk()
        window.title("Aim trainer")
        self.canva = Canvas(width= 1000, height= 500)
        self.canva.bind("<Button-1>", self.drawcircle)
        self.canva.bind("<Button-3>", self.removecircle)
        self.canva.pack()
        window.mainloop()
    def drawcircle(self, event):
        color = ["red", "green", "black", "white", "purple", "pink", "blue", "grey", "orange", "yellow"]
        x, y = event.x, event.y
        self.canva.create_oval(x-20, y-20, x+50, y+50, outline= "black", fill= random.choice(color))

    def removecircle(self, event):
        x, y = event.x, event.y
        items = self.canva.find_overlapping(x - 20, y - 20, x + 50, y + 50)
        self.canva.delete(items)

Bob()