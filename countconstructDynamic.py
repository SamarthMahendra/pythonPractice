def canconstruct(target,wordbank,memo={}):
    if target in memo:
        memo[target]
    if target=='':
        return 1
    totalcount=0
    for w in wordbank:
        if w in target:
            if target.index(w)==0:
                suffix=target[len(w):]
                memo[target]=canconstruct(suffix,wordbank,memo)
                totalcount+=memo[target]

    return totalcount
print(canconstruct('abcd',['a','bc','ab','cd','abc','d']))