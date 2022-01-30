from threading import Thread
import time
def sq():
    for i in range(100):
        i*i
        time.sleep(0.1)
threads=[]
tn=20
for i in range(tn):
    t=Thread(target=sq)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()
print("end")
'''this is multithreading'''