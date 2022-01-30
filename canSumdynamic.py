def cansum(s,targetsum,memo={}):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum==0:
        return True
    if targetsum < 0:
        return False
    for i in s:
        r=targetsum-i
        if cansum(s,r,memo )==True:
            memo[targetsum]=True
            return memo[targetsum]
    memo[targetsum]=False
    return memo[targetsum]
print(cansum([7,14],300))