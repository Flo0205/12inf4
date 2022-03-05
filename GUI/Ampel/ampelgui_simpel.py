from tkinter import *

fenster = Tk()
fenster.title("Ampel")
fenster.geometry("200x200")

frameAmpel = Frame(master=fenster, background='darkgray')
frameAmpel.place(x=80, y=20, width=40, height=100)

labelRot = Label(master=frameAmpel, background='gray')
labelRot.place(x=10, y=10, width=20, height=20)

labelGelb = Label(master=frameAmpel, background='gray')
labelGelb.place(x=10, y=40, width=20, height=20)

labelGruen = Label(master=frameAmpel, background='gray')
labelGruen.place(x=10, y=70, width=20, height=20)

fenster.mainloop()