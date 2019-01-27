import tkinter
import threading
from tkinter import ttk
from tkinter import *
import random
import datetime
import time

def close():
    date = datetime.datetime.today()
    print("Closing file")
    file.destroy()

title = "A GAME"
background = "lightblue"
bg2 = "#AACCFF"

file = Tk()
file.title(title)
file.geometry("1250x600+10+50")
file.overrideredirect(1)
file.config(bg=background)

exitButton = Button(file, text= " ✖ ", command = close, font="Arial 20", bd=0, background="black", foreground="white", cursor="hand2")
exitButton.place(relx=.95, rely=.0)

fileTitle = Label(file, text=title, background=background, font="Arial 29 bold underline")
fileTitle.place(relx=.0, rely=.0)

gameCanvas = Canvas(file, width=1250, height=500, background=bg2, bd=0)
gameCanvas.place(relx=.0, rely=.1)

randomPosx = random.randrange(0, 1000)
randomPosx /= 1000

print(randomPosx)

starPos = 0.0
starPos2 = 0.05

def move(event):
    global starPos
    time.sleep(0.025)
    starPos += 0.00875
    car.place(relx=starPos, rely=.45)

opponents = []
place = 0

for car in range(10):
    a = []
    if car !=4 and car != 5:
        car1 = Canvas(gameCanvas, width=25, height =25)
        car1.place(relx=.0, rely=starPos2)
        a.append(car1)
        a.append(.0)
        opponents.append(a)
    starPos2 += 0.1

print(opponents)

def check():
    for opponent in opponents:
        try:
            if opponent[0] >= 0.9:
                return True
            else:
                return False
        except:
            pass

def play():
    global value
    global starPos3
    value = 0

    while True:
        time.sleep(0.05)
        for opponent in opponents:
            if opponents.index(opponent) != 4:
                    if value < .895:
                        print(opponent)
                        change = random.randrange(23, 25)
                        change /= 500
                        i = opponents.index(opponent)
                        value = opponent[1]
                        value = value + change
                        opponents[i][1] = value
                        yPos = (0.1 * (i + 1))
                        opponent[0].place(relx=opponents[i][1], rely=yPos)
                    if value >=.895:
                        place += 1
                        opponent.append(place)
                        break;



car = Canvas(gameCanvas, width=25, height=25)
car.place(relx=starPos, rely=.45)

file.bind("<space>", move)
while False:
    if starPos >= .895:
        place += 1
        print("Rank: {}".format(str(place)))
        break;

a = False


crossLine = Canvas(gameCanvas, width=1, height=500)
crossLine.place(relx=.9, rely=.0)


threading.Thread(target=play, args=()).start()

threading.Thread(target=file.mainloop(), args=()).start()

# file.mainloop()
