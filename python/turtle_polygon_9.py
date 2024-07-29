from turtle import*
shape("turtle")
col=["orange","limegreen","gold","plum","tomato","blue","yellow","purple","pink"]
for i in range(9):
    color(col[i])
    forward(100)
    left(180*7/9+180)
done()
