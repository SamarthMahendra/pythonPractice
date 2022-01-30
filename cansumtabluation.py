def cansum(target,nums):
    l=[False]*(target+1)
    l[0]=True
    for i in range(len(l)):
        if l[i]==True:
            for j in nums:
                if i+j<=target:
                    l[i+j]=True
                if l[target]==True:
                    break
    print(l[target])
cansum(7,[5,3,4])