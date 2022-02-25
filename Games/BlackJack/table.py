from deck import Deck
from player import Player
from dealer import Dealer

class Table(object):
    def __init__(self, players):
        # Erstellung der Werte-Variablen
        self.dValue = 0
        self.pValues = {}
        self.response = {}

        # Initialisierung der Objekte
        self._cardDeck = Deck()
        self._dealer = Dealer(self._cardDeck)
        self._players = []

        for pc in range(players):
            self._players.append(Player(self._cardDeck, pc+1))
            self.pValues[pc+1] = 0
        

    # Startet das Spiel. Mögliche Rückgabewerte: {1: "win", 2: "loss", 3: "win", 4: "draw"}
    def Play(self) -> dict:
        # Lässt das Spiel solange laufen, bis beide passen oder einer verliert
        done = False
        while not done:

            # Lässt die Spieler entscheiden, solange diese nicht gepasst haben + Updaten der Handwerte
            p: Player
            for p in self._players:
                if not p.Done:
                    p.GetPlayerInput()
                    self.pValues[p.ID] = p.GetHandValue()
            # Lässt den Dealer entscheiden, solange dieser nicht gepasst hat + Updaten des Handwertes
            if not self._dealer.Done:
                self._dealer.DecideAction()
                self.dValue = self._dealer.GetHandValue()

            self._printStats(self.pValues, self.dValue)

            # Check ob alle gepasst haben
            done = True
            if not self._dealer.Done:
                done = False
            for p in self._players:
                if not p.Done:
                    done = False

            # Check ob einer über 21 ist
            # Spieler Check
            for i in range(len(self._players)):
                if not i+1 in self.response:
                    if self.pValues[i+1] > 21:
                        self._players[i].Done = True
                        self.response[i+1] = "loss"
                    elif self.pValues[i+1] == 21:
                        self._players[i].Done = True
                        self.response[i+1] = "win"
            # Dealer Check
            if self.dValue == 21:
                self._dealer.Done = True
                for i in range(len(self._players)):
                    if not i+1 in self.response:
                        self._players[i].Done = True
                        self.response[i+1] = "loss"
            elif self.dValue > 21:
                self._dealer.Done = True
                for i in range(len(self._players)):
                    if not i+1 in self.response:
                        self._players[i].Done = True
                        self.response[i+1] = "win"

        # Siegescheck
        for i in range(len(self._players)):
            if not i+1 in self.response:
                if self.pValues[i+1] == self.dValue:
                    self.response[i+1] = "draw"
                elif self.pValues[i+1] > self.dValue:
                    self.response[i+1] = "win"
                else:
                    self.response[i+1] = "loss"

        self._printResult(self.response)
        return self.response


    # Gibt die Werte beider Hände in der Konsole aus
    def _printStats(self, pValues: dict, dValue: int):
        print("\n\n-----------------------")
        for i in range(len(self._players)):
            print(f"Player {i+1}: {pValues[i+1]}")
        print(f"Dealer: {dValue}")
        print("-----------------------\n")

    def _printResult(self, response: dict):
        print("\n\n\n-----------------------")
        for k in sorted(response):
            print(f"Player {k}: {response[k]}")
        print("-----------------------\n")


# Startet das Spiel, wenn diese Datei ausgeführt wird
if __name__ == "__main__":
    inString = input("How many players are playing? (1 - 4)  ")
    if inString.isnumeric():
        inNum = int(inString)
        if inNum > 0 and inNum < 5:
            table = Table(inNum)
            table.Play()