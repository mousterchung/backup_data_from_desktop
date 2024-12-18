from tkinter import*
import math as M
curve=0
undulation=0
def key_down(e):
    global curve,undulation
    key=e.keysym
    if key=="Up":
        undulation-=20
    if key=="Down":
        undulation+=20
    if key=="Left":
        curve-=5
    if key=="Right":
        curve+=5
    draw_road(curve,undulation)
updown=[0]*24
for i in range(23,-1,-1):
    updown[i]=M.sin(M.radians(180*i/23))
BORD_COL=["red","orange","yellow","green","blue","indigo","violet"]
def draw_road(di,ud):
    canvas.delete("ROAD")
    h=24
    y=600-h
    for i in range(23,0,-1):
        uw=(i-1)*(i-1)*1.5
        ux=400-uw/2+di*(23-(i-1))
        uy=y+int(updown[i-1]*ud)
        bw=i*i*1.5
        bx=400-bw/2+di*(23-i)
        by=y+h+int(updown[i]*ud)
        col=BORD_COL[(6-tmr%7+i)%7]
        canvas.create_polygon(ux,uy,ux+uw,uy,bx+bw,by,bx,by,fill=col,tag="ROAD")
        h-=1
        y-=h
tmr=0
def main():
    global tmr
    tmr+=1
    draw_road(curve,undulation)
    root.after(200,main)
root=Tk()
root.title("繪製道路")
root.bind("<Key>",key_down)
canvas=Canvas(width=800,heigh=600,bg="black")
canvas.pack()
canvas.create_rectangle(0,300,800,600,fill="gray")
canvas.create_text(400,100,text="使用方向鍵讓道路產生變化",fill="white")
main()
root.mainloop()
