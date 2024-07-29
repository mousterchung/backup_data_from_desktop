num=0
times=0
average=0
a=0
def avg(n):
    global num
    global times
    global average
    num+=a
    times+=1
    average=num/times

while a!=-1:
    a=eval(input("輸入分數（輸入-1結束程式）:"))
    if a==-1:
        break
    avg(a)

print("你的平均分數為:",average)
