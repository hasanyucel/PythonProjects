from os import path
import pathlib
root = str(pathlib.Path(__file__).parent.absolute())

dosyalar = ("captcha.py","musteri_olustur.py","sip_no_olustur.py",
"siparisler.txt","musteriler/isimler.txt","musteriler/soyisimler.txt","mahalleler/kocasinan.txt",
"mahalleler/melikgazi.txt","mahalleler/talas.txt","driver/chromedriver.exe")

klasorler = ("ariza","captchas","driver","mahalleler","modeller","musteriler")

def kontrol_dosya_klasor(yol):
    if(path.exists(root+"/"+yol)==False):
        print(root+"/"+yol+" dosyası/klasörü bulunamadı!")


def kontrol():
    for yol in dosyalar:
        kontrol_dosya_klasor(yol)
    for yol in klasorler:
        kontrol_dosya_klasor(yol)
