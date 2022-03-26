from tkinter import *

fenster = Tk()
fenster.geometry("700x400")

frame = Frame(master=fenster, bg='gray')
frame.place(x=150, y=50, width=400, height=300)

label = Label(master=frame, text="Label", bg="gray")
label.place(x=170, y=0, width=60, height=30)

button = Button(master=frame, text="Button", command=print)
button.place(x=120, y=135, width=160, height=30)

fenster.mainloop()