import tkinter
import threading
from tkinter import ttk
from tkinter import *
import random
import datetime
import time
import math

def LeaderBoard():
    global leaderboard, cars

    bg2 = "#000000"
    fg2 = "orange"

    leaderboard = Tk()
    leaderboard.overrideredirect(1)
    leaderboard.title("Leaderboard")
    leaderboard.geometry("300x174+500+300")
    leaderboard.config(bg=bg2)
    ranking = []

    font= "Fixedsys 15"
    font2= "Fixedsys 20 bold"
    font3 = "Fixedsys 17"

    for x in range(0, len(cars)):
        for y in range(0, len(cars)):
            if cars[y][4] == x + 1:
                ranking.append([])
                ranking[x].append("Player " + str(cars[y][0]))
                ranking[x].append(cars[y][3])

    #print(ranking)

    titleLabel = Label(leaderboard, text=" LEADERBOARD ", font=font2, background=bg2, foreground=fg2, anchor=CENTER , justify=CENTER)
    titleLabel.grid(row=0, column=0, columnspan=3, rowspan=1)

    for x in range(0, len(ranking)):
        no = Label(leaderboard, text="  " + str(x+1)+ "  ", font=font, background=bg2, foreground=fg2)
        no.grid(row=x+1, column=0, sticky="NSEW", rowspan=1, columnspan=2)

        if ranking[x][0] != "Car No 2" :
            car = Label(leaderboard, text=ranking[x][0], font=font, background=bg2, foreground=fg2, anchor=W)
            car.grid(row=x+1, column=2, sticky="NSEW", rowspan=1, columnspan=1)
        else:
            car = Label(leaderboard, text="You", font=font, background=bg2, foreground=fg2, anchor=W)
            car.grid(row=x+1, column=2, sticky="NSEW", rowspan=1, columnspan=1)

        carTimes = Label(leaderboard, text=ranking[x][1], font=font, background=bg2, foreground=fg2, anchor=W)
        carTimes.grid(row=x+1, column=3, sticky="NSEW", rowspan=1, columnspan=1)

    blank = Label(leaderboard, text="", font=font2,background=bg2)
    blank.grid(row=x+2, column=1, sticky="NSEW", rowspan=1, columnspan=1)

    if ranking[0][1] != ranking[1][1]:
        message = ranking[0][0] + " Wins"
    else:
        message = "Draw"

    messageLabel = Label(leaderboard, text=message, font=font3, background=bg2, foreground=fg2, anchor=W)
    messageLabel.grid(row=x+3, column=1, sticky="NSEW", rowspan=1, columnspan=3)

    leaderboard.mainloop()


def move(event):
    if event.keysym.upper() == "M":
        if cars[1][1] < (.975*1250):
            xChange = random.randint(19, 23)
            gameCanvas.move(cars[1][0], xChange, 0)
            cars[1][1] += xChange

    if event.keysym.upper() == "Q":
        if cars[0][1] < (.975*1250):
            xChange = random.randint(19, 23)
            gameCanvas.move(cars[0][0], xChange, 0)
            cars[0][1] += xChange

def clock():
    global timing
    timing = 0
    while pos != 2:
        time.sleep(0.01)
        timing += (0.02 * (10/8))
        #print(timing)
        timing = round(timing, 2)
        if pos != 1:
            timeLabel['text'] = timing

def close():
    date = datetime.datetime.today()
    print("Closing file")
    file.destroy()
    try:
        leaderboard.destroy()
    except:
        pass
    quit()

def play():
    global pos
    #initialTime = time.clock()
    #print(initialTime)

    while True:
        time.sleep(0.15)
        for car in cars:
            if car[1] >= (.925*1250):
                if len(car) == 3:
                    pos += 1
                    timStr = str(round(timing, 2))
                    for x in range(0, len(timStr)):
                        if timStr[x] == ".":
                            break;

                    section = timStr[x+1:len(timStr)]
                    if len(section) == 1:
                        timStr + "0"


                    car.append(timStr)
                    car.append(pos)
            if pos == 2:
                LeaderBoard()
                break;

title="COUNTDOWN"
background="black"
background2= "gray"


instructions = "Press Q to move the top car\nPress M to move the bottom car"

title = "RACERS"
background = "black"
background2= "black"
bg2 = "#7A7A7A"
pos = 0

file = Tk()
file.title(title)
file.geometry("1250x650+10+50")
file.overrideredirect(1)
file.config(bg=background)

exitButton = Button(file, text= " × ", command = close, font="Arial 35", bd=0, background="black", foreground="white", cursor="hand2")
exitButton.place(relx=.95, rely=-.025)

fileTitle = Label(file, text=title, background=background, font="Segoe 29")
fileTitle.config(fg="white")
fileTitle.place(relx=.0, rely=.025)

gameCanvas = Canvas(file, width=1250, height=500, background=bg2, bd=0)
gameCanvas.place(relx=.0, rely=.1)

carsImages = ["racecar1.png", "racecar2.png", "racecar3.png", "racecar4.png", "racecar5.png", "racecar6.png"]
random.shuffle(carsImages)
cars = []
photoImages = []

for c in carsImages:
    photoImage = PhotoImage(file=c)
    photoImages.append(photoImage)

for car in range(0, 2):
    xValue = 10
    yValue = (75*(car + 2)) + 50
    car1 = gameCanvas.create_image(10, yValue, image=photoImages[car])
    cars.append([])
    cars[car].append(car1)
    cars[car].append(xValue)
    cars[car].append(yValue)

for car in range(0, 7):
    line = gameCanvas.create_line(0, (75*(car-1) + 90), 1250, (75*(car-1) + 90), width=3, fill="white")

#print(cars)

startLine = Canvas(gameCanvas, width=1, height=500)
startLine.place(relx=.05, rely=.0)

crossLine = Canvas(gameCanvas, width=1, height=500)
crossLine.place(relx=.975, rely=.0)

def countDown1():
    lbl.config(bg=background)
    lbl.config(foreground="white", font=('fixedsys 60'))
    for k in range(3, 0, -1):
        lbl["text"] = str(k)
        file.update()
        time.sleep(1)
    lbl.destroy()
    lbl2.destroy()

lbl = Label()
lbl.place(relx=.4, rely=.35)
lbl2 = Label(file, text=instructions, font='fixedsys 15', bg=background)
lbl2.config(fg="white")
lbl2.place(relx=.32, rely=.5)

timeLabel = Label(file, text=0.000, font="Ebrima 20", width=10, anchor=E)
timeLabel.place(relx=.85, rely=.9)

countDown1()

file.bind("<KeyRelease>", move)

threading.Thread(target=play, args=()).start()
threading.Thread(target=clock, args=()).start()
threading.Thread(target=file.mainloop(), args=()).start()
