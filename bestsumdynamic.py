def bestsum(s,targetsum,memo={}):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum==0:
        return []
    if targetsum<0:
        return None
    shortest=None
    for i in s:
        r=targetsum-i
        rs=bestsum(s,r)
        if rs!=None:
            rc=rs+[i]
            if (shortest==None) or (len(rc)<len(shortest)):
                shortest=rc
    memo[targetsum]=shortest
    return memo[targetsum]
print(bestsum([5,3,4,25],100))