import random
import linecache

def satir_getir(yol):
    dosya = open(yol,"r",encoding="utf8")
    lines = dosya.readlines()
    rand_line = random.randint(0,len(lines)-1)
    satir = (lines[rand_line])
    dosya.close()
    return satir

ad = satir_getir("isimler.txt").replace("\n","")
soyad = satir_getir("soyisimler.txt").replace("\n","")
print(ad,soyad)
