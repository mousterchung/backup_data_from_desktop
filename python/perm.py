def perm(iterable,r=None):
    items=list(iterable)
    r=len(items) if r is None else r
    answers=[]
    def sub(items,k,p):
        if k==0:
            answers.append(p)
        else:
            for i in range(k):
                sub(items[:i]+items[i+1:],k-1,p+(items[i],))
    sub(items,r,())
    return answers