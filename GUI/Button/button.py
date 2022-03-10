from tkinter import *

def changeColor():
    labelA.configure(bg="yellow")

fenster = Tk()
fenster.geometry("250x100")

labelA = Label(fenster, text="Color", bg="blue", fg="red")
buttonB = Button(fenster, text="Click to change color", command=changeColor)

labelA.pack(side=LEFT)
buttonB.pack(side=RIGHT)

fenster.mainloop()
