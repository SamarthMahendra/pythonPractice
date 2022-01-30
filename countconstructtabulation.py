def countconstruct(target,wordbank):
    l=[0]*(len(target)+1)
    l[0]=1
    for i in range(len(l)):
        for j in wordbank:
                if target[i:i+len(j)]==j:
                    if i+len(j)<=len(target):
                        l[i+len(j)]+=l[i]
    print(l)
countconstruct('purple',['purp','p','ur','le','purpl'])
