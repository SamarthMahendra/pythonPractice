s={}
def fib(n):
    if n in s:
        return s[n]
    if n==1 or n==2 :
        return 1
    s[n]=fib(n-1)+fib(n-2)
    return s[n]
print(fib(50 ))