import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from user_credentials import user, passw

driver = webdriver.Chrome()
followers = []
# Initializing the headless chrome with given website
def login_github(website):

    driver.get(website)
    wait = WebDriverWait(driver, 10)
    # Locating username and password field
    username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    # password and username need to go into these values
    username.send_keys(user)
    password.send_keys(passw)
    # Clicking the sign in button
    login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
    login_form.click()


# Unfollow users
def unfollow(user,numOfFollowings):
    driver.get("https://github.com/{}?tab=following".format(user))
    time.sleep(3)
    arrrange = int(numOfFollowings / 50)
    for page in range(1, arrrange):
        string = "https://github.com/{}?page={}&tab=following".format(user, page)
        driver.get(string)
        time.sleep(3)

        unfollow_button = driver.find_elements_by_xpath("//input[@aria-label='Unfollow this person']")
        try:
            for i in unfollow_button:
                i.click()
        except:
            pass

    driver.close()

login_github("https://github.com/login")
unfollow("hasanyucel",3300)
