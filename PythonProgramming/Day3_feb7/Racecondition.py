#race condition is multiple threads access  shared data without synchronization
import threading
count=0
lock = threading.Lock()

def increment():
    global count
    with lock:
        for _ in range(100000):
            count+=1
t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)