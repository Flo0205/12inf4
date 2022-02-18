from deck import Deck


class PlayerBase(object):
    def __init__(self, deck: Deck):
        self._cards = []
        self.done = False
        self._deck = deck

    def GetHandValue(self):
        return self._deck.GetValue(self._cards)

    def Draw(self):
        self._cards.append(self._deck.Draw())

    def Pass(self):
        self.done = True