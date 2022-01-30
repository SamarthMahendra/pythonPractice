from timeit import  default_timer as timer
def printmatrix(l):
    for i in l:
        for j in i:
            print(j, end=" ")
        print(end="\n")
def gridtraveler(m,n):
    l=[[0]*(n+1) for i in range(m+1)]
    l[1][1]=1
    for i in range(m+1):
        for j in range(n+1):
            if j+1<=n:
                l[i][j+1]+=l[i][j]
            if i+1<=m:
                l[i+1][j]+=l[i][j]
    print(l[m][n])
start=timer()
gridtraveler(300,18)
end=timer()
print(end-start)