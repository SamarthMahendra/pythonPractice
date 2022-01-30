def canconstruct(target,wordbank):
    if target=='':
        return 1
    totalcount=0
    for w in wordbank:
        if w in target:
            if target.index(w)==0:
                suffix=target[len(w):]
                totalcount+=canconstruct(suffix,wordbank)

    return totalcount
print(canconstruct('abcd',['a','bc','ab','cd','abc','d']))