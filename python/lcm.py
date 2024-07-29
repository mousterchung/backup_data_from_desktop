def lcm(x,y):
    if x>y:
        k=x
    else:
        k=y

    while k>=x and k>=y:
        if k%x==0 and k%y==0:
            break
        k+=1
    return k

while True:
    a=eval(input("輸入第一個正整數a："))
    b=eval(input("輸入第二個正整數b："))
    if a>0 and b>0:
        break
    else:
        print("無效輸入，請重新輸入···")
        print()

print("a,b兩數的LCM為",lcm(a,b))
