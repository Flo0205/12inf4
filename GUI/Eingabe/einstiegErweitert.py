from tkinter import *
from random import randint

def button_action():
    entry_text = eingabefeld.get()
    if entry_text == "":
        antwort_label.config(text="Gib zuerst deinen Namen ein.")
    else:
        entry_text = "Welcome " + entry_text + "!"
        antwort_label.config(text=entry_text)

def changeColor():
    colors = ["yellow", "blue", "red", "white", "grey", "green"]
    color_label.config(bg=colors[randint(0, len(colors)-1)])
    

def buttonAdd():
    e1 = int(entry_add1.get())
    e2 = int(entry_add2.get())

    add_label.config(text="Answer: " + str(e1+e2))

fenster = Tk()
fenster.title("Erweitertes Musterprogramm für ein Eingabefeld!")

anweisungs_label = Label(fenster, text="Gib deinen Namen ein: ")
antwort_label = Label(fenster)

eingabefeld = Entry(fenster, bd=5, width=40)

antwort_button = Button(fenster, text="Klick me", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.destroy)

anweisungs_label.grid(row=0, column=0)
eingabefeld.grid(row=0, column=1)
antwort_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
antwort_label.grid(row=2, column=0, columnspan=2)


color_button = Button(text="Change color", command=changeColor)
color_label = Label(text="I can change my background!")

color_button.grid(row=3, column=0)
color_label.grid(row=3, column=1)


entry_add1 = Entry(fenster, bd=5, width=40)
entry_add2 = Entry(fenster, bd=5, width=40)
add_button = Button(fenster, text="Click to get the sum!", command=buttonAdd)
add_label = Label(fenster, text="Answer: ")

entry_add1.grid(row=4, column=0)
entry_add2.grid(row=4, column=1)
add_button.grid(row=5, column=0)
add_label.grid(row=5, column=1)


fenster.mainloop()
