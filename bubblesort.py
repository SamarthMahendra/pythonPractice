from timeit import default_timer as timer
start=timer()
l=[5,1,7,3,9]
for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
end=timer()
print(l)
print(end-start)