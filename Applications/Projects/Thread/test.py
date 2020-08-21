import threading
import time


def calistir(threadName): 
    for i in range(7):
        print(threadName ," --- ",i)
        time.sleep(0.3)

def calistir2(threadName): 
    for i in range(7):
        print(threadName ," --- ",i)
        time.sleep(0.1)

def calistir3(threadName): 
    for i in range(7):
        print(threadName ," --- ",i)


t1 = threading.Thread(target=calistir, args = ("thread-1", ), daemon=True) # daemon ile 2 ve 3 thread bittiyse 1i bekleme main threadi sonlardır
t2 = threading.Thread(target=calistir2, args = ("thread-2", ))
t3 = threading.Thread(target=calistir3, args = ("thread-3", ))

t1.start()
t2.start()
t3.start()
