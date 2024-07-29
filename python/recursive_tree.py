from tkinter import *
import math
def paintTree(depth,x1,y1,length,angle):
    '''draw recursive tree based on the specified level tree'''
    if depth>=0:
        depth-=1
        x2=x1+int(math.cos(angle)*length)
        y2=y1-int(math.sin(angle)*length)
        #draw line
        drawLine(x1,y1,x2,y2)
        #draw left
        paintTree(depth,x2,y2,length*sizeRatio,angle+angleValue)
        #draw left
        paintTree(depth,x2,y2,length*sizeRatio,angle-angleValue)
def drawLine(x1,y1,x2,y2):
    '''draw line between p1 and p2'''
    canvas.create_line(x1,y1,x2,y2,tags="htree")
def show():
    '''show recursive tree'''
    canvas.delete("myline")
    myDepth=depth.get()
    paintTree(myDepth,myWidth/2,myHeight,myHeight/3,math.pi/2)
#main
tk=Tk()
myWidth=400
myHeight=400
canvas=Canvas(tk,width=myWidth,height=myHeight)#create canvas
canvas.pack()
frame=Frame(tk)#create frame
frame.pack(padx=5,pady=5)
#crate label in frame, input depth in entry, show button
Label(frame,text="input depth: ".pack(side=LEFT)
depth=IntVar()
depth.set(0)
entry=Entry(frame,textvariable=depth).pack(side=LEFT,padx=3)
Button(frame,text="show recursive tree",command=show).pack(side=LEFT)
angleValue=math.pi/4#set angle
sizeRatio=0.6#set seze ratio
tk.mainloop()