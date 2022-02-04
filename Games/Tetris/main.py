from time import sleep
from turtle import up
from block import Block
from field import Field
from eventhandler import EventHandler
import msvcrt, threading

events = EventHandler()

def main():
    field = Field()

    events.on_left += field.moveLeft
    events.on_right += field.moveRight
    events.on_update += field.update

    updater = fieldupdater()
    updater.__init__()
    updater.start()

    inhandler = inputhandler()
    inhandler.start()
    inhandler.join()

    updater.loop = False
    updater.join()

class inputhandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.loop = True 

    def run(self):
        while self.loop:
            key = str(msvcrt.getch()).lower().split('\'')[1]
            if key == 'a':
                events.on_left()
            elif key == 'd':
                events.on_right()
            elif key == 'c':
                self.loop = False
                return

class fieldupdater(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.loop = True

    def run(self):
        while self.loop:
            sleep(1)
            events.on_update()

if __name__ == "__main__":
    main()