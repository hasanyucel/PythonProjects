import sqlite3
import datetime

db_name = "gunluk_sip_no.db"

def db_olustur():
    db = sqlite3.connect(db_name)
    imlec = db.cursor()
    imlec.execute("CREATE TABLE IF NOT EXISTS counter(tarih text, sip_sayisi int)") 
    db.commit()
    db.close()

def tarihi_kontrol_et():
    db_olustur()
    result = 0
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
        records = imlec.fetchone()
        result = records[0] + 1
        imlec.execute("UPDATE counter set sip_sayisi = ? where tarih = ?", (result,trh))
        sonuc = trh+"MS"+str("{:02d}".format(result))
    db.commit()
    db.close()
    return sonuc

sip_no = tarihi_kontrol_et()
print(sip_no)