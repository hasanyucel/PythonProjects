import random

def satir_getir(yol):
    dosya = open(yol,"r",encoding="utf8")
    lines = dosya.readlines()
    rand_line = random.randint(0,len(lines)-1)
    satir = (lines[rand_line])
    dosya.close()
    return satir

def numara_olustur():
    numara = random.randint(1000000,9999999)
    return ("0352"+str(numara))

ad = satir_getir("isimler.txt").replace("\n","")
soyad = satir_getir("soyisimler.txt").replace("\n","")
numara = numara_olustur()
print(ad,soyad)
print(numara)   