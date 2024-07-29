from turtle import*
shape("turtle")
col=["orange","limegreen","gold","plum","tomato","blue","yellow"]
for i in range(7):
    color(col[i])
    forward(100)
    left(180*5/7+180)
done()
