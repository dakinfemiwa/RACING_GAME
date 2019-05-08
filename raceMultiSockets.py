import tkinter
import threading
from tkinter import ttk
from tkinter import *
import random
import datetime
import time
import math
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
import urllib.request
import os
import pprint
import socket

class Client:
    def __init__(self, username):
        self.s = socket.socket()
        self.host = '127.0.0.1'
        self.port = 6000
        self.username = username
        

        try:
            self.availiable = False
            self.s.connect((self.host, self.port))
            print("Connected to chat server")
        except ConnectionRefusedError:
            self.availiable = True

    def receiveMessage(self):
        self.incomingMessage = self.s.recv(4096)
        self.incomingMessage = self.incomingMessage.decode()
        print(self.incomingMessage)

    def sendMessage(self, message):
        #message = username + ": " + message
        message = message.encode()
        self.s.send(message)

class Server:
    def __init__(self, username, teamID):
        self.teamID = teamID
        self.s = socket.socket()
        self.host = "0.0.0.0"
        print(self.host)
        print("server will start on host")
        self.port = 6000
        self.s.bind((self.host, self.port))
        print("server done binding to host")

        print("Server is waiting for connections")

    def listen(self):
        self.s.listen(1)

        self.conn, self.addr = self.s.accept()
        self.receive()
        if self.incomingMessage == self.teamID:
            return True
        else:
            return False

        print(self.addr, "connected to the server and is now online")

    def send(self, message):
        #message = username + ": " + message
        print(self.message)
        self.message = self.message.encode()
        self.conn.send(self.message)
        #print("Message has been sent")

    def receive(self):
        self.incomingMessage = self.conn.recv(4096)
        self.incomingMessage = self.incomingMessage.decode()

