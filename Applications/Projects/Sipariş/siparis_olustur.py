import time
import sip_no_olustur as sno
import musteri_olustur as mo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def login_gspn(website):

    driver.get(website)
    Alert(driver).accept()

    time.sleep(5)
    driver.find_element_by_name("").send_keys(Keys.ENTER)
    time.sleep(5)
    
    username = driver.find_element_by_css_selector("#login_form_all > div.login_form > dl > dd.user_id > input")

    username.send_keys("user")


login_gspn("https://gspn1.samsungcsportal.com/")
