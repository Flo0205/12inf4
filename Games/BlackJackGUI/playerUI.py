from argparse import Action
from tkinter import *
from typing import Tuple
from deck import Deck
from playerBase import PlayerBase

class PlayerUI(PlayerBase):
    def __init__(self, parent: Tk, number: int, pos: Tuple, deck: Deck, Continue: Action):
        super().__init__(deck, Continue)
        self.parent = parent
        self.number = number
        self.pos = pos

        self.playerFrame = Frame(self.parent, background="darkgray", width=100)
        self.playerFrame.grid(row=self.pos[0], column=self.pos[1], padx=25)

        title = Label(self.playerFrame, text=f"Player {self.number}", bg="darkgray", width=9)
        title.pack(side="top", padx=5)

        self.balanceLabel = Label(self.playerFrame, text="Balance: XXXXX", bg="darkgray", width=9)
        self.balanceLabel.pack(side="top", padx=5)

    def placeGameButtons(self):
        self.drawButton = Button(self.playerFrame, text="Draw", command=self.Draw, width=9)
        self.passButton = Button(self.playerFrame, text="Pass", command=self.Pass, width=9)

        self.drawButton.pack(side="top")
        self.passButton.pack(side="top")

    def destroyGameButtons(self):
        self.drawButton.destroy()
        self.passButton.destroy()

    def placeMenuUI(self):
        self.entry = Entry(self.playerFrame, bd=5)
        self.setButton = Button(self.playerFrame, text="Set", command=print)

        self.entry.pack(side="top")
        self.setButton.pack(side="top")

    def destroyMenuUI(self):
        self.entry.destroy()
        self.setButton.destroy()

    def updateBalance(self, value: int, cardBalance: bool):
        if cardBalance:
            self.balanceLabel.config(text=f"Value: {value}")
        else:
            self.balanceLabel.config(text=f"Balance: {value}")
