from tkinter import *
def htree(order,center,ht):
    '''draw htree based on the specified level tree'''
    if order>=0:
        p1=[center[0]-ht/2,center[1]-ht/2]#lt
        p2=[center[0]-ht/2,center[1]+ht/2]#lb
        p3=[center[0]+ht/2,center[1]-ht/2]#rt
        p4=[center[0]+ht/2,center[1]+ht/2]#rb
        drawLine([center[0]-ht/2,center[1]],[center[0]+ht/2,center[1]])#h
        drawLine(p1,p2)#vl
        drawLine(p3,p4)#vr
        htree(order-1,p1,ht/2)#recursion lt
        htree(order-1,p2,ht/2)#recursion lb
        htree(order-1,p3,ht/2)#recursion rt
        htree(order-1,p2,ht/2)#recursion rb
def drawLine(p1,p2):
    '''draw line between p1 and p2'''
    canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags="htree")
def show():
    '''show htree'''
    canvas.delete("htree")
    length=200
    center=[200,200]
    htree(order.get(),center,length)
tk=Tk()
canvas=Canvas(tk,width=400,height=400)#create canvas
canvas.pack()
frame=Frame(tk)#create frame
frame.pack(padx=5,pady=5)
#crate label in frame, input level in entry, show button
Label(frame,text="input level: ").pack(side=LEFT)
order=IntVar()
order.set(0)
entry=Entry(frame,textvariable=order).pack(side=LEFT,padx=3)
Button(frame,text="show htree",command=show).pack(side=LEFT)
tk.mainloop()