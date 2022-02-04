from block import Block
from datetime import datetime


class Field(object):
    def __init__(self):
        self._field = {}
        for h in range(20):
            for w in range(10):
                self._field[f"{h}.{w}"] = 0
        self._now = datetime.now()
        
        self.addBlock(Block())

        self._printField()

    def update(self):
        if (datetime.now() - self._now).total_seconds() >= 1:
            self.moveDown()

    def _printField(self):
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
        for k in move.keys():
            if '-' in k:
                return False
            elif int(str(k).split('.')[1]) > 9:
                return False
        # TODO: Check for move down
        return True

    def moveDown(self):
        move_dict = {}
        for h in range(20):
            for w in range(10):
                if self._field[f"{h}.{w}"] == 1:
                    move_dict[f"{h+1}.{w}"] = 1
                    if f"{h}.{w}" not in move_dict:
                        move_dict[f"{h}.{w}"] = 0
                else:
                    if f"{h}.{w}" not in move_dict:
                        move_dict[f"{h}.{w}"] = 0

        if self.checkMove(move_dict):
            self._field = move_dict
            self._printField()
    
    def moveLeft(self):
        move_dict = {}
        for h in range(20):
            for w in range(10):
                if self._field[f"{h}.{w}"] == 1:
                    move_dict[f"{h}.{w-1}"] = 1
                    if f"{h}.{w}" not in move_dict:
                        move_dict[f"{h}.{w}"] = 0
                else:
                    if f"{h}.{w}" not in move_dict:
                        move_dict[f"{h}.{w}"] = 0

        if self.checkMove(move_dict):
            self._field = move_dict
            self._printField()

    def moveRight(self):
        move_dict = {}
        for h in range(20):
            for w in range(10):
                if self._field[f"{h}.{w}"] == 1:
                    move_dict[f"{h}.{w+1}"] = 1
                    if f"{h}.{w}" not in move_dict:
                        move_dict[f"{h}.{w}"] = 0
                else:
                    if f"{h}.{w}" not in move_dict:
                        move_dict[f"{h}.{w}"] = 0

        if self.checkMove(move_dict):
            self._field = move_dict
            self._printField()


    def rotate(self):
        pass