class Player():
    def __init__(self, username):
        self.username = username
        self.title = "RACING (MULTIPLAYER)"
        self.background="black"
        self.background2= "gray"
        self.title = "RACERS"
        self.background = "black"
        self.background2= "black"
        self.bg2 = "#7A7A7A"
        self.bg3 = "black"
        self.bg4 = "white"
        self.foreground = "white"
        self.foreground1 = "black"
        self.foreground2 = "red"
        self.pos = 0

        self.file = Tk()
        self.file.title(self.title)
        self.file.geometry("1250x650+10+50")
        self.file.overrideredirect(1)
        self.file.config(bg=self.background)


        self.exitButton = Button(self.file, text=" × ", command=lambda :self.close(), font="Arial 35", bd=0, background="black",foreground="white", cursor="hand2", activebackground="black", activeforeground="lightgray")
        self.exitButton.place(relx=.95, rely=-.025)

        self.fileTitle = Label(self.file, text=self.title, background=self.background, font="Ebrima 29", foreground=self.foreground)
        self.fileTitle.place(relx=.0, rely=.025)

        self.gameCanvas = Canvas(self.file, width=1250, height=500, background=self.bg2, bd=0)
        self.gameCanvas.place(relx=.0, rely=.1)

        self.startLine = Canvas(self.gameCanvas, width=5, height=500)
        self.startLine.place(relx=.05, rely=.0)

        self.crossLine = Canvas(self.gameCanvas, width=5, height=500)
        self.crossLine.place(relx=.975, rely=.0)

        self.Images = ["racecar1.png", "racecar2.png", "racecar3.png", "racecar4.png", "racecar5.png", "racecar6.png"]
        self.cars = []
        self.photoImages = []



        for c in self.Images:
            self.photoImage = PhotoImage(file=c)
            self.photoImages.append(self.photoImage)

        #print(self.photoImages)

        for car in range(0, 2):
            xValue = 10
            yValue = (75 * (car + 2)) + 50
            #print(yValue)
            car1 = self.gameCanvas.create_image(10, yValue, image=self.photoImages[car])
            self.cars.append([])
            self.cars[car].append(car1)
            self.cars[car].append(xValue)
            self.cars[car].append(yValue)

        for car in range(0, 7):
            line = self.gameCanvas.create_line(0, (75 * (car - 1) + 90), 1250, (75 * (car - 1) + 90), width=3, fill="white")

        self.findTeam()
        #self.getData()

        self.file.mainloop()
    def close(self):
        date = datetime.datetime.today()
        print("Closing file")
        self.file.destroy()
        self.finishWithData()
        try:
            self.leaderboard.destroy()
        except:
            pass

    def crypt(self):
        try:
            os.remove("tool1a.json")
            os.remove("tool2a.py")
        except:
            pass

        self.file1 = "https://raw.githubusercontent.com/dakinfemiwa/Tools/master/Tool1/tool1a.json"
        self.name1 = "tool1a.json"
        self.file2 = "https://raw.githubusercontent.com/dakinfemiwa/Tools/master/Tool2/tool2a.py"
        self.name2 = "tool2a.py"

        urllib.request.urlretrieve(self.file1, self.name1)
        urllib.request.urlretrieve(self.file2, self.name2)


    def getData(self):
        global sheet
        from tool2a import Cryptographer
        Cryptographer.decrypt("tool1a.json")
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('tool1a.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open('GameDatabases').sheet1
        sheet = self.client.open('GameDatabases').sheet1

    def finishWithData(self):
        try:
            self.sheet.update_cell(self.x + self.lane + 1, 1, self.lane)
            self.sheet.update_cell(self.x + self.lane + 1, 5, "No")
        except:
            pass
        try:
            Cryptographer.encrypt("tool1a.py")
        except:
            pass
        try:
            os.remove("tool1a.json")
        except:
            pass
        try:
            os.remove("tool2a.py")
        except:
            pass
        try:
            os.remove("tool2b.py")
        except:
            pass


    def timer(self):
        try:
            file = open("tool2b.py")
        except:
            self.file = "https://raw.githubusercontent.com/dakinfemiwa/Tools/master/Tool2/tool2b.py"
            self.name = "tool2b.py"
            urllib.request.urlretrieve()
        from tool2b import clock
        tick = clock
        timer.stopwatch()

    def findTeam(self):
        self.teamCanvas = Canvas(self.file, width=1250, height=500, background=self.bg3, bd=0)
        self.teamCanvas.place(relx=.0, rely=.1)

        self.findTeamTitle = "MULTIPLAYER - OPTIOINS"
        self.joinTeamText = "Enter teamID to join"
        self.makeTeamTitle = "CREATE TEAM"
        self.makeTeamText = "Choose a teamID for your group"
        self.joinButtonText = "   JOIN  "
        self.createButtonText = "CREATE"
        self.createErrorText = "Sorry, that name isn't availiable at the moment"
        self.joinErrorText = "Sorry, the teamID does not attribute to an active group"
        self.createWaitText = "Waiting for teams..."
        self.font = "Ebrima 40 underline"
        self.font2 = "Ebrima 20"
        self.font3 = "Ebrima 30"
        self.font4 = "Ebrima 12"
        self.font5 = "Fixedsys 12"
        self.font6 = "Fixedsys 40 underline"

        self.title = Label(self.teamCanvas, text=self.findTeamTitle, font=self.font)
        self.title.place(relx=.05, rely=.1)

        self.joinLabel = Label(self.teamCanvas, text=self.joinTeamText, font=self.font2)
        self.joinLabel.place(relx=.05, rely=.3)

        self.joinButton = Button(self.teamCanvas, text=self.joinButtonText, command = lambda: self.joinGroup())
        self.joinButton.place(relx=.9, rely=.275)

        self.joinEntry = Entry(self.teamCanvas)
        self.joinEntry.place(relx=.45, rely=.3)

        self.createTitle = Label(self.teamCanvas, text=self.makeTeamTitle, font=self.font3)
        self.createTitle.place(relx=.05, rely=.5)

        self.createLabel = Label(self.teamCanvas, text=self.makeTeamText, font=self.font2)
        self.createLabel.place(relx=.05, rely=.65)

        self.createEntry = Entry(self.teamCanvas)
        self.createEntry.place(relx=.45, rely=.65)

        self.createButton = Button(self.teamCanvas, text=self.createButtonText, command= lambda:self.createGroup())
        self.createButton.place(relx=.9, rely=.625)

        self.MMButtons = [self.joinButton, self.createButton]
        self.MMEntries = [self.joinEntry, self.createEntry]

        self.createErrorMessage = Label(self.teamCanvas, text=self.createErrorText, font=self.font4)
        self.createWaitMessage = Label(self.teamCanvas, text=self.createWaitText, font=self.font4)
        self.joinErrorMessage = Label(self.teamCanvas, text=self.joinErrorText, font=self.font4)

        self.createErrorMessage = Label(self.teamCanvas, text=self.createErrorText, font=self.font4)
        self.joinErrorMessage = Label(self.teamCanvas, text=self.joinErrorText, font=self.font4)

        self.ErrorLabels = [self.createErrorMessage, self.joinErrorMessage]

        for widget in self.teamCanvas.winfo_children():
            widget.config(bg=self.bg3, fg=self.foreground)

        for widget in self.ErrorLabels:
            widget.config(fg=self.foreground2)

        for button in self.MMButtons:
            button.config(font=self.font2, background=self.bg4, foreground=self.foreground1, cursor="hand2")

        for entry in self.MMEntries:
            entry.config(font= self.font2, width=35, background=self.bg4, foreground=self.foreground1)



    def move(event):
        if event.keysym.upper() == "M":
            if self.cars[self.lane - 1][1] < (.975 * 1250):
                xChange = random.randint(19, 23)
                gameCanvas.move(self.cars[self.lane - 1][0], xChange, 0)
                self.cars[self.lane][1] += xChange
                Server.send(self.cars[self.lane - 1][1])

    def play():
        while True:
            time.sleep(0.0002)
            for car in self.cars:
                if car[self.OtherLane - 1] < (.97 * 1250):
                    if self.cars.index(car) != 1 and self.cars:
                        self.incomingMessage = int(self.incomingMessage)
                        xChange = self.incomingMessage - self.cars[self.OtherLane - 1][1]
                        gameCanvas.move(self.cars[self.OtherLane - 1][0], xChange, 0)
                        
                if car[1] >= (.925 * 1250):
                    if len(car) == 3:
                        pos += 1
                        timStr = str(round(timing, 2))
                        for x in range(0, len(timStr)):
                            if timStr[x] == ".":
                                break;

                        section = timStr[x + 1:len(timStr)]
                        if len(section) == 1:
                            timStr + "0"

                        car.append(timStr)
                        car.append(pos)
                if pos == 2:
                    LeaderBoard()
                    break;

    def joinGroup(self):
        client = Client(self.username)
        try:
            self.lane = 2
            self.OtherLane = 1

            self.TeamID = self.joinEntry.get()
            
            client.sendMessage(self.TeamID)
        except ConnectionRefusedError:
            self.joinErrorMessage.place(relx=.45, rely=.4)

        self.teamCanvas.destroy()

        threading.Thread(target=self.play, args=())
        threading.Thread(target=client.receiveMessage(), args=())

    def createGroup(self):
        self.TeamID = self.joinEntry.get()
        server = Server(self.username, self.TeamID)
        self.lane = 1
        self.OtherLane = 2

        while True:
            self.OtherPlayers = server.listen()
            if self.OtherPlayers == True:
                self.createErrorMessage.place(relx=.45, rely=.75)
                return False
            else:
                self.createWaitMessage.place(relx=.45, rely=.75)                
                break;

        self.gameCanvas.destroy()
        
        threading.Thread(target=self.play, args=())
        threading.Thread(target=server.receive(), args=())

Player("dakinfemiwa")
