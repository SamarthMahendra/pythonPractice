def appendatbeg(a,l):
    return [ a + e for e in l]
def binarystring(n):
    if n==0:return []
    if n==1:return ["0","1"]
    else:
        return (appendatbeg("0",binarystring(n-1))+appendatbeg("1",binarystring(n-1)))
def bitstring(n):
    if n==0:return []
    if n==1:return ["0","1"]
    return [digit+bitst for digit in bitstring(1) for bitst in bitstring(n-1)]
print(binarystring(4))
print(" ",end=" \n")
print(bitstring(4))
