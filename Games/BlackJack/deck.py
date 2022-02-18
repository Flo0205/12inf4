from random import shuffle


class Deck(object):
    def __init__(self):
        self._cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        self._cards = self._cards * 4
        self.Shuffle()

        self._values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "jack":10, "queen":10, "king":10}

    
    def Draw(self):
        card = self._cards[0]
        self._cards.pop(0)
        return card

    def Shuffle(self):
        shuffle(self._cards)

    def GetValue(self, cards):
        value = 0

        aces = 0
        for c in cards:
            if c == "ace":
                aces += 1
            else:
                value += self._values[c]

        for i in range(aces):
            if (value + 11) > 21:
                value += 1
            else:
                value += 11

        return value
        