import tkinter as tk
from apnetwork import APNetwork as APN
from tkinter import *
from changeListObject import ChangeListObject

apn = APN("10.0.0.1", "13000")
ROLES = apn.getRoles()
changes = []


def addSteamID():
    changes.append(ChangeListObject(listFrame, entry.get(), variable.get(), removeChanges))

def removeChanges(clo: ChangeListObject):
    changes.remove(clo)

def update():
    cdo = {}
    l = changes
    for clo in l:
        clo: ChangeListObject
        role, steamID = clo.getValue()
        if role not in cdo.keys():
            cdo[role] = [steamID]
        else:
            cdo[role] += [steamID]

        clo.destroy()
        

    payload = []
    for o in cdo.keys():
        d = {}
        d["groupname"] = o
        d["members"] = cdo[o]

        payload.append(d)

    apn.updateUsers(payload)



main = Tk()
main.geometry("550x550")
main.title("AutoPerms GUI")

inputFrame = Frame(master=main, height=100, bg="yellow")
inputFrame.pack(fill=tk.X)

listFrame = Frame(master=main, bg="red")
listFrame.pack(fill=tk.BOTH, expand=True)

entry = Entry(inputFrame, width=25)
entry.pack(side=tk.LEFT, pady=20, padx=20)

variable = StringVar(master=inputFrame)
variable.set(ROLES[0])

menu = OptionMenu(inputFrame, variable, *ROLES)
menu.pack(side=tk.LEFT, pady=20, padx=20)

addButton = Button(master=inputFrame, width=5, text="Set", command=addSteamID)
addButton.pack(side=tk.LEFT, pady=20, padx=20)

sendButton = Button(master=inputFrame, width=5, text="Update", command=update)
sendButton.pack(side=tk.LEFT, pady=20, padx=20)



main.mainloop()