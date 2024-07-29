import math as ma
a=float(input("三角形第一邊:"))
b=float(input("三角形第二邊:"))
c=float(input("三角形第三邊:"))
p=float((a+b+c)/float(2))
d=ma.sqrt(p*(p-a)*(p-b)*(p-c))
print("三角形面積:",d)
