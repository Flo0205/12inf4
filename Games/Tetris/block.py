from random import randint


class Block(object):
    def __init__(self):
        self.shape = self._getShape()

    def _getShape(self) -> dict:
        straight = {"0.5": 1, "1.5": 1, "2.5": 1, "3.5": 1}
        block = {"0.4": 1, "0.5": 1, "1.4": 1, "1.5": 1}
        special = {"0.5": 1, "1.4": 1, "1.5": 1, "2.5": 1}
        l_block = {"0.4": 1, "0.5": 1, "1.5": 1, "2.5": 1}
        anti_l_block = {"0.4": 1, "0.5": 1, "1.4": 1, "2.4": 1}
        curve = {"0.5": 1, "1.4": 1, "1.5": 1, "2.4": 1}
        anti_curve = {"0.4": 1, "1.4": 1, "1.5": 1, "2.5": 1}

        blocks = [straight, block, special, l_block, anti_l_block, curve,  anti_curve]
        return blocks[randint(0, len(blocks)-1)]
