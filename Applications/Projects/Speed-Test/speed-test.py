import speedtest

speed = speedtest.Speedtest()
print("Wait 20 Seconds to calculate speed of connection.")
dmb = speed.download()/1000000
umb = speed.upload()/1000000
print("Download:\t",round(dmb,2),'mb/s')
print("Upload:\t\t",round(umb,2),'mb/s')