from random import randint
from playerBase import PlayerBase


class Dealer(PlayerBase):
    def __init__(self, deck):
        super().__init__(deck)
        self.riskRoundDone = False

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