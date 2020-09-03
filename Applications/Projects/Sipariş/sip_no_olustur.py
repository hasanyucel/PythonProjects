import sqlite3
import datetime

db_name = "gunluk_sip_adedi.db"

def db_olustur():
    db = sqlite3.connect(db_name)
    imlec = db.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS counter(tarih text, sip_sayisi int)") 
    imlec.execute("CREATE TABLE IF NOT EXISTS model_tur(model TEXT,tur TEXT,PRIMARY KEY(model))")
    db.commit()
    db.close()

def siparis_no_olustur():
    db_olustur()
    gecici_degisken = 0
    sonuc = ""
    x = datetime.datetime.now()
    trh = (x.strftime("%d-%m-%Y")).replace("-","")
    db = sqlite3.connect(db_name)
    imlec = db.cursor()
    # tarih databasede varmı kontrol et
    imlec.execute("SELECT * FROM counter WHERE tarih=?", (trh,))
    row = imlec.fetchone()
    # yoksa tarihi ve 1 sayisi insert et return 1
    if row is None:
        imlec.execute('INSERT INTO counter VALUES(?,?)',(trh,1))
        sonuc = trh+"MS01"
    # varsa sip_sayisinin değişkenini al bir arttır update et return sip_sayisi+1
    else:
        imlec.execute("SELECT sip_sayisi FROM counter WHERE tarih=?", [trh])
        kayitlar = imlec.fetchone()
        gecici_degisken = kayitlar[0] + 1
        imlec.execute("UPDATE counter set sip_sayisi = ? where tarih = ?", (gecici_degisken,trh))
        sonuc = trh+"MS"+str("{:02d}".format(gecici_degisken))
    db.commit()
    db.close()
    return sonuc

def kontrol_tur(model):
    db_olustur()
    db = sqlite3.connect(db_name)
    imlec = db.cursor()
    imlec.execute("SELECT tur FROM model_tur WHERE model=?", (model,))
    tur = imlec.fetchall()
    db.commit()
    db.close()
    return tur[0][0]+".txt"