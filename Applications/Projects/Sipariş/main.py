import siparis_olustur as sa
import kontrol as k
import time
import pathlib

root = str(pathlib.Path(__file__).parent.absolute())

def start():
    k.kontrol()
    sa.gspn_giris("https://gspn1.samsungcsportal.com/")
    sa.yonetime_git()
    with open(root+"/"+"siparisler.txt") as dosya: 
        for satir in dosya:
            sa.is_emri_olustur()
            sa.sip_no_doldur()
            sa.musteri_ekle()
            sa.urun_bilgilerini_gir(satir.strip())
            sa.parca_ekle_ve_iste(satir.strip())
            time.sleep(60)
    # sa.tarayici_kapat()

start()