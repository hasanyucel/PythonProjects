#import win32gui, win32con
#The_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE) #! İlk 3 satır cmd ekranını ve araç çubuğunda ki simgesini kaldırır.
import requests
from bs4 import BeautifulSoup
import threading
from tkinter import Label,Tk

def Gold():
    root = Tk(className=' Altın Kuru Kuveyttürk')   #* Canvasın başlık yazısı.(Iconlarla birlikte kapandığı için gözükmüyor.)
    root.geometry("100x36+1820+1004")               #* Canvasın büyüklüğü ve başlangıç noktalarını ayarlar.
    root.wm_attributes("-topmost", 1)               #* Always on top özelliğini aktif eder.
    root.overrideredirect(1)                        #* Arayüzdeki maximize minimize ve close iconlarını kaldırır.
    lab = Label(root)
    lab.pack()

    def clock():
        r = requests.get("https://www.kuveytturk.com.tr/finans-portali/")
        soup = BeautifulSoup(r.content,"lxml")
        k = soup.find_all("div",attrs={"class","col-md-4 col-sm-6"}, limit=3)
        result = k[2].getText()
        r2 = result.replace(" ","").replace("\n\n"," ")
        alis =  " SATIŞ\t: " + r2[20:26]
        # if(int(float(r2[40:43])) < 379 ):
        #     root.configure(background='red')
        #     lab.configure(background='red')
        satis = " ALIŞ\t: "  + r2[40:46]
        yuzde = "% " + r2[61:68]
        print(yuzde)
        sonuc = alis + "\n" + satis
        lab.config(text=sonuc)
        root.after(10000, clock) 
    clock()
    root.mainloop()

Gold()