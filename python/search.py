import sort
from fib import fib
def showdata(data):
    for i in range(len(data)):print('%3d'%data[i],end='')
    print()
def sequentially(d,s):
    find=False
    for i in range(len(d)):
        if d[i]==s:
            print(f'Found {d[i]} at {i+1}')
            find=True
    if find==False:print('Not found')
def binary(d,s):
    d=sort.bubble(d)
    low =0
    high=len(d)-1
    while low<=high:
        mid=int((low+high)/2)
        if   s<data[mid]:
            print(f'{s} between {low+1}[{data[low]}] and median {mid+1}[{data[mid]}], look for left')
            high=mid-1
        elif s>data[mid]:
            print(f'{s} between median {mid+1}[{data[mid]}] and {high+1}[{data[high]}], look for right')
            low=mid+1
        else:
            print(f'Found {s} at {mid}')
            return
    print('Not found')
def interpolation(d,s):
    low =0
    high=len(d)-1
    while low<=high:
        mid=low+int((s-data[low])*(high-low)/(data[high]-data[low]))
        if s==data[mid]:
            print(f'Found {s} at {mid}')
            return
        elif s<data[mid]:
            print(f'{s} between {low+1}[{data[low]}] and median {mid+1}[{data[mid]}], look for left')
            high=mid-1
        elif s<data[mid]:
            print(f'{s} between median {mid+1}[{data[mid]}] and {high+1}[{data[high]}], look for right')
            low=mid+1
    print('Not found')
def fibonacci(d,s):
    MAX=20
    index=2
    while fib(index)<=MAX:index+=1
    index-=1
    #index>=2
    root=fib(index)
    diff1=fib(index-1)
    #diff2=fib(index-2)
    diff2=root-diff1
    root-=1
    while True:
        if s==data[root]:
            print(f'Found {s} at {root}')
            return
        else:
            if index==2:
                print('Not found')
                return
            if s<data[root]:
                root-=diff2
                diff1,diff2=diff2,tmp-diff2
                index-=1
            else:
                if index==3:
                    print('Not found')
                    return
                root+=diff2
                diff1,diff2=diff1-diff2,diff2-diff1
                index-=2