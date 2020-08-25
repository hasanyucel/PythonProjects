import siparis_olustur as sa
import time

sa.gspn_giris("https://gspn1.samsungcsportal.com/")
sa.yonetime_git()
with open("siparisler.txt") as dosya: 
    for satir in dosya:
        time.sleep(5)
        sa.is_emri_olustur()
        sa.sip_no_doldur()
        sa.musteri_ekle()
        sa.urun_bilgilerini_gir(satir.strip())