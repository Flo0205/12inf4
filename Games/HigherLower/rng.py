from random import randint

class RandomNumberGenerator(object):
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

        self.lastNumber = randint(self.min, self.max)
        self.newNumber = self.getRandomNumber()

    def getRandomNumber(self) -> int:
        num = randint(self.min, self.max)
        while self.lastNumber == num:
            num = randint(self.min, self.max)
        return num

    def isCorrect(self, selectedHigher: bool) -> bool:
        if selectedHigher:
            if self.newNumber > self.lastNumber:
                return True
        else:
            if self.newNumber < self.lastNumber:
                return True
        return False

    def check(self, selectedHigher: bool) -> bool:
        res = self.isCorrect(selectedHigher)
        self.lastNumber = self.newNumber
        self.newNumber = self.getRandomNumber()
        return res

    def getDisplay(self) -> str:
        return str(self.lastNumber)
