from timeit import default_timer as timer
string = "Hello World"*1000000
mylist=string.split(" ")
start=timer()
newstring = " ".join(mylist)
stop=timer()
print(stop-start)
st=""
start=timer()
for i in mylist:
    st+=i

stop=timer()
print(stop-start)


