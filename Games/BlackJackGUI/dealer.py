from random import randint


class Dealer(object):
    def __init__(self, deck):
        self._cards = []
        self.Done = False
        self._deck = deck
        self.riskRoundDone = False

    # Hier entscheidet der Dealer, ob er eine Karte zieht oder nicht
    def DecideAction(self):
        value = self.GetHandValue()

        if value < 16:
            self.Draw()
        elif self.riskRoundDone:
            self.Pass()
        else:
            # Wenn randint() ungerade ist, dann zieht der Dealer trotz hohem Risiko
            if randint(1, 10) % 2 == 1:
                self.Draw()
                self.riskRoundDone = True
            else:
                self.Pass()

    def GetHandValue(self):
        return self._deck.GetValue(self._cards)

    def Draw(self):
        self._cards.append(self._deck.Draw())

    def Pass(self):
        self.Done = True