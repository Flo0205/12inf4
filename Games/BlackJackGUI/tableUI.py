from argparse import Action
from dealer import Dealer
from deck import Deck
from playerUI import PlayerUI
from tkinter import *

class TableUI(object):
    def __init__(self, parent: Tk, players: int, finish: Action):
        self.parent = parent
        self.players = players
        self.finish = finish
        
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
        
        self.response = {}

        p1 = self.playerUIs[0]
        p1: PlayerUI
        p1.placeGameButtons()

        self.currentPlayer = 1

    def updateDealerValue(self, value: int):
        self.dealerLabel.config(text=f"Dealer: {value}")

    def Continue(self):
        last = self.playerUIs[self.currentPlayer-1]
        last: PlayerUI
        last.destroyGameButtons()
        last.updateBalance(last.GetHandValue(), True)
        self.PlayerDeathCheck(last)


        self.currentPlayer = self.currentPlayer + 1
        if self.currentPlayer > self.players:
            self.currentPlayer = 1
            self._dealer.DecideAction()
            self.dealerLabel.config(text=f"Dealer: {self._dealer.GetHandValue()}")
            self.DealerDeathCheck()
            
            
        done = True
        for p in self.playerUIs:
            p: PlayerUI
            if not p.Done:
                done = False

        if done:
            while not self._dealer.Done:
                self._dealer.DecideAction()
                self.dealerLabel.config(text=f"Dealer: {self._dealer.GetHandValue()}")
                self.DealerDeathCheck()
            self.ResponseProcessor()
            self.CleanUp()
            self.finish()
            return

        next = self.playerUIs[self.currentPlayer-1]
        next: PlayerUI
        while next.Done:
            self.currentPlayer = self.currentPlayer + 1
            if self.currentPlayer > self.players:
                self.currentPlayer = 1
            next = self.playerUIs[self.currentPlayer-1]
        next.placeGameButtons()
    
    def PlayerDeathCheck(self, player: PlayerUI):
        value = player.GetHandValue()
        if value > 21:
            player.Done = True
            self.response[player.number] = "loss"
        elif value == 21:
            player.Done = True
            self.response[player.number] = "win"

    def DealerDeathCheck(self):
        value = self._dealer.GetHandValue()
        if value > 21:
            self._dealer.Done = True
            p: PlayerUI
            for p in self.playerUIs:
                if p.number not in self.response.keys():
                    p.Done = True
                    self.response[p.number] = "win"
        if value == 21:
            self._dealer.Done = True
            p: PlayerUI
            for p in self.playerUIs:
                if p.number not in self.response.keys():
                    p.Done = True
                    self.response[p.number] = "loss"

    def ResponseProcessor(self):
        self.DealerDeathCheck()
        dValue = self._dealer.GetHandValue()
        for p in self.playerUIs:
            p:PlayerUI
            if p.number not in self.response.keys():
                pValue = p.GetHandValue()
                if pValue == dValue:
                    self.response[p.number] = "draw"
                elif pValue > dValue:
                    self.response[p.number] = "win"
                elif pValue < dValue:
                    self.response[p.number] = "loss"

    def CleanUp(self):
        # self.dealerLabel.destroy()
        for pUI in self.playerUIs:
            pUI: PlayerUI
            pUI.destroyGameButtons()

            if self.response[pUI.number] == "win":
                pUI.changeColor("green")
                continue
            elif self.response[pUI.number] == "loss":
                pUI.changeColor("red")
                continue
            else:
                pUI.changeColor("blue")
                continue
