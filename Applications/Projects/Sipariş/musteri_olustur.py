import random

def satir_getir(yol):
    dosya = open(yol,"r",encoding="utf8",errors='ignore')
    satirlar = dosya.readlines()
    rasgele_satir = random.randint(0,len(satirlar)-1)
    satir = (satirlar[rasgele_satir])
    dosya.close()
    return satir.replace("\n","")

def numara_olustur():
    numara = random.randint(1000000,9999999)
    return ("0352"+str(numara))

def adres_olustur():
    adres = []
    lst=["MELIKGAZI","KOCASINAN","TALAS"]
    mah = random.choice(lst)
    yol=""
    if(mah=="MELIKGAZI"):
        yol = "mahalleler//melikgazi.txt"
    elif(mah=="KOCASINAN"):
        yol = "mahalleler//kocasinan.txt"
    elif(mah=="TALAS"):
        yol = "mahalleler//talas.txt"
    adres.insert(0, mah) 
    adres.insert(1, satir_getir(yol).replace("\n","")) 
    return adres

def musteri_ad_olustur():
    return satir_getir("musteriler//isimler.txt")

def musteri_soyad_olustur():
    return satir_getir("musteriler//soyisimler.txt")

def model_bul(kod):
    yol = "modeller//"+kod+".txt"
    return satir_getir(yol).replace("\t","")
