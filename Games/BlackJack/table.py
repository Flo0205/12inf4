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
        

    # Startet das Spiel. Mögliche Rückgabewerte: "win", "loss" oder "draw"
    def Play(self) -> str:
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

            # TODO Check ob einer über 21 ist

        # TODO Siegescheck

    # Gibt die Werte beider Hände in der Konsole aus
    def _printStats(self, pValues, dValue):
        print("\n\n-----------------------")
        for i in range(len(self._players)):
            print(f"Player {i+1}: {pValues[i+1]}")
        print(f"Dealer: {dValue}")
        print("-----------------------\n")


# Startet das Spiel, wenn diese Datei ausgeführt wird
if __name__ == "__main__":
    table = Table(1)
    table.Play()