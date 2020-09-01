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
# from selenium.webdriver import ChromeOptions	
import sip_no_olustur as sno	
import musteri_olustur as mo	
import captcha as c	

# chrome_options = webdriver.ChromeOptions()	
# prefs = {"profile.default_content_setting_values.notifications" : 1}	
# chrome_options.add_experimental_option("prefs",prefs)	
# driver = webdriver.Chrome(chrome_options=chrome_options)	


driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")	
wait = WebDriverWait(driver, 20)	

def gspn_giris(website):	
    driver.get(website)	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	
    username = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/dl/dd[1]/input""")))	
    password = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/dl/dd[2]/input""")))	
    usercr = kullanici_adi_sifre_getir()	
    username.send_keys(usercr[0])	
    password.send_keys(usercr[1])	
    login_form = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/img""")))	
    login_form.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	

def yonetime_git():	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[2]""")))	
    yonetim = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="MAIN_04"]/span""")))	
    yonetim.click()	

def is_emri_olustur():	
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""//*[@id="leftMenus"]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""//*[@id="b2BLeftMenuScroll"]""")))	
    st = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td"""))) #Favoriler	
    # ev = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/img[1]""")))	
    # ev.click()	
    # st = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr[10]/td""")))	
    st.click()	
    # ie = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table/tbody/tr[11]/td/table/tbody/tr[5]/td""")))	
    # ie.click()	

def kullanici_adi_sifre_getir():	
    dosya = open("D:\\user.txt","r",encoding="utf8")	
    satir = dosya.readline() 	
    # print(line)	
    return satir.split(",")	

def sip_no_doldur():	
    sip_no = sno.siparis_no_olustur()	
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    sip_no_textbox = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[4]/td/div/table[1]/tbody/tr[1]/td[4]/input""")))	
    sip_no_textbox.send_keys(sip_no)	

def musteri_ekle():	
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
    m_adi.send_keys(mo.musteri_ad_olustur())	
    m_soyadi = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[1]/td[2]/input[2]""")))	
    m_soyadi.send_keys(mo.musteri_soyad_olustur())	
    m_tel = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/table[1]/tbody/tr[2]/td/form[5]/div/table/tbody/tr[3]/td[2]/input[1]""")))	
    m_tel.send_keys(mo.numara_olustur())	
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
    driver.switch_to_window(driver.window_handles[0])	
    driver.switch_to_default_content()	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/frameset/frame[3]""")))	
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"""/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/iframe""")))	
    model = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/input""")))	
    model.send_keys(mo.model_bul(malzeme_kodu))	
    model.send_keys(Keys.ENTER)	
    seri_no = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/input""")))	
    seri_no.send_keys("M000")	
    g_sorgula = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[3]/tbody/tr/td[3]/table/tbody/tr/td[2]/a""")))	
    try:	
        g_sorgula.click()	
        g_sorgula.click()	
        wait.until(EC.alert_is_present())	
        driver.switch_to_alert().accept()	
        # time.sleep(5)	
        wait.until(EC.alert_is_present())	
        driver.switch_to_alert().accept()	
    except:	
        pass	
    s_tipi = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[8]/tbody/tr[1]/td[2]/select/option[2]""")))	
    s_tipi.click()	
    m_sikayet1 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[1]/select/option[13]""")))	
    m_sikayet1.click()	
    m_sikayet2 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[2]/select/option[5]""")))	
    m_sikayet2.click()	
    m_sikayet3 = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[11]/tbody/tr/td[2]/table/tbody/tr/td[3]/select/option[2]""")))	
    m_sikayet3.click()	
    aciklama = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[12]/tbody/tr[2]/td[2]/input""")))	
    aciklama.send_keys("Emrah Beye Teslim Edilecek. HY")	
    talep = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[4]/tbody/tr[9]/td/div/table[1]/tbody/tr/td/table[12]/tbody/tr[3]/td[2]/input""")))	
    talep.send_keys("Arızalı. Çalışmıyor.")	
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
    # wait.until(EC.alert_is_present())	
    # driver.switch_to_alert().accept()	
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
    pekle = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table[10]/tbody/tr/td[5]/table/tbody/tr/td[10]/table/tbody/tr/td[1]/a""")))	
    pekle.click()	
    parca = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/div[14]/table/tbody/tr/td/table/tbody/tr/td[4]/input[2]""")))	
    parca.send_keys(malzeme_kodu)	
    adet = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/div[14]/table/tbody/tr/td/table/tbody/tr/td[6]/input""")))	
    adet.send_keys("1")	
    save = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/div[4]/input[3]""")))	
    save.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	
    yeniistek = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/div[14]/table/tbody/tr/td/table/tbody/tr/td[8]/input""")))	
    yeniistek.click()	
    wait.until(EC.alert_is_present())	
    driver.switch_to_alert().accept()	
    time.sleep(5)	

def captcha_kontrol():	
    wait.until(EC.alert_is_present())	
    alert = driver.switch_to_alert().text	
    print(alert)	
    while("Captcha" in alert):	
        driver.switch_to_alert().accept()	
        cap_name = ""+datetime.datetime.now().strftime("%Y%d%m-%H-%M-%S")	
        captcha_kaydet("/html/body/form[5]/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr/td[1]/div/img",cap_name)	
        # a = c.captcha_solve("captchas/"+cap_name+".png")	
        # print(a)	
        # cap_in = wait.until(EC.presence_of_element_located((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/input[1]""")))	
        # cap_in.send_keys(a)	
        # save = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/form[5]/table/tbody/tr[1]/td[1]/table[5]/tbody/tr[1]/td[3]/table/tbody/tr/td[2]/a""")))	
        # save.click()	
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

# def test(website,pic_id):	
#     driver.get(website)	
#     captcha_kaydet("/html/body/img",""+datetime.datetime.now().strftime("%Y%d%m-%H-%M-%S"))	

def tarayici_kapat():	
    driver.close()	
    driver.quit() 