import threading

def timerEx():
    print("yucel.io")

timer = threading.Timer(2,timerEx)
timer.start()
print("Test")
