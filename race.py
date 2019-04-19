import tkinter
import threading
from tkinter import ttk
from tkinter import *
import random
import datetime
import time

def LeaderBoard():
    global leaderboard, cars

    bg2 = "#000000"

    leaderboard = Tk()
    leaderboard.overrideredirect(1)
    leaderboard.title("Leaderboard")
    leaderboard.geometry("250x174+100+100")
    leaderboard.config(bg=bg2)
    ranking = []

    font= "Fixedsys 15"
    font2= "Fixedsys 20 bold"

    for x in range(0, len(cars)):
        for y in range(0, len(cars)):
            if cars[y][3] == x + 1:
                ranking.append("Car No " + str(cars[y][0]))

    #print(ranking)

    titleLabel = Label(leaderboard, text=" LEADERBOARD ", font=font2, background=bg2, foreground="white", anchor=CENTER , justify=CENTER)
    titleLabel.grid(row=0, column=0, columnspan=3, rowspan=1)

    for x in range(0, len(ranking)):
        no = Label(leaderboard, text="  " + str(x+1)+ "  ", font=font, background=bg2, foreground="white")
        no.grid(row=x+1, column=0, sticky="NSEW", rowspan=1, columnspan=2)

        if ranking[x] != "Car No 2" :
            car = Label(leaderboard, text=ranking[x], font=font, background=bg2, foreground="white", anchor=W)
            car.grid(row=x+1, column=2, sticky="NSEW", rowspan=1, columnspan=1)
        else:
            car = Label(leaderboard, text="You", font=font, background=bg2, foreground="white", anchor=W)
            car.grid(row=x+1, column=2, sticky="NSEW", rowspan=1, columnspan=1)

    leaderboard.mainloop()

def move(event):
    if event.keysym == "space":
        if cars[1][1] < (.925*1250):
            xChange = 25
            gameCanvas.move(cars[1][0], xChange, 0)
            cars[1][1] += xChange


def close():
    date = datetime.datetime.today()
    print("Closing file")
    file.destroy()
    try:
        leaderboard.destroy()
    except:
        pass

def play():
    global pos
    value = 0

    while True:
        time.sleep(0.15)
        for car in cars:
            if car[1] < (.97*1250):
                if cars.index(car) != 1:
                    change = random.randint(21, 29)
                    gameCanvas.move(car[0], change, 0)
                    car[1] += change
                    #print(cars)
            if car[1] >= (.925*1250):
                if len(car) == 3:
                    pos += 1
                    car.append(pos)
            if pos == 6:
                LeaderBoard()
                break;

title = "RACERS"
background = "lightgray"
bg2 = "#7A7A7A"
pos = 0

file = Tk()
file.title(title)
file.geometry("1250x650+10+50")
file.overrideredirect(1)
file.config(bg=background)

exitButton = Button(file, text= " ✖ ", command = close, font="Arial 20", bd=0, background="black", foreground="white", cursor="hand2")
exitButton.place(relx=.95, rely=.0)

fileTitle = Label(file, text=title, background=background, font="Arial 29 bold underline")
fileTitle.place(relx=.0, rely=.0)

gameCanvas = Canvas(file, width=1250, height=500, background=bg2, bd=0)
gameCanvas.place(relx=.0, rely=.1)

carsImages = ["racecar1.png", "racecar2.png", "racecar3.png", "racecar4.png", "racecar5.png", "racecar6.png"]
cars = []
photoImages = []

for c in carsImages:
    photoImage = PhotoImage(file=c)
    photoImages.append(photoImage)

for car in range(0, 6):
    xValue = 10
    yValue = (75*car) + 50
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

file.bind("<KeyRelease>", move)

threading.Thread(target=play, args=()).start()
threading.Thread(target=file.mainloop(), args=()).start()