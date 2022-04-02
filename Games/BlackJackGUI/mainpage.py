from argparse import Action
from tkinter import Button, Entry, Frame, Label, Tk


class MainPage(object):
    def __init__(self, parent: Tk, SetConfig: Action):
        self.SetConfig = SetConfig
        self.players = 1

        self.titleLabel = Label(parent, text="BLACKJACK")
        self.titleLabel.grid(row=0, column=1, columnspan=2, padx=90, pady=25)

        self.filler1 = Frame(parent, background="darkgray", width=100)
        self.filler1.grid(row=0, column=0, rowspan=4, padx=25)

        self.filler2 = Frame(parent, background="darkgray", width=100)
        self.filler2.grid(row=0, column=4, rowspan=4, padx=25)


        self.text = Label(parent, text="How many players are playing? (max. 4)")
        self.text.grid(row=1, column=1, columnspan=2, padx=25)

        self.input = Entry(parent, width=30)
        self.input.grid(row=2, column=1, columnspan=2, padx=25)

        self.button = Button(parent, text="Play", command=self.CheckInput)
        self.button.grid(row=3, column=1, columnspan=2, padx=25)

    def CheckInput(self):
        inPlayers = int(self.input.get())

        if inPlayers < 1 or inPlayers > 4:
            return

        self.players = inPlayers

        self.titleLabel.destroy()
        self.filler1.destroy()
        self.filler2.destroy()
        self.text.destroy()
        self.input.destroy()
        self.button.destroy()

        self.SetConfig()
