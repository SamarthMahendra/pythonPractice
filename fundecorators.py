import functools
def startenddec(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        r=fun(*args,**kwargs)
        return r
    return  wrapper
@startenddec
def add(x):
    return x+5

re=add(5)
print(re)