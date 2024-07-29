memory={1:1,0:0}
def fib(n):
    if n not in memory:memory[n]=fib(n-1)+fib(n-2)
    return memory[n]