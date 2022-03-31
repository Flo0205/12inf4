from tkinter import *

def begone():
    button.destroy()

tk = Tk()

button = Button(text="Bye!", command=begone)
button.grid(row=0, column=0)
