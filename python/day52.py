from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


USERNAME = "username"
PASSWORD = "password"

class InstaFollower():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)

        input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        input.send_keys(USERNAME,Keys.TAB,PASSWORD)
        time.sleep(3)

        sign_in = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
        sign_in.click()

        time.sleep(20)

    def find_followers(self):
        #in this we get xpath of search and search for account
        #go to followers 
        pass

    def follow(self):
        #in this we find all follow element button 
        #we use for loop to loop through each item 
        #and click on it
        pass



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()