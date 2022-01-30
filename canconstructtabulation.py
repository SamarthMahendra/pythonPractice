def canconstruct(target,wordbank):
    l=[False]*(len(target)+1)
    l[0]=True
    for i in range(len(l)):
        if l[i]==True:
            for j in wordbank:
                if j in target and target.index(j)==i:
                        if i+len(j)<=len(target):
                            l[i+len(j)]=True
    print(l[len(target)])
canconstruct('abcdef',['ab','abc','cd','def','abcd'])