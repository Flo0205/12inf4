from tkinter import *

class AmpelObject(object):
    def __init__(self, fenster: Tk, x: int, y: int, state: list[bool], activeAt: int):
        frameAmpel = Frame(master=fenster, background='darkgray')
        frameAmpel.place(x=x, y=y, width=40, height=100)

        self.activeAt = activeAt
        self.state = state
        self.currentStatus = 1

        self.labelRot = Label(master=frameAmpel, background='gray')
        self.labelRot.place(x=10, y=10, width=20, height=20)
        
        self.labelGelb = Label(master=frameAmpel, background='gray')
        self.labelGelb.place(x=10, y=40, width=20, height=20)

        self.labelGruen = Label(master=frameAmpel, background='gray')
        self.labelGruen.place(x=10, y=70, width=20, height=20)

    def update(self):
        if self.activeAt == self.currentStatus:
            self.turnOn()
        else:
            self.labelRot.configure(background='gray')
            self.labelGelb.configure(background='gray')
            self.labelGruen.configure(background='gray')

        self.currentStatus += 1
        if self.currentStatus == 5:
            self.currentStatus = 1
            
    def turnOn(self):
        if self.state[0]:
            self.labelRot.configure(background='red')
        if self.state[1]:
            self.labelGelb.configure(background='yellow')
        if self.state[2]:
            self.labelGruen.configure(background='green')
            
        

fenster = Tk()
fenster.title("Ampel")
fenster.geometry("380x180")

a1 = AmpelObject(fenster, 80,  20, [True, False, False], 1)
a2 = AmpelObject(fenster, 140, 20, [True, True, False],  2)
a3 = AmpelObject(fenster, 200, 20, [False, False, True], 3)
a4 = AmpelObject(fenster, 260, 20, [False, True, False], 4)

status = 1
def schalten():
    a1.update()
    a2.update()
    a3.update()
    a4.update()


button = Button(fenster, text="Schalten", command=schalten)
button.place(x=140, y=140, width=100)

fenster.mainloop()
