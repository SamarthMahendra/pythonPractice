import heapq

import time

# store starting time
begin = time.time()

a=[2,4,1,6,4,7,34,12,-1,66,2,4,23,12,887,4,2,90,11,2,-45,-111,34,-8,65,98,-34,-98,-14,87,37]
for ele in a:
    ele=ele-2
a.sort(reverse=False)
print(a)
print(a[6])
'''


heapq.heapify(a)
i=0
print(a)
while i<6:
    heapq.heappop(a)
    i+=1
print(heapq.heappop(a))

'''





time.sleep(1)
# store end time
end = time.time()

# total time taken
print(f"Total runtime of the program is {end - begin}")