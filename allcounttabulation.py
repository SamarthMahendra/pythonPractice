def allcount(target,wordbank):
    l=[None]*(len(target)+1)
    l[0]=[[]]
    for i in range(len(l)):
        for j in wordbank:
            if target[i:i+len(j)]==j and i+len(j)<=len(target):
                x=l[i]
                for k in x:
                    k.insert(0,j)
                if l[i+len(j)]!=None:
                    l[i+len(j)].append()
                else:
                    l[i+len(j)]=x
    print(l)
allcount('abc',['ab','c','a','bc'])