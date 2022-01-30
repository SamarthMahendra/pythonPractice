a=[['sam',5],['hello',1]]
def sec(x):
    return x[1]
a.sort(key=sec)
print(a)