from tkinter import *
from tkinter import messagebox

class Currency:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")

        self.num = StringVar()
        entry1 = Entry(window, textvariable=self.num)
        entry1.pack()

        Button1 = Button(window, text="USD -> THB", command=self.convert1)
        Button1.pack()

        Button2 = Button(window, text = "THB -> USD", command = self.convert2)
        Button2.pack()

        window.mainloop()

    def convert1(self):
        usd = float(self.num.get())
        converted1 = usd*30
        messagebox.showinfo("USD -> THB", f"{usd} USD is {converted1:.2f} THB")
    def convert2(self):
        bht = float(self.num.get())
        converted2 = bht/30
        messagebox.showinfo("THB -> USD", f"{bht} BHT is {converted2:.2f} USB")

Currency()
