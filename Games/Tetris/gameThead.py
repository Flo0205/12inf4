from time import sleep
from field import Field
import threading


class gameUpdater(threading.Thread):
    def __init__(self, field: Field):
        self.__loop = True
        self._loop(field)

    def _loop(self, field):
        while self.__loop:
            field.update()
            sleep(1)

    def stop(self):
        self.__loop = False

