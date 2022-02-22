from deck import Deck
from player import Player
from dealer import Dealer

def main():
    # Initialisierung der Objekte
    cardDeck = Deck()
    dealer = Dealer(cardDeck)
    player = Player(cardDeck)

    # Erstellung der Variablen außerhalb der Schleife
    pValue = 0
    dValue = 0

    # Lässt das Spiel solange laufen, bis beide passen oder einer verliert
    while not player.Done or not dealer.Done:

        # Lässt den Spieler entscheiden, solange dieser nicht gepasst hat
        if not player.Done:
            player.GetPlayerInput()
        # Lässt den Dealer entscheiden, solange dieser nicht gepasst hat
        if not dealer.Done:
            dealer.DecideAction()

        # Laden der Handwerte
        pValue = player.GetHandValue()
        dValue = dealer.GetHandValue()
        printStats(pValue, dValue)

        # Check ob einer über 21 ist
        if pValue > 21:
            print("\nDu hast verloren!")
        elif dValue > 21:
            print("\nDu hast gewonnen!")

    if pValue == dValue:
        print("\nKeiner gewinnt!")
    elif pValue > dValue:
        print("\nDu hast gewonnen!")
    else:
        print("\nDu hast verloren!")

# Gibt die Werte beider Hände in der Konsole aus
def printStats(pValue, dValue):
    print("\n\n-----------------------")
    print(f"Hand: {pValue}")
    print(f"Dealer: {dValue}")
    print("-----------------------\n")

# Startet das Spiel, wenn diese Datei ausgeführt wird
if __name__ == "__main__":
    main()