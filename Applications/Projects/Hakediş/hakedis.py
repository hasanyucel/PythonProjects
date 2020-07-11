import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from keyboard import press

driver = webdriver.Chrome()

def login_gspn(website):
    driver.get(website)
    Alert(driver).accept()
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/dl/dd[1]/input""")))
    password = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/dl/dd[2]/input""")))
    usercr = get_username_password()
    username.send_keys(usercr[0])
    password.send_keys(usercr[1])
    login_form = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="login_form_all"]/div[1]/img""")))
    login_form.click()
    Alert(driver).accept()
    driver.switch_to_frame("menu")
    management = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="MAIN_04"]/span""")))
    management.click()

    time.sleep(5)
    driver.switch_to_default_content()
    time.sleep(1)
    driver.switch_to_frame("body")
    time.sleep(1)
    driver.switch_to_frame("leftMenus")
    time.sleep(1)
    driver.switch_to_frame("b2BLeftMenuScroll")
    time.sleep(1)
    
    html = driver.page_source
    print(html)

def get_username_password():
    dosya = open("D:\\user.txt","r",encoding="utf-8")
    line = dosya.readline() 
    print(line)
    return line.split(",")

login_gspn("https://gspn1.samsungcsportal.com/")
