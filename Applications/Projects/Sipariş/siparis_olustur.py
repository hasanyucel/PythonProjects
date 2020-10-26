import time	
import sys	
import os	
import requests	
from PIL import Image	
import datetime	
from selenium import webdriver	
from selenium.webdriver.common.keys import Keys	
from selenium.webdriver.common.by import By	
from selenium.webdriver.common.alert import Alert	
from selenium.webdriver.support.ui import WebDriverWait	
from selenium.webdriver.support import expected_conditions as EC	
import sip_no_olustur as sno	
import musteri_olustur as mo	
import captcha as c

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")	
wait = WebDriverWait(driver, 15)	
ilk = 0
log = ""

def gspn_giris(website):
    global log 	
    driver.get(website)	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	
    username = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/dl/dd[1]/input""")))	
    password = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/dl/dd[2]/input""")))	
    usercr = kullanici_adi_sifre_getir()
    username.send_keys(Keys.CONTROL, "a")
    username.send_keys(Keys.BACKSPACE)
    username.send_keys(usercr[0])
    password.send_keys(usercr[1])
    log = log + " " + usercr[0]
    print(usercr[0])
    print(usercr[1])
    login_form = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/img""")))	
    login_form.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	

def yonetime_git():	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[2]""")))	
    yonetim = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="MAIN_04"]/span""")))	
    yonetim.click()	

def is_emri_olustur():	
    global ilk
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""//*[@id="leftMenus"]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""//*[@id="b2BLeftMenuScroll"]""")))	
    # st = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td"""))) #Favoriler	
    if(ilk==0):
        st = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr[10]/td""")))	
        st.click()	
        ilk = 1
    ie = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr[11]/td/table/tbody/tr[5]/td""")))	
    ie.click()	

def kullanici_adi_sifre_getir():	
    dosya = open("D:\\user2.txt","r",encoding="utf8")	
    satir = dosya.readline() 	
    print(satir)	
    return satir.split(",")	

def sip_no_doldur():
    global log 	
    sip_no = sno.siparis_no_olustur()	
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    sip_no_textbox = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[4]/td/div/table[1]/tbody/tr[1]/td[4]/input""")))	
    sip_no_textbox.send_keys(sip_no)
    log = log + " " + sip_no	

def musteri_ekle():	
    global log 
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    musteri_formu = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[6]/td/div/table[1]/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table/tbody/tr/td[2]/a""")))	
    musteri_formu.click()	
    name_surname_window = driver.window_handles[1]	
    driver.switch_to_window(name_surname_window)	
    yeni = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[3]/table[1]/tbody/tr/td[2]/table/tbody/tr/td[2]/a""")))	
    yeni.click()	
    m_adi = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[1]/td[2]/input[1]""")))
    musteri_adi = mo.musteri_ad_olustur()	
    m_adi.send_keys(musteri_adi)
    log = log + " " + musteri_adi	
    m_soyadi = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[1]/td[2]/input[2]""")))
    musteri_soyadi = mo.musteri_soyad_olustur()
    m_soyadi.send_keys(musteri_soyadi)	
    log = log + " " + musteri_soyadi
    m_tel = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[3]/td[2]/input[1]""")))
    musteri_telefon = mo.numara_olustur()
    m_tel.send_keys(musteri_telefon)
    log = log + " " + musteri_telefon
    m_il_ilce = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[8]/td[2]/a/img[1]""")))	
    m_il_ilce.click()	
    address_window = driver.window_handles[2]	
    driver.switch_to_window(address_window)	
    m_il = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[3]/table/tbody/tr[2]/td/table[1]/tbody/tr[2]/td[2]/input""")))	
    m_il.send_keys("KAYSERİ")	
    m_il_ara = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[3]/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td[5]/table/tbody/tr/td[2]/a""")))	
    m_il_ara.click()	

    adres = mo.adres_olustur()
    m_ilce = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[3]/table/tbody/tr[2]/td/table[3]/tbody[2]/tr[7]/td[13]""")))	
    if(adres[0]=="MELIKGAZI"):	
        m_ilce = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[3]/table/tbody/tr[2]/td/table[3]/tbody[2]/tr[7]/td[13]""")))	
    elif(adres[0]=="KOCASINAN"):	
        m_ilce = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[3]/table/tbody/tr[2]/td/table[3]/tbody[2]/tr[6]/td[13]"""))) #KOCASİNAN	
    elif(adres[0]=="TALAS"):	
        m_ilce = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[3]/table/tbody/tr[2]/td/table[3]/tbody[2]/tr[11]/td[13]""")))	

    m_ilce.click()	
    driver.switch_to_window(name_surname_window)	
    m_adres = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[6]/td[2]/input[1]""")))	
    m_adres.send_keys(adres[1])	
    m_kaydet = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[3]/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/a""")))	
    m_kaydet.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	
    m_ekle = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[3]/div[3]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/a""")))	
    m_ekle.click()	

