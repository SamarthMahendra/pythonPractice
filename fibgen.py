import sys


def fib(x):
    a,b=0,1
    while a<x:
        yield a
        a,b=b,a+b
def fib2(x):
    a,b=0,1
    l=[]
    while a<x:
        l.append(a)
        a,b=b,a+b
    return l

a=fib(30)
for i in a:
    print(i)
print(".....")
fib2(30)
print(sys.getsizeof(fib(10000000)))
print((sys.getsizeof(fib2(100000000))))
