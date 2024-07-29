def add(a,b):
    if len(a)!=len(b):raise
    m=len(a)
    result=[[None for j in range(n)]for i in range(m)]
    for i in range(m):
        if len(a[i])!=len(b[i]):raise
        n=len(a[i])
        for j in range(n):
            result[i][j]=a[i][j]+b[i][j]
    return result
def multiply(a,b):
    if len(a[0])!=len(b):raise
    result=[[None for j in range(n)]for i in range(p)]
    m=len(a)
    n=len(b)
    p=len(b[0])
    for i in range(m):
        for j in range(p):
            tmp=0
            for k in range(n):
                tmp+=int(a[i][k])*int(b[k][j])
            result[i][j]=tmp
    return result
def transpose(a):
    result=[[None for j in range(len(a[0]))]for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[j][i]=a[i][j]
    return result
def sparse_to_3tuple(a):
    result=[[len(a),len(a[0]),None]]
    nonzero=0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]!=0:
                nonzero+=1
                result.append([i,j,a[i][j]])
    result[0][2]=nonzero
    return result
def triangular_to_1d(a):
    result=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i][j]!=0):
                result.append(a[i][j])
    return result