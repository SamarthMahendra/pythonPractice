def mergesort(arr):
    if len(arr)>1:
        mid=int(len(arr)/2)
        l= arr[:mid]
        r= arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j < len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1

            else:
                arr[k]=r[j]

                j += 1
            k+=1
        while i < len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k]=r[j]
            j+=1
            k+=1
def printf(arr):
    for i in arr:
        print(i,end=" ")
arr=[3,4,1,2,7,6,0,8]
print(arr)
mergesort(arr)
printf(arr)

