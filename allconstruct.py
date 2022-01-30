def allconstruct(target,wordbank,result=[]):
    if target=='':
        return [[]]
    result=[]
    for w in wordbank:
        if w in target:
            if target.index(w)==0:
                suffix=target[len(w):]
                rs=allconstruct(suffix,wordbank,result)
                rc=[]
                for i in rs:
                    rc.append([w]+i)
                result.extend(rc)


    return result

r=allconstruct('abcd',['a','bc','ab','cd','abc','d'])
print(r)