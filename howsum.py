ar=[]
t=7
def howsum(s,targetsum):
    if targetsum==0:
        return []
    if targetsum<0:
        return None
    for i in s:
        r=targetsum-i
        rs=howsum(s,r)
        if rs !=None:
            if sum(rs+[i])==t:
                ar.append(rs+[i])
            else:
                return rs+[i]

howsum([5,3,4,7],t)
print(ar)