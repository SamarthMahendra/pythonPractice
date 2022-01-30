def howsum(target,nums):
    l=[None]*(target+1)
    l[0]=[]
    for i in range(len(l)):
        if l[i] !=None:
            for j in nums:
                if i+j<=target:
                    l[i+j]=l[i]+[j]

                if l[target]!=None and sum(l[target])==target:
                    break

    print(l[target])
howsum(7,[5,4,3])
