import siparis_olustur as sa
import kontrol as k
import time

def start():
    k.kontrol()
    sa.gspn_giris("https://gspn1.samsungcsportal.com/")
    time.sleep(5)
    sa.yonetime_git()
    time.sleep(5)
    with open("siparisler.txt") as dosya: 
        for satir in dosya:
            sa.is_emri_olustur()
            sa.sip_no_doldur()
            time.sleep(5)
            sa.musteri_ekle()
            time.sleep(30)
            sa.urun_bilgilerini_gir(satir.strip())
            time.sleep(30)
            sa.parca_ekle_ve_iste(satir.strip())
            time.sleep(15)
    # sa.tarayici_kapat()

start()