from timeit import default_timer as timer
a=[1,2,3,4,5,6,7,8]
for i in range(8,100000000):
    a.append(i)
print("enter a digit to be searched")
x=int(input())
start=0
end=len(a)
flag=0
s=timer()
while start<=end:
    mid=int((start+end)/2)
    if x==a[mid]:
        flag=1
        break
    else:
        if x<a[mid]:
            end=mid-1
        else:
            start=mid+1
e=timer()
print(e-s)

if flag:
    print("found")
else:
    print("Not found")
s1=timer()

for i in range(len(a)):
    if x==a[i]:
        print("found")
        break

e1=timer()
print(e1-s1)
