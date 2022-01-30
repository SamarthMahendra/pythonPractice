def bestsum(target,nums):
    l=[None]*(target+1)
    l[0]=[]
    for i in range(len(l)):
        if l[i]!=None:
            for j in nums:
                if i+j<=target:
                    if l[i+j]!=None:
                        l[i+j]=l[i+j] if (len(l[i+j])<(len(l[i])+1)) else l[i]+[j]
                    else:
                        l[i+j]=l[i]+[j]
    print(l[target])
bestsum(8,[2,3,5])
