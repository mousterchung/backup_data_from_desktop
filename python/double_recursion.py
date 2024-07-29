def F1(m):
    if m>3:
        print(m,end="   ")
        return
    else:
        print(m,end="   ")
        F2(m+2)
        print(m,end="   ")

def F2(n):
    if n>3:
        print(n,end="   ")
        return
    else:
        print(n,end="   ")
        F1(n-1)
        print(n,end="   ")

F1(1)
