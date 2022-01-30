def canconstruct(target,wordbank):
    if target=='':
        return True
    for w in wordbank:
        if w in target:
            if target.index(w)==0:
                suffix=target[len(w):]
                if canconstruct(suffix,wordbank)==True:
                    return True
    return False
print(canconstruct('abcd',['a','bc','ab','cd','abc','d']))