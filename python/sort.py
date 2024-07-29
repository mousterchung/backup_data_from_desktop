from copy import deepcopy
def showdata(data):
    for i in range(len(data)):print('%3d'%data[i],end='')
    print()
def bubble(d):
    data=deepcopy(d)
    for i in range(len(data)-1,-1,-1):
        flag=0
        for j in range(i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                flag+=1
        if flag==0:break
        print('sort %d times: '%(len(data)-i),end='')
        showdata(data)
    print('sort done:',end='')
    showdata(data)
    return data
def select(d):
    data=deepcopy(d)
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            if data[i]>data[j]:
                data[i],data[j]=data[j],data[i]
    return data
def insert(d):
    data=deepcopy(d)
    for i in range(1,len(data)):
        tmp=data[i]
        no=i-1
        while no>=0 and tmp<data[no]:
            data[no+1]=data[no]
            no-=1
        data[no+1]=tmp
    return data
def shell(d):
    data=deepcopy(d)
    size=len(data)
    k=1
    jmp=size//2
    while jmp!=0:
        for i in range(jmp,size):
            tmp=data[i]
            j=i-jmp
            while tmp<data[j] and j>=0:
                data[j+jmp]=data[j]
                j-=jmp
            data[jmp+j]=tmp
        print('sort %d times: '%k,end='')
        k+=1
        showdata(data)
        print('-'*42)
        jmp//=2
    return data
def merge(data1,data2):
    result=[None for i in range(len(data1)+len(data2))]
    def sub(size1,size2):
        nonlocal result
        index1=index2=0
        for index3 in range(size1+size2):
            if data1[index1]<data2[index2]:
                result.append(data1[index1])
                index1+=1
                print('this number %d is from data1'%result[index3])
            else:
                result.append(data2[index2])
                index2+=1
                print('this number %d is from data2'%result[index3])
            print('now merge sort result: ',end='')
            showdata(result)
            print('\n')
    select(data1)
    select(data2)
    print('\nfirst data sort done: ',end='')
    showdata(data1)
    print('\nsecond data sort done: ',end='')
    showdata(data2)
    print('='*60)
    sub(len(data1)-1,len(data2)-1)
    print('='*60)
    print('\nmerge sort final result: ',end='')
    showdata(result)
    return result
def quick(d,lf,rg):
    data=deepcopy(d)
    size=len(data)
    if lf<rg:
        lf_idx=lf+1
        while data[lf_idx]<data[lf]:
            if lf_idx+1>size:break
            lf_idx+=1
        rg_idx=rg
        while data[rg_idx]>data[lf]:rg_idx-=1
        while lf_idx<rg_idx:
            data[lf_idx],data[rg_idx]=data[rg_idx],data[lf_idx]
            lf_idx+=1
            while data[lf_idx]<data[lf]:lf_idx+=1
            rg_idx-=1
            while data[rg_idx]>data[lf]:rg_idx-=1
        data[lf],data[rg_idx]=data[rg_idx],data[lf]
        showdata(data)
        quick(data,lf,rg_idx-1)
        quick(data,rg_idx+1,rg)
    return data
def heap(d):
    data=deepcopy(d)
    size=len(data)
    def ad_heap(data,i,size):
        j=2*i
        tmp=data[i]
        post=0
        while j<=size and post==0:
            if j<size:if data[j]<data[j+1]:j+=1
            if tmp>=data[j]:
                post=1
            else:
                data[int(j/2)]=data[j])
                j*=2
        data[int(j/2)]=tmp
    for i in range(int(size/2,0,-1):ad_heap(data,i,size-1)
    print()
    print('heap content: ',end='')
    showdata(data)
    for i in range(size-2,0,-1):
        data[i+1],data[1]=data[1],data[i+1]
        ad_heap(data,1,i)
        print('processing: ',end='')
        showdata(data)
    return data
def radix(d):
    data=deepcopy(d)
    size=len(data)
    n=1
    while n<=100:
        tmp=[[0]*100 for row in range(10)]
        for i in range(size):
            m=(data[i]//n%10
            tmp[m][i]=data[i]
        k=0
        for i in range(10):
            for j in range(size):
                if tmp[i][j]!=0:
                    data[k]=tmp[i][j]
                    k+=1
        print('after %3d digit sort: '%n,end='')
        showdata(data)
        n=10*n
    return data