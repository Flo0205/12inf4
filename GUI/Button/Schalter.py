# Import von TkInter
from tkinter import *

class Ampel(object):
    def __init__(self, fenster):
        self.status = 1

        # Button
        button = Button(fenster, text="Schalten", command=self.changeColor)
        button.grid(column=1, row=1, sticky=E)

        # Rot
        self.labelA = Label(fenster, bg="red", fg="red", width="5")
        self.labelA.grid(column=0, row=0)

        # Gelb
        self.labelB = Label(fenster, bg="gray", fg="yellow", width="5")
        self.labelB.grid(column=0, row=1)

        # Grün
        self.labelC = Label(fenster, bg="gray", fg="green", width="5")
        self.labelC.grid(column=0, row=2)
    
    def changeColor(self):
        # Wenn Rot
        if self.status == 1:
            self.labelB.configure(bg="yellow")
            self.status = 2

        # Wenn Rot-Gelb
        elif self.status == 2:
            self.labelA.configure(bg="gray")
            self.labelB.configure(bg="gray")
            self.labelC.configure(bg="green")
            self.status = 3

        # Wenn Grün
        elif self.status == 3:
            self.labelB.configure(bg="yellow")
            self.labelC.configure(bg="gray")
            self.status = 4
            
        # Wenn Gelb
        elif self.status == 4:
            self.labelA.configure(bg="red")
            self.labelB.configure(bg="gray")
            self.status = 1



fenster = Tk()
fenster.geometry("250x100")

Ampel(fenster)

fenster.mainloop()
