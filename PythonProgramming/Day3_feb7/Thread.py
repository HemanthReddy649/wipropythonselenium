#threading - execution of tasks
#multithreading is execution of many tasks at atime - concurrent execution -

#multiprocessing -

#threading -imported

#process - execution unit
#threads-light weight unit inside the process

#simple thread

import threading
import time

def task():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")
t=threading.Thread(target=task)
t.start()
t.join()


#multi threading

