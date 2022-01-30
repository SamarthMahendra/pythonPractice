ar=[]
t=300
def howsum(s,targetsum,memo={}):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum==0:
        return []
    if targetsum<0:
        return None
    for i in s:
        r=targetsum-i
        rs=howsum(s,r,memo)
        if rs !=None:
            memo[targetsum]=rs+[i]
            return memo[targetsum]
    memo[targetsum]=None
    return memo[targetsum]

print(howsum([7,14],300))
