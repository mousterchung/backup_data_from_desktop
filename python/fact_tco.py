import sys
class TailRecurseException(BaseException):
    def __init__(self,args,kwargs):
        self.args=args
        self.kwargs=kwargs
def tail_call_optimized(g):
    def func(*args,**kwargs):
        f=sys._getframe()
        if(f.f_back and f.f_back.f_back and f.f_back.f_back.f_code==f.f_code):
            raise TailRecurseException(args,kwargs)
        else:
            while 1:
                try:
                    return g(*args,**kwargs)
                except TailRecurseException as e:
                    args=e.args
                    kwargs=e.kwargs
    return func
def fact_tco(n,result=1):
    if n==1 or n==0:
        return result
    else:
        return fact_tco(n-1,n*result)
def fact_r_tail(n,result=1):
    if n==1 or n==0:
        return result
    else:
        return fact_r_tail(n-1,n*result)
####
sys.setrecursionlimit(2000)
print(fact_r_tail(1000))
sys.setrecursionlimit(100)
print(fact_tco(1000))