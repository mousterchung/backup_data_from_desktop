import random as R
import time as T
import threading as TH
from contextlib import contextmanager as CTM
_local=TH.local()
@CTM
def acquire(*locks):
    locks=sorted(locks,key=lambda x:id(x))
    acquired=getattr(_local,'acquired',[])
    if acquired and max(id(lock)for lock in acquired)>=id(locks[0]):
        raise RuntimeError('Lock Order Violation')
    acquired.extend(locks)
    _local.acquired=acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]
def philosopher(id,left,right):
    while True:
        with acquire(left,right):
            print(id,'eating')
            T.sleep(R.random())
        print(id,'thinking')
        T.sleep(R.random())
num_sticks=5
sticks_lock=[TH.Lock()for n in range(num_sticks)]
for n in range(num_sticks):
    t=TH.Thread(target=philosopher,args=(n,sticks_lock[n],sticks_lock[(n+1)%num_sticks]))
    t.start()
