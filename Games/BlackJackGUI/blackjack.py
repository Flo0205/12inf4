from tkinter import *
from tableUI import TableUI

def GameFinished():
    print(table.response)

main = Tk()
main.geometry("550x200")
main.resizable(0, 0)

table = TableUI(main, 4, GameFinished)
print("yes")

main.mainloop()

