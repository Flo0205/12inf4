from torch import true_divide
from dealer import Dealer
from deck import Deck
from playerUI import PlayerUI
from tkinter import *

class TableUI(object):
    def __init__(self, parent: Tk, players: int):
        self.parent = parent
        self.players = players
        
        deck = Deck()
        self._dealer = Dealer(deck)


        self.dealerLabel = Label(self.parent, text="Dealer: 0")
        self.dealerLabel.grid(row=0, column=1, columnspan=2, pady=25)

        self.playerUIs = []
        for i in range(self.players):
            self.playerUIs.append(PlayerUI(self.parent, i+1, [1, i], deck, self.Continue))
            pui = self.playerUIs[i]
            pui: PlayerUI
            pui.updateBalance(0, True)
        
        self.__old_init__()

        p1 = self.playerUIs[0]
        p1: PlayerUI
        p1.placeGameButtons()

        self.currentPlayer = 1

    def updateDealerValue(self, value: int):
        self.dealerLabel.config(text=f"Dealer: {value}")


    # TODO: Die ganze Funktion hier ist komisch.... Mach die neu
    def Continue(self):
        last = self.playerUIs[self.currentPlayer-1]
        last: PlayerUI
        last.destroyGameButtons()
        last.updateBalance(last.GetHandValue(), True)


        self.currentPlayer = self.currentPlayer + 1

        if self.currentPlayer > self.players:

            #TODO: Dealer action hier
            self._dealer.DecideAction()
            self.updateDealerValue(self._dealer.GetHandValue())
            #TODO: Auswertung hier
            self.DeathCheck()

            self.currentPlayer = 1

        p: PlayerUI
        done = True
        for p in self.playerUIs:
            if not p.Done:
                done = False

        if done:
            return self.GameOver()
        else:
            p = self.playerUIs[self.currentPlayer-1]
            while p.Done:
                self.currentPlayer = self.currentPlayer + 1
                if self.currentPlayer > self.players:
                    self.currentPlayer = 1
                p = self.playerUIs[self.currentPlayer-1]

            p.placeGameButtons()

        
    def GameOver(self):
        print("Game Over!")

    # Funktionen des alten tables
    def __old_init__(self):
        # Erstellung der Werte-Variablen
        self.dValue = 0
        self.pValues = {}
        self.response = {}

        for pc in range(self.players):
            self.pValues[pc+1] = 0

    def DeathCheck(self):
        # Check ob einer über 21 ist
            # Spieler Check
            for i in range(self.players):
                if not i+1 in self.response:
                    self.pValues[i+1] = self.playerUIs[i].GetHandValue()
                    if self.pValues[i+1] > 21:
                        self.playerUIs[i].Done = True
                        self.response[i+1] = "loss"
                    elif self.pValues[i+1] == 21:
                        self.playerUIs[i].Done = True
                        self.response[i+1] = "win"
            # Dealer Check
            if self.dValue == 21:
                self._dealer.Done = True
                for i in range(self.players):
                    if not i+1 in self.response:
                        self.playerUIs[i].Done = True
                        self.response[i+1] = "loss"
            elif self.dValue > 21:
                self._dealer.Done = True
                for i in range(len(self.players)):
                    if not i+1 in self.response:
                        self.playerUIs[i].Done = True
                        self.response[i+1] = "win"

    def ResponseProcessor(self):
        # Siegescheck
        for i in range(self.players):
            if not i+1 in self.response:
                if self.pValues[i+1] == self.dValue:
                    self.response[i+1] = "draw"
                elif self.pValues[i+1] > self.dValue:
                    self.response[i+1] = "win"
                else:
                    self.response[i+1] = "loss"
        





main = Tk()
main.geometry("550x200")
main.resizable(0, 0)

TableUI(main, 4)

main.mainloop()