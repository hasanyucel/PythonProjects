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

# Go to the followers tab of given username
def go_followers_page_of_user(nameOfUser):
    driver.get("https://github.com/{}?tab=followers".format(nameOfUser))
    time.sleep(3)

# Find the followers
def find_followers_of_user():
    users = driver.find_elements_by_xpath("//a[@data-hovercard-type='user']")
    temp = []
    for follower in users:
        temp.append(follower.get_attribute("href"))
    list_set = set(temp) 
    followers = (list(list_set))
    # Follow everyone who is following 'nameOfUser'
    for user in followers:
        for page in range(1, 5):
            string = "{}?page={}&tab=following".format(user, page)
            driver.get(string)
            time.sleep(3)

            follow_button = driver.find_elements_by_xpath("//input[@aria-label='Follow this person']")
            try:
                for i in follow_button:
                    i.submit()
            except:
                pass

    driver.close()

login_github("https://github.com/login")
go_followers_page_of_user("hasanyucel") #Enter a user to follow the followings of the users
find_followers_of_user()
