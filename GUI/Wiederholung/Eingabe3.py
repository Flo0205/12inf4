from tkinter import *

main = Tk()
main.title('Test')
main.geometry('256x125')

def buttonCommand():
    e1 = int(entry1.get())
    e2 = int(entry2.get())

    entry1.delete(0, 'end')
    entry1.insert(0, str(e1+e2))

    entry2.delete(0, 'end')

entry1 = Entry(main)
entry1.place(x=24, y=25, width=96, height=25)

label = Label(main, text='+=')
label.place(x=120, y=25, width=16, height=25)

entry2 = Entry(main)
entry2.place(x=136, y=25, width=96, height=25)

button = Button(main, text='Add', command= buttonCommand)
button.place(x=24, y=75, width=208, height=25)

main.mainloop()
