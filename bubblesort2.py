from timeit import default_timer as timer
start=timer()
l=[5,1,7,3,9]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
end=timer()
print(l)
print(end-start)