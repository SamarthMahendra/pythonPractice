def fib(n):
    l=[0]*(n+3)
    l[1]=1
    for i in range(n+1):
        l[i+1]+=l[i]
        l[i+2]+=l[i]
    print(l[n])
fib(6)