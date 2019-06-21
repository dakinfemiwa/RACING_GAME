import random
from tkinter import *
from threading import Thread
import time


class Racing:
    def __init__(self):
        self.Window = Tk()
        self.Window.title("RACING GAME")
        self.Window.geometry('1250x650+10+50')
        self.Window.config(bg='#141414')

        self.Game_Cars = []
        self.Game_Images = []
        self.Game_Timer = 0
        self.Game_Position = 0
        self.Game_Active = True

        self.Menu_Frame = Frame(self.Window, bg='#141414', width=1250, height=650)
        self.Game_Frame = Frame(self.Window, bg='#141414', width=1250, height=650)
        self.Countdown_Frame = Frame(self.Window, bg='#141414', width=300, height=175)
        self.Leaderboard_Frame = Frame(self.Window, bg='#181818', width=1250, height=510)

        self.LBL_Title = Label(self.Game_Frame, text='RACING GAME', background='#141414', foreground='white', font="Ebrima 29 bold").place(relx=.01, rely=.01)

        self.LBL_Time = Label(self.Game_Frame, text='CURRENT TIME', background='#141414', foreground='white', font="Ebrima 12 bold").place(relx=.8, rely=.9)
        self.INF_Time = Label(self.Game_Frame, text='00.00', background='#141414', foreground='white', font="Ebrima 24 bold")
        self.INF_Time.place(relx=.9, rely=.895)

        # self.LBL_Position = Label(self.Game_Frame, text='POSITION', background='#141414', foreground='white', font="fixedsys 12 bold").place(relx=.6, rely=.9)
        self.INF_Position = Label(self.Game_Frame, text='1', background='#141414', foreground='white', font="fixedsys 24 bold")
        # self.INF_Position.place(relx=.7, rely=.895)

        self.Game_Canvas = Canvas(self.Game_Frame, width=1250, height=500, background="#7A7A7A", bd=0)
        self.Game_Canvas.place(relx=.0, rely=.1)

        for x in range(6):
            photoImage = PhotoImage(file=f'racecar{x+1}.png')
            self.Game_Images.append(photoImage)

        for car in range(6):
            xValue = 10
            yValue = (75 * car) + 50
            car1 = self.Game_Canvas.create_image(10, yValue, image=self.Game_Images[car])
            self.Game_Cars.append([])
            self.Game_Cars[car].append(car1)
            self.Game_Cars[car].append(xValue)
            self.Game_Cars[car].append(yValue)

        for x in range(7):
            self.Game_Canvas.create_line(0, (75 * (x - 1) + 90), 1250, (75 * (x - 1) + 90), width=3, fill="white")

        for x in range(1250):
            self.Game_Canvas.create_line(65, x, 65, x + 1, width=3, fill="white")
            self.Game_Canvas.create_line(1225, x, 1225, x + 1, width=3, fill="white")

        self.Game_Frame.place(x=0, y=0)

        Thread(target=self.countdown).start()

        self.Window.mainloop()

    def countdown(self):
        self.Countdown_Frame.place(relx=.4, y=.7)

        CurrentSecond = 3

        Label(self.Countdown_Frame, text='Press M to move your car', font='fixedsys 16 bold', bg='#141414', fg='#FFFFFF').place(relx=.135, rely=.8)
        LBL_Countdown = Label(self.Countdown_Frame, text=CurrentSecond, font='fixedsys 50 bold', bg='#141414', fg='#FFFFFF')
        LBL_Countdown.place(relx=.425, rely=.25)

        while CurrentSecond > 0:
            time.sleep(1)
            CurrentSecond -= 1
            LBL_Countdown.config(text=CurrentSecond)

        self.Countdown_Frame.place_forget()

        Thread(target=self.timer).start()
        Thread(target=self.play).start()

        self.Window.bind('<KeyRelease>', lambda event: self.move(event))

    def convert(self, t):
        stringT = str(t)
        a = False
        b = False
        
        for digit in range(0, len(stringT)):
            if stringT[digit] == ".":
                a = True
                break

        string = stringT[digit: len(stringT)-1]

        if len(string) < 2:
            b = True            

        if b == True:        
            if a == False:
                stringT = stringT + ".00"
            else:
                stringT = stringT + "0"

        return stringT


    def timer(self):
        while self.Game_Position != 6:
            time.sleep(0.01)
            self.Game_Timer += (0.01 * 3)
            self.Game_Timer = round(self.Game_Timer, 2)

            
            if self.Game_Position != 1:
                self.INF_Time['text'] = self.Game_Timer

    def play(self):
        while self.Game_Active:
            time.sleep(0.003)
            for car in self.Game_Cars:
                if car[1] < (.97 * 1250):
                    if self.Game_Cars.index(car) != 1:
                        change = random.randint(15, 55)
                        change /= 10
                        self.Game_Canvas.move(car[0], change, 0)
                        car[1] += change
                if car[1] >= (.925 * 1250):
                    if len(car) == 3:
                        self.Game_Position += 1
                        car.append(str(self.Game_Timer))
                        car.append(self.Game_Position)
                if self.Game_Position == 6:
                    Thread(target=self.ending).start()
                    self.Game_Active = False

    def move(self, event):
        if event.keysym.upper() == "M":
            if self.Game_Cars[1][1] < (.975 * 1250):
                xChange = random.randint(30, 35)
                self.Game_Canvas.move(self.Game_Cars[1][0], xChange, 0)
                self.Game_Cars[1][1] += xChange

    def ending(self):
        self.scores()
        x = 1.0
        while True:
            self.Leaderboard_Frame.place(relx=x, rely=0.095)
            x -= 0.005
            if x + 0.002 < 0.0:
                break
            time.sleep(0.001)

    def scores(self):
        #self.LBL_Title = Label(self.Leaderboard_Frame, text='LEADERBOARD', background='#181818', foreground='orange', font="fixedsys 29 bold").place(relx=.01, rely=.01)
        if self.Game_Cars[1][4] == 1:
            self.posStr = "1st "
        elif self.Game_Cars[1][4] == 2:
            self.posStr = "2nd "
        elif self.Game_Cars[1][4] == 3:
            self.posStr = "3rd "
        else:
            self.posStr = str(self.Game_Cars[1][4]) + "th "
            
        self.LBL_Title = Label(self.Game_Frame, text='You came: '+ self.posStr, background='#141414', foreground='white', font="Ebrima 29 bold").place(relx=.01, rely=.01)
        ranking = []
        for x in range(0, len(self.Game_Cars)):
            for y in range(0, len(self.Game_Cars)):
                if self.Game_Cars[y][4] == x + 1:
                    ranking.append([])
                    ranking[x].append("Car No " + str(self.Game_Cars[y][0]))
                    ranking[x].append(self.Game_Cars[y][3])

        x1 = 0.05
        y = 0.2

        for x in range(0, len(ranking)):
            no = Label(self.Leaderboard_Frame, text="  " + str(x + 1) + "  ", font="Fixedsys 30 bold", background='#181818', foreground='orange')
            no.place(relx=x1, rely=y)

            if ranking[x][0] != "Car No 2":
                car = Label(self.Leaderboard_Frame, text=ranking[x][0], font="Fixedsys 30 bold", background='#181818', foreground='orange', anchor=W, justify="left")
                car.place(relx=x1 + 0.2, rely=y)
            else:
                car = Label(self.Leaderboard_Frame, text="You", font="Fixedsys 30 bold", background='#181818', foreground='orange', anchor=W, justify="left")
                car.place(relx=x1 + 0.3, rely=y)

            carTimes = Label(self.Leaderboard_Frame, text=ranking[x][1], font="Fixedsys 30 bold", background='#181818', foreground='orange', anchor=W)
            carTimes.place(relx=x1 + 0.82, rely=y)
            y += 0.1


if __name__ == '__main__':
    Test = Racing()
