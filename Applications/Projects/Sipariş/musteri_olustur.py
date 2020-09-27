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
    mahalle = ""
    sokak = ""
    bina = "cad-sok-bina//bina.txt"
    if(mah=="MELIKGAZI"):
        mahalle = "mahalleler//melikgazi.txt"
        sokak = "cad-sok-bina//melikgazi.txt"
    elif(mah=="KOCASINAN"):
        mahalle = "mahalleler//kocasinan.txt"
        sokak = "cad-sok-bina//kocasinan.txt"
    elif(mah=="TALAS"):
        mahalle = "mahalleler//talas.txt"
        sokak = "cad-sok-bina//talas.txt"
    mcsb = (satir_getir(mahalle).replace("\n","")) + " " + (satir_getir(sokak).replace("\n","")) + " " + (satir_getir(bina).replace("\n",""))
    adres.insert(0, mah) 
    adres.insert(1, mcsb) 
    return adres

def musteri_ad_olustur():
    return satir_getir("musteriler//isimler.txt")

def musteri_soyad_olustur():
    return satir_getir("musteriler//soyisimler.txt")

def model_bul(kod):
    yol = "modeller//"+kod+".txt"
    return satir_getir(yol).replace("\t","")
