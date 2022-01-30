from timeit import default_timer as timer
def gridtraveler(m,n,memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if (m==1 and n==1):
        return 1
    if (m==0) or (n==0):
        return 0
    memo[(m,n)]=gridtraveler(m-1,n,memo)+gridtraveler(m,n-1,memo)
    return memo[(m,n)]
start=timer()
print(gridtraveler(300,18))
end=timer()
print(end-start)