from turtle import*
shape("turtle")
col=["red","orange","gold","yellow","limegreen","green","skyblue","blue","purple","plum"]
left(90)
color("white")
forward(330)
right(90)
for i in range(100):
    color(col[i%10])
    forward(20)
    right(3.6)
right(90)
color("white")
forward(330)
left(90)
color("black")
done()
