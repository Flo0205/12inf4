from tkinter import *

class AmpelObject(object):
    def __init__(self, fenster: Tk, x: int, y: int, state: list[bool]):
        frameAmpel = Frame(master=fenster, background='darkgray')
        frameAmpel.place(x=x, y=y, width=40, height=100)


        if state[0]:
            labelRot = Label(master=frameAmpel, background='red')
        else:
            labelRot = Label(master=frameAmpel, background='gray')
        labelRot.place(x=10, y=10, width=20, height=20)

        if state[1]:
            labelGelb = Label(master=frameAmpel, background='yellow')
        else:
            labelGelb = Label(master=frameAmpel, background='gray')
        labelGelb.place(x=10, y=40, width=20, height=20)

        if state[2]:
            labelGruen = Label(master=frameAmpel, background='green')
        else:
            labelGruen = Label(master=frameAmpel, background='gray')
        labelGruen.place(x=10, y=70, width=20, height=20)

fenster = Tk()
fenster.title("Ampel")
fenster.geometry("380x150")

AmpelObject(fenster, 80, 20, [True, False, False])
AmpelObject(fenster, 140, 20, [True, True, False])
AmpelObject(fenster, 200, 20, [False, False, True])
AmpelObject(fenster, 260, 20, [False, True, False])

fenster.mainloop()