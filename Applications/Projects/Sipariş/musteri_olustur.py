import random

def satir_getir(yol):
    dosya = open(yol,"r",encoding="utf8",errors='ignore')
    lines = dosya.readlines()
    rand_line = random.randint(0,len(lines)-1)
    satir = (lines[rand_line])
    dosya.close()
    return satir.replace("\n","")

def numara_olustur():
    numara = random.randint(1000000,9999999)
    return ("0352"+str(numara))

def adres_olustur():
    lst=["MELİKGAZİ","KOCASİNAN"]
    mah = random.choice(lst)
    path=""
    if(mah=="MELİKGAZİ"):
        path = "melikgazi_mahalleleri.txt"
    elif(mah=="KOCASİNAN"):
        path = "kocasinan_mahalleleri.txt"
    return mah+"/"+satir_getir(path).replace("\n","")

ad = satir_getir("isimler.txt")
soyad = satir_getir("soyisimler.txt")
numara = numara_olustur()
adres = adres_olustur()
print(ad,soyad)
print(numara)   
print(adres)