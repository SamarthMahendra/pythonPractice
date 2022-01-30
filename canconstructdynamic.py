def canconstruct(target,wordbank,memo={}):
    if target in memo:
        return memo[target]
    if target =='':
        return True
    for w in wordbank:
        if w in target:
            if target.index(w)==0:
                suffix=target[len(w):]
                if canconstruct(suffix,wordbank,memo)==True:
                    memo[target]=True
                    return True
    memo[target]=False
    return False
print(canconstruct('eeeeeeeeeeeeeeeeeeeeefeeeeeeeeeef',['e','ee','eeee','eeeeeeeee','eeeeeeeeeeee']))