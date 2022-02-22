from deck import Deck


# Standart Klasse, von der Spieler und Dealer erben.
# Enthält alle grundlegenden Eigenschaften und Funktionen
class PlayerBase(object):
    def __init__(self, deck: Deck):
        self._cards = []
        self.Done = False
        self._deck = deck

    def GetHandValue(self):
        return self._deck.GetValue(self._cards)

    def Draw(self):
        self._cards.append(self._deck.Draw())

    def Pass(self):
        self.Done = True