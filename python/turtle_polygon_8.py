from turtle import*
shape("turtle")
col=["orange","limegreen","gold","plum","tomato","blue","yellow","purple"]
for i in range(8):
    color(col[i])
    forward(100)
    left(180*6/8+180)
done()
