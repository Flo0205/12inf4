from tkinter import Tk
from mainpage import MainPage
from tableUI import TableUI


class BlackJack(object):
    def __init__(self) -> None:
        self.main = Tk()
        self.main.geometry("550x200")
        self.main.resizable(0, 0)

        self.config = MainPage(self.main, self.SetConfigs)

        self.main.mainloop()

    def SetConfigs(self):
        self.table = TableUI(self.main, self.config.players, self.GameFinished)

    def GameFinished(self):
        print(self.table.response)



if __name__ == "__main__":
    BlackJack()

