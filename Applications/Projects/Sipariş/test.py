import sip_no_olustur as sno
import musteri_olustur as mo
import opengspn as og

sip_no = sno.siparis_no_olustur()
m_adi = mo.musteri_ad_olustur()
m_soyadi = mo.musteri_soyad_olustur()
m_tel = mo.numara_olustur()
m_adres = mo.adres_olustur()
model = mo.model_bul("BN59-01220D")


og.login_gspn("https://gspn1.samsungcsportal.com/")
og.go_management()