def gcd(x,y):
    if x>y:
        k=y
    else:
        k=x

    while x>=k and y>=k:
        if x%k==0 and y%k==0:
            break
        k-=1
    return k

while True:
    a=eval(input("輸入第一個正整數a:"))
    b=eval(input("輸入第二個正整數b:"))
    if a>0 and b>0:
        break
    else:
        print("無效輸入，請重新輸入···")
        print()

print("a,b兩整數的GCD為",gcd(a,b))
