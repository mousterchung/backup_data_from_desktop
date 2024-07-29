a=[4,-15,20,13,-6]
print("排 序 前 ：",end=" ")
for i in range(5):
    print(" a[%d]=%3d"%(i,a[i]),end=" ")

for loop in range(1,5):
    for index in range(0,(5-loop)):
        if a[index]<a[index+1]:
            temp=a[index]
            a[index]=a[index+1]
            a[index+1]=temp
    print()
    print("第%d次排列："%loop,end=" ")
    for j in range(5):
        print(" a[%d]=%3d"%(j,a[j]),end=(" "))
