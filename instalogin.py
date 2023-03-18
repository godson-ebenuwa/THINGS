from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

os.environ['PATH'] += r"C:/Users/godso/Downloads/chromedriver"
driver = webdriver.Chrome()

name = input("Enter your username: ")
pas = input("Enter your password: ")




class InstaBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        driver.get("https://www.instagram.com/login")
        time.sleep(3)

        User = driver.find_element(By.XPATH,
               '// * [ @ id = "loginForm"] / div / div[1] / div / label / input')

        User.send_keys(self.username)
        time.sleep(3)
        Pass = driver.find_element(By.XPATH,
                                       '//*[@id="loginForm"]/div/div[2]/div/label/input')
        Pass.send_keys(self.password)
        time.sleep(3)
        driver.find_element(By.XPATH,
                        '//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(10)

godson = InstaBot(name, pas)
godson.login()