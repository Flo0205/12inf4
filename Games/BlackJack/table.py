from tokenize import String
from deck import Deck
from player import Player
from dealer import Dealer

class Table(object):
    def __init__(self):
        # Initialisierung der Objekte
        self._cardDeck = Deck()
        self._dealer = Dealer(self._cardDeck)
        self._player = Player(self._cardDeck)

        # Erstellung der Werte-Variablen
        self.pValue = 0
        self.dValue = 0

    # Startet das Spiel. Mögliche Rückgabewerte: "win", "loss" oder "draw"
    def Play(self) -> str:
        # Lässt das Spiel solange laufen, bis beide passen oder einer verliert
        while not self._player.Done or not self._dealer.Done:

            # Lässt den Spieler entscheiden, solange dieser nicht gepasst hat
            if not self._player.Done:
                self._player.GetPlayerInput()
            # Lässt den Dealer entscheiden, solange dieser nicht gepasst hat
            if not self._dealer.Done:
                self._dealer.DecideAction()

            # Laden der Handwerte
            self.pValue = self._player.GetHandValue()
            self.dValue = self._dealer.GetHandValue()
            self._printStats(self.pValue, self.dValue)

            # Check ob einer über 21 ist
            if self.pValue > 21:
                print("\nDu hast verloren!")
                return "win"
            elif self.dValue > 21:
                print("\nDu hast gewonnen!")
                return "loss"

        if self.pValue == self.dValue:
            print("\nKeiner gewinnt!")
            return "draw"
        elif self.pValue > self.dValue:
            print("\nDu hast gewonnen!")
            return "win"
        else:
            print("\nDu hast verloren!")
            return "loss"

    # Gibt die Werte beider Hände in der Konsole aus
    def _printStats(self, pValue, dValue):
        print("\n\n-----------------------")
        print(f"Hand: {pValue}")
        print(f"Dealer: {dValue}")
        print("-----------------------\n")


# Startet das Spiel, wenn diese Datei ausgeführt wird
if __name__ == "__main__":
    table = Table()
    table.Play()