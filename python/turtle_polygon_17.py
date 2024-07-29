from turtle import*
shape("turtle")
col=["orange","limegreen","gold","plum","tomato","blue","yellow","purple","pink","brown"]
for i in range(17):
    color(col[i%10])
    forward(50)
    left(180*15/17+180)
done()
