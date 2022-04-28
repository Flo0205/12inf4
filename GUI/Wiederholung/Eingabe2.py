from tkinter import *
def buttonVerdoppelnClick():
    zahl = float(entryZahl.get())
    zahl = zahl * 2
    entryZahl.delete(0, 'end')
    entryZahl.insert(0, str(zahl))
tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('120x110')
entryZahl = Entry(master=tkFenster, bg='white')
entryZahl.place(x=45, y=40, width=30, height=30)
buttonVerdoppeln = Button(master=tkFenster, text='verdoppeln', command=buttonVerdoppelnClick)
buttonVerdoppeln.place(x=10, y=80, width=100, height=20)
tkFenster.mainloop()
