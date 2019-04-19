import tkinter
from tkinter import ttk
from tkinter import *
import os
import urllib.request

def play():
    link = "https://raw.githubusercontent.com/dakinfemiwa/RacingGame/master/race.py"
    name = "raceP.py"

    urllib.request.urlretrieve(link, name)

    x = os.getcwd()

    os.system("cd " + x)
    os.system(name)

homepageWindow = Tk()
homepageWindow.overrideredirect(1)
homepageWindow.title("RACERS")
homepageWindow.geometry("600x400")

photo = PhotoImage(file="raceFlag.png")
backgroundLabel = Label(homepageWindow, image=photo)
backgroundLabel.place(relx=.0, rely=.0)

playButton = Button(homepageWindow, text="PLAY", bd=0, background="black", foreground="white", font="Ebrima 25", activebackground="gray", activeforeground="black", command=play)
playButton.place(relx=.4, rely=.4)

homepageWindow.mainloop()