n=100
for i in range(1,n):
    c=0
    for k in range(1,i):
        if i%k==0:
            c=c+1
    if(c<2):
        print(i)



