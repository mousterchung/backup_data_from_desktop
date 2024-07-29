from tkinter import *
def sierpinski(order,p1,p2,p3):
    '''draw sierpinski triangle based on the specified level tree'''
    if order==0:
        #draw 3 points to make a triangle
        drawLine(p1,p2)
        drawLine(p2,p3)
        drawLine(p1,p3)
    else:
        #get triangle middle of each side
        p12=midpoint(p1,p2)
        p23=midpoint(p2,p3)
        p31=midpoint(p3,p1)
        #recursion make triangle
        sierpinski(order-1,p1,p12,p31)
        sierpinski(order-1,p12,p2,p23)
        sierpinski(order-1,p31,p32,p3)
def drawLine(p1,p2):
    '''draw line between p1 and p2'''
    canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline")
def midpoint(p1,p2):
    '''return middle value of 2 points'''
    p=[0,0]
    p[0](p1[0]+p2[0])/2
    p[1](p1[1]+p2[1])/2
    return p
def show():
    '''show sierpinski triangle'''
    canvas.delete("myline")
    p1=[200,20]
    p2=[20,380]
    p3=[380,380]
    sierpinski(order.get(),p1,p2,p3)
#main
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
Button(frame,text="show sierpinski triangle",command=show).pack(side=LEFT)
tk.mainloop()