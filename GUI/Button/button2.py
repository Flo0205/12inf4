from tkinter import *

def changeColorA():
    labelA.configure(bg="red")

def changeColorB():
    labelB.configure(bg="yellow")

def changeColorC():
    labelC.configure(bg="green")

fenster = Tk()
fenster.geometry("250x100")


# Rot
labelA = Label(fenster, text="Red", bg="gray", fg="red")
buttonA = Button(fenster, text="A", command=changeColorA)
labelA.grid(column=0, row=0)
buttonA.grid(column=1, row=0)

# Gelb
labelB = Label(fenster, text="Yellow", bg="gray", fg="yellow")
buttonB = Button(fenster, text="B", command=changeColorB)
labelB.grid(column=0, row=1)
buttonB.grid(column=1, row=1)

# Grün
labelC = Label(fenster, text="Green", bg="gray", fg="green")
buttonC = Button(fenster, text="C", command=changeColorC)
labelC.grid(column=0, row=2)
buttonC.grid(column=1, row=2)


fenster.mainloop()
