import siparis_olustur as sa

with open("siparisler.txt") as dosya: 
    for satir in dosya:
        sa.gspn_giris("https://gspn1.samsungcsportal.com/")
        sa.yonetime_git()
        sa.is_emri_olustur()
        sa.sip_no_doldur()
        sa.musteri_ekle()
        sa.urun_bilgilerini_gir(satir.strip())