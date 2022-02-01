from block import Block
from field import Field


def main():
    f = Field()
    f.printField()
    f.addBlock(Block())
    f.printField()
    f.moveDown()
    f.printField()


if __name__ == "__main__":
    main()
