from playerBase import PlayerBase


# Der Spieler, muss ich mehr sagen?
class Player(PlayerBase):
    def __init__(self, deck, id):
        super().__init__(deck)
        self.ID = id
    
    # Lässt den Spieler eine Eingabe machen und verarbeitet diese
    def GetPlayerInput(self):
        done = False
        while not done:
            inString = input(f"\n\nPlayer {self.ID}\nDraw: 1\nPass: 2\n\nInput number: ")
            if not inString.isnumeric():
                print("\n\nOnly input numbers!")
                continue
            inNum = int(inString)
            if inNum == 1:
                self.Draw()
                done = True
            elif inNum == 2:
                self.Pass()
                done = True
            else:
                print("\n\nOnly input 1 or 2!")
                continue
