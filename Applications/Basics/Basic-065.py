# Write a Python program to convert seconds to day, hour, minutes and seconds.

time = int(input("Please Enter Second :"))

day = time // (86400)
time = time % (86400)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))