import itertools
def funsub(s,n):
    return list(itertools.combinations(s,n))
s={1,2,3}
n=len(s)
res=[]
for i in range(n):
    temp=funsub(s,i)
    res.append(temp)
print(res)

