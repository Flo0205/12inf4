from block import Block


class Field(object):
    def __init__(self):
        self._field = {}
        for h in range(20):
            for w in range(10):
                self._field[f"{h}.{w}"] = 0

    def update(self):
        pass

    def printField(self):
        for h in range(20):
            line = "| "
            for w in range(10):
                if self._field[f"{h}.{w}"] == 0:
                    line += "O "
                else:
                    line += "M "
            print(line + "|")
        print("⎿_____________________⏌")
        print("\n\n")

    def addBlock(self, block: Block):
        for k in block.shape.keys():
            self._field[k] = block.shape[k]

    def checkMove(self, move: dict) -> bool:
        return True

    def moveDown(self):
        # TODO: Does not work
        moveDict = {}
        for h in range(20):
            for w in range(10):
                if self._field[f"{h}.{w}"] == 1:
                    moveDict[f"{h+1}.{w}"] = 1
                    moveDict[f"{h}.{w}"] = 0
                else:
                    if f"{h}.{w}" not in moveDict:
                        moveDict[f"{h}.{w}"] = 0

        if self.checkMove(moveDict):
            self._field = moveDict

    def rotate(self):
        pass
