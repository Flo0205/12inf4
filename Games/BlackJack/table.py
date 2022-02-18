from deck import Deck
from player import Player
from dealer import Dealer


def main():
    cardDeck = Deck()
    dealer = Dealer(cardDeck)
    player = Player(cardDeck)

    # TODO: Ab hier wird in Zukunft das restliche Spielgeschehen gelenkt

if __name__ == "__name__":
    main()