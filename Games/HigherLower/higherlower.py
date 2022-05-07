import tkinter as tk
from tkinter import *
from rng import RandomNumberGenerator as RNG


rng = RNG(0, 10)
lifes = {}
currentLifes = 3
highestStreak = 0


def inputHigher():
    handleResult(rng.check(True))

def inputLower():
    handleResult(rng.check(False))
    

def handleResult(correct: bool):
    if not correct:
        global currentLifes
        global highestStreak

        cStreak = getStreak()
        if cStreak > highestStreak:
            highestStreak = cStreak

        updateScore(getScore()-1)
        updateStreak(0)
        output.config(text=rng.getDisplay())

        lifes[currentLifes].config(bg="red")
        currentLifes -= 1
        if currentLifes == 0:
            handleEnd()
    else:
        updateStreak(getStreak()+1)
        updateScore(getScore()+getStreak())
        output.config(text=rng.getDisplay())

def handleEnd():
    output.config(text="Game\nOver")
    streak.config(text=f"Highest Streak: {highestStreak}")
    highButton.config(text="Play again!", command=handleReplay)
    lowerButton.config(text="Quit", command=main.quit)

def handleReplay():
    resetLifes()
    updateScore(0)
    updateStreak(0)
    highestStreak = 0
    highButton.config(text="Higher", command=inputHigher)
    lowerButton.config(text="Lower", command=inputLower)
    rng.check(True)
    output.config(text=rng.getDisplay())


def updateScore(num: int):
    score.config(text=f"Score: {num}")

def getScore() -> int:
    return int(score["text"].split(' ')[1])

def updateStreak(num: int):
    streak.config(text=f"Streak: {num}")

def getStreak() -> int:
    return int(streak["text"].split(' ')[1])

def resetLifes():
    global currentLifes
    currentLifes = 3
    for e in lifes.values():
        e.config(bg="green")


main = Tk()
main.title("Higher Lower")
main.geometry("400x200")
main.resizable(False, False)

inputFrame = Frame(main)
inputFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

outputFrame = Frame(main)
outputFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

highButton = Button(inputFrame, text="Higher", command=inputHigher)
highButton.pack(side=tk.TOP, fill=tk.BOTH, padx=20, pady=20)

lowerButton = Button(inputFrame, text="Lower", command=inputLower)
lowerButton.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=20, pady=20)

output = Label(outputFrame, text=rng.getDisplay(), bg="grey", height=30)
output.pack(fill=tk.BOTH, padx=20, pady=20)

score = Label(inputFrame, text="Score: 0")
score.pack(side=tk.TOP, fill=tk.BOTH)

streak = Label(inputFrame, text="Streak: 0")
streak.pack(side=tk.BOTTOM, fill=tk.BOTH)


lifeFrame = Frame(inputFrame, width=100)
lifeFrame.pack(side=tk.TOP, fill=tk.Y, expand=True, pady=5)

life1 = Frame(lifeFrame, bg="green", width=15)
life1.config(height=life1["width"])
life1.pack(side=tk.LEFT, padx=5)

life2 = Frame(lifeFrame, bg="green", width=15)
life2.config(height=life1["width"])
life2.pack(side=tk.LEFT, padx=5)

life3 = Frame(lifeFrame, bg="green", width=15)
life3.config(height=life1["width"])
life3.pack(side=tk.LEFT, padx=5)

lifes[1] = life1
lifes[2] = life2
lifes[3] = life3

main.mainloop()