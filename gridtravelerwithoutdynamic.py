from timeit import default_timer as timer
def gridtraveler(m,n):
    if (m==1 and n==1):
        return 1
    if (m==0) or (n==0):
        return 0
    return gridtraveler(m-1,n)+gridtraveler(m,n-1)

start=timer()
print(gridtraveler(14,14))
end=timer()
print(end-start)