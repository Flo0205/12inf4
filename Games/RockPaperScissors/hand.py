import datetime
from random import randint, seed


class Hand(object):
    def __init__(self, player):
        self.player = player
        self._state = 'none'
        self._states = ['rock', 'paper', 'scissors']
        self._prints = [self._printRock, self._printPaper, self._printScissors]

    def rps(self):
        seed(randint(1, 3000))
        num = randint(1, 9) // 3 - 1
        self._state = self._states[num]

        print(f"Player {self.player}:")
        self._prints[num]()

        return self._state

    def _printRock(self):
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

    def _printPaper(self):
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

    def _printScissors(self):
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)