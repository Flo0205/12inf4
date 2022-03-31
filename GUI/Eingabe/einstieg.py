from tkinter import *

def button_action():
    entry_text = eingabefeld.get()
    if entry_text == "":
        antwort_label.config(text="Gib zuerst deinen Namen ein.")
    else:
        entry_text = "Welcome " + entry_text + "!"
        antwort_label.config(text=entry_text)


fenster = Tk()
fenster.title("Musterprogramm für ein Eingabefeld!")

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

fenster.mainloop()
