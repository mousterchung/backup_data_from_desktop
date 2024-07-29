from tkinter import *
from random import *
import time
class Ball:
    def __init__(self,canvas,color,winW,winH,racket):
        self.canvas=canvas
        self.racket=racket
        self.id=canvas.create_oval(0,0,20,20,fill=color)#create ball object
        self.canvas.move(self.id,winW/2,winH/2)#set init position of ball
        startPos=[-4,-3,-3,-2,1,2,3,4]#radom init x-axis move of ball
        shuffle(startPos)#shuffle
        self.x=startPos[0]#horizontal
        self.y=-step#vertical
        self.notTouchBottom=True#did not touch bootom of canvas
    def hitRacket(self,ballPos):
        racketPos=self.canvas.coords(self.racket.id)
        return ballPos[2]>=racketPos[0]and ballPos[0]>=racketPos[2]and ballPos[3]>=racketPos[1]and ballPos[1]>=racketPos[3]
    def ballMove(self):
        self.canvas.move(self.id,self.x,self.y)#step>0 mean move down
        ballPos=self.canvas.coords(self.id)
        if ballPos[0]<=0:self.x=step#sensor ball top over
        if ballPos[1]<=0:self.y=step#sensor ball left over
        if ballPos[2]>=winW:self.x=-step#sensor ball right over
        if ballPos[3]>=winH:self.y=-step#sensor ball bottom over
        if self.hitRacket(ballPos)==True:self.y=-step#sensor touch racket
        if ballPos[3]>=winH:self.notTouchBottom=False#if ball touch bottom of canvas
class Racket:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,15,fill=color)#racket object
        self.canvas.move(self.id,270,400)#racket position
        self.x=0
        self.canvas.bind_all('<KeyPress-Right>',self.moveRight)#bind right keys
        self.canvas.bind_all('<KeyPress-Left>',self.moveLeft)#bind left keys
    def racketMove(self):
        '''move the racket'''
        self.canvas.move(self.id,self.x,0)
        racketPos=self.canvas.coords(self.id)
        if racketPos[0]<=0 or racketPos[2]>=winW:self.x=0#sensor racket left over or right over
    def moveLeft(self,event):self.x=-3#move left
    def moveRight(self,event):self.x=3#move right
winW=640#define width of canvas
winH=480#define height of canvas
step=3#define step
speed=0.01#set move speed
tk=Tk()
tk.title("Bouncing Ball")#game window title
tk.wm_attributes('-topmost',1)#game window on the top level
canvas=Canvas(tk,width=winW,height=winH)
canvas.pack()
tk.update()
racket=Racket(canvas,'puple')#define purple racket
ball=Ball(canvas,'yellow',winW,winH,racket)#define ball object
while ball.notTouchBottom:#if ball did not touch bottom of canvas
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)#control move speed