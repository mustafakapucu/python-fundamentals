from instagramUserInfo import username, pasword
from selenium import webdriver
import time

class Instagram:
    def __init__(self,username,password) :
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        


        