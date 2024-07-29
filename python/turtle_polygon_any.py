from turtle import *
x=input("請問你要畫的是正幾邊形？")
x=int(x)
shape("turtle")
for i in range(x):
    forward(100)
    y=x-int(2)
    z=y*float(180)
    k=z/x
    right(float(180)-k)
done()
