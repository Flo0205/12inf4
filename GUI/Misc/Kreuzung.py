from tkinter import *

class Ampel(object):
    def __init__(self, parent: Tk, x: int, y: int, state: list[bool]):
        frameAmpel = Frame(master=parent, background='darkgray')
        frameAmpel.place(x=x, y=y, width=40, height=100)


        if state[0]:
            self._labelRot = Label(master=frameAmpel, background='red')
        else:
            self._labelRot = Label(master=frameAmpel, background='gray')
        self._labelRot.place(x=10, y=10, width=20, height=20)

        if state[1]:
            self._labelGelb = Label(master=frameAmpel, background='yellow')
        else:
            self._labelGelb = Label(master=frameAmpel, background='gray')
        self._labelGelb.place(x=10, y=40, width=20, height=20)

        if state[2]:
            self._labelGruen = Label(master=frameAmpel, background='green')
        else:
            self._labelGruen = Label(master=frameAmpel, background='gray')
        self._labelGruen.place(x=10, y=70, width=20, height=20)

    def update(self, state: list[bool]):
        if state[0]:
            self._labelRot.configure(bg='red')
        else:
            self._labelRot.configure(bg='gray')

        if state[1]:
            self._labelGelb.configure(bg='yellow')
        else:
            self._labelGelb.configure(bg='gray')

        if state[2]:
            self._labelGruen.configure(bg='green')
        else:
            self._labelGruen.configure(bg='gray')

class Kreuzung(object):
    def __init__(self, parent: Tk) -> None:
        self._ampel1 = Ampel(parent, 80, 20, [True, False, False])
        self._ampel2 = Ampel(parent, 20, 140, [False, False, True])
        self._ampel3 = Ampel(parent, 140, 140, [False, False, True])
        self._ampel4 = Ampel(parent, 80, 260, [True, False, False])

        self._button = Button(parent, text="Schalten", command=self.schalten)
        self._button.place(x=70, y=180, width=60, height=20)
        self._button.focus()

        self._state = 1

    def schalten(self):
        self._state += 1
        if self._state == 9:
            self._state = 1

        # 1: Rot  - Grün - Grün - Rot
        # 2: Rot  - Gelb - Gelb - Rot
        # 3: Rot  - Rot  - Rot  - Rot
        # 4: RG   - Rot  - Rot  - RG
        # 5: Grün - Rot  - Rot  - Grün
        # 6: Gelb - Rot  - Rot  - Gelb
        # 7: Rot  - Rot  - Rot  - Rot
        # 8: Rot  - RG   - RG   - Rot
        if self._state == 1:
            self._ampel2.update([False, False, True])
            self._ampel3.update([False, False, True])
        elif self._state == 2:
            self._ampel2.update([False, True, False])
            self._ampel3.update([False, True, False])
        elif self._state == 3:
            self._ampel2.update([True, False, False])
            self._ampel3.update([True, False, False])
        elif self._state == 4:
            self._ampel1.update([True, True, False])
            self._ampel4.update([True, True, False])
        elif self._state == 5:
            self._ampel1.update([False, False, True])
            self._ampel4.update([False, False, True])
        elif self._state == 6:
            self._ampel1.update([False, True, False])
            self._ampel4.update([False, True, False])
        elif self._state == 7:
            self._ampel1.update([True, False, False])
            self._ampel4.update([True, False, False])
        elif self._state == 8:
            self._ampel2.update([True, True, False])
            self._ampel3.update([True, True, False])



fenster = Tk()
fenster.geometry("200x380")

k = Kreuzung(fenster)

fenster.mainloop()