def urun_bilgilerini_gir(malzeme_kodu):
    global log	
    driver.switch_to_window(driver.window_handles[0])	
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    model = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/input""")))	
    model_kodu = mo.model_bul(malzeme_kodu)
    log = log + " " + model_kodu + " " + malzeme_kodu
    model.send_keys(model_kodu)	
    model.send_keys(Keys.ENTER)	
    seri_no = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/input""")))	
    seri_no.send_keys("M000")	
    g_sorgula = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[3]/tbody/tr/td[3]/table/tbody/tr/td[2]/a""")))	
    try:	
        g_sorgula.click()	
        g_sorgula.click()	
        wait.until(EC.alert_is_present())	
        driver.switch_to_alert().accept()	
        time.sleep(1)	
        driver.switch_to_alert().accept()	
    except:	
        pass	
    s_tipi = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[8]/tbody/tr[1]/td[2]/select/option[2]""")))	
    s_tipi.click()	
    try:
        m_sikayet1 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[1]/select/option[13]""")))	
        m_sikayet1.click()
    except:	
        m_sikayet1 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[1]/select/option[2]""")))
        m_sikayet1.click()
    try:
        m_sikayet2 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[2]/select/option[5]""")))	
        m_sikayet2.click()
    except:	
        m_sikayet2 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[2]/select/option[2]""")))
        m_sikayet2.click()
    try:
        m_sikayet3 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[3]/select/option[2]""")))	
        m_sikayet3.click()
    except:
        m_sikayet3 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[3]/select/option[2]""")))	
        m_sikayet3.click()
    aciklama = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[12]/tbody/tr[2]/td[2]/input""")))	
    aciklama.send_keys("Emrah Beye Teslim Edilecek. HY")	
    talep = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[12]/tbody/tr[3]/td[2]/input""")))	
    # talep.send_keys("Arızalı. Çalışmıyor.")	
    ariza = mo.satir_getir("ariza/"+sno.kontrol_tur(malzeme_kodu))
    talep.send_keys(ariza)	
    s1 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[11]/td/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/img""")))	
    s1.click()	
    s2 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[11]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/img""")))	
    s2.click()	
    s3 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[11]/td/div/table/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/img""")))	
    s3.click()	
    teknisyen = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[11]/td/div/table/tbody/tr[4]/td[2]/select/option[5]""")))	
    teknisyen.click()	
    save = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[5]/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/a""")))	
    save.click()	
    #Alerti oku captcha istiyorsa çöz yoksa devam	
    captcha_kontrol()	
    update = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[5]/tbody/tr[2]/td[5]/table/tbody/tr/td[2]/a""")))	
    update.click()	

def parca_ekle_ve_iste(malzeme_kodu):	
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    bekliyor = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/div[13]/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/select/option[2]""")))	
    bekliyor.click()	
    pbekliyor = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/div[13]/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/select/option[10]""")))	
    pbekliyor.click()	
    pekle = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table[10]/tbody/tr/td[5]/table/tbody/tr/td[6]/table/tbody/tr/td[1]/a""")))	
    pekle.click()
    parca_ekle_window = driver.window_handles[1]	
    driver.switch_to_window(parca_ekle_window)
    try:
        wait.until(EC.alert_is_present())	
        driver.switch_to_alert().accept()	
        

    except:	
        pass	
    parca_ekle = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/table[1]/tbody/tr[1]/td/form/div[7]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/a""")))	
    parca_ekle.click()	
    parca = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[1]/td/form/div[7]/table[3]/tbody/tr/td[2]/input[1]""")))	
    parca.send_keys(malzeme_kodu)	
    adet = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[1]/td/form/div[7]/table[3]/tbody/tr/td[4]/input""")))	
    adet.send_keys("1")	
    kaydet = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/table[1]/tbody/tr[1]/td/form/div[7]/table[2]/tbody/tr/td[4]/table/tbody/tr/td[2]/a""")))	
    kaydet.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()
    driver.switch_to_window(driver.window_handles[0])	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    yeniistek = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/div[14]/table/tbody/tr/td/table/tbody/tr/td[8]/input""")))	
    yeniistek.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()
    log_yaz(log)	
    time.sleep(5)	

def captcha_kontrol():	
    global log
    wait.until(EC.alert_is_present())	
    alert = driver.switch_to_alert().text	
    print(alert)	
    while("Captcha" in alert):	
        driver.switch_to_alert().accept()	
        cap_name = ""+datetime.datetime.now().strftime("%Y%m%d-%H-%M-%S")	
        captcha_kaydet("/html/body/form[5]/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr/td[1]/div/img",cap_name)	
        try:
            cozulmus_captcha = c.captcha_solve("captchas/"+cap_name+".png")
            log = log + " " + cap_name + " " + cozulmus_captcha
        except:	
            log = log + " " + cap_name + " Captcha tarafında hata döndü!"
            print("Captcha tarafında hata döndü!")
            pass
        print(cozulmus_captcha)	
        cap_in = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/input[1]""")))	
        cap_in.send_keys(Keys.CONTROL, "a")
        cap_in.send_keys(Keys.BACKSPACE)
        cap_in.send_keys(cozulmus_captcha)	
        save = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[5]/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/a""")))	
        save.click()	
        wait.until(EC.alert_is_present())	
        alert = driver.switch_to_alert().text	
    else:
        driver.switch_to_alert().accept()	


def captcha_kaydet(xpath_id,pic_id): #img ile biten full xpathle ve captcha id göndermek yeterli olacaktır. 	
    # os.mkdir("captchas")	
    ele = driver.find_element_by_xpath(xpath_id)	
    loc1 = ele.location	
    driver.save_screenshot("captchas/"+pic_id+".png")	
    image = Image.open("captchas/"+pic_id+".png")	
    left = loc1['x']	
    top = loc1['y']	
    right = loc1['x'] + 480	
    bottom1 = loc1['y'] + 137	
    image = image.crop((left,top,right,bottom1))	
    image = image.crop((240,90,480,137))	
    image.save("captchas/"+pic_id+".png")  
    # image2.save("captchas/test.png")  	

def log_yaz(log2):
    with open("log.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        file_object.write(log2)
    global log
    log = ""

def tarayici_kapat():	
    driver.close()	
    driver.quit() 