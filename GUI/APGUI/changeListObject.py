from argparse import Action
from tkinter import *
import tkinter as tk

class ChangeListObject(object):
    def __init__(self, master: Tk, steamID, role, removeAction: Action):
        self.steamID = steamID
        self.role = role
        self.removeAction = removeAction

        self.frame = Frame(master=master, height=10, bg="red")
        self.frame.pack()

        Label(master=self.frame, text=steamID).pack(side=tk.LEFT)
        Label(master=self.frame, text=role).pack(side=tk.LEFT)
        Button(master=self.frame, text="Remove", command=self.destroy).pack(side=tk.LEFT)

    def destroy(self):
        self.frame.destroy()
        self.removeAction(self)

    def getValue(self):
        return self.role, self.steamID
        