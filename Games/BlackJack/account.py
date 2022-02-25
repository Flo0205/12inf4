class Account(object):
    def __init__(self, id: int, money: int):
        self.ID = id
        self.Balance = money
        self._payment = 0

    def PayToPlay(self):
        done = False
        while not done:
            inString = input(f"Balance: {self.Balance}\nHow much do you want to play?  ")
            if inString.isnumeric():
                inNum = int(inString)
                if inNum <= self.Balance and inNum > 0:
                    self._payment = inNum
                    self.Balance -= inNum
                    done = True
                else:
                    print("You dont have that much money!")
            else:
                print("Please input a number!")

    def PayOut(self, winCondition: str):
        if winCondition == "draw":
            self.Balance += self._payment
        elif winCondition == "win":
            self.Balance += 2*self._payment
        self._payment = 0
