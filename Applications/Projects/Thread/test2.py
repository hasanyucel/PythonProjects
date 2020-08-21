import threading
import time

def calistir(): 
    for i in range(8):
        time.sleep(1)

def calistir2(): 
    for i in range(8):
        time.sleep(0.5)

t1 = threading.Thread(target=calistir)
t2 = threading.Thread(target=calistir2)

start_time = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))