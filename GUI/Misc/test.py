from tkinter import *

main = Tk()

def execute():
    text = label["text"]
    text = "Hello\n" + text
    label.config(text=text)

label = Label(main, text="World")
label.place(x=10, y=20)

button = Button(main, command=execute)
button.place(x=10, y=10, height=10, width=30)


main.mainloop()
