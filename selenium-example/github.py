from selenium.webdriver.common import by
from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        self.usernameForFollowers = "umutluoglu"
        # self.usernameForFollowers = "mustafakapucu"

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(
            By.ID, "login_field").send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.NAME, "commit").click()

    def getFollowers(self):
        self.browser.get(
            "https://github.com/{}?tab=followers".format(self.usernameForFollowers))
        time.sleep(2)

        self.loadFollowers()

        try:
            if not self.browser.find_element(By.CLASS_NAME, "pagination"):
                pass
            else:
                while True:
                    links = self.browser.find_element(
                        By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "a")

                    if len(links) == 1:
                        if links[0].text == "Next":
                            links[0].click()
                            time.sleep(1)
                            self.loadFollowers()

                        else:
                            break
                    else:
                        for link in links:
                            if link.text == "Next":
                                link.click()
                                time.sleep(1)
                                self.loadFollowers()
                            else:
                                continue

        except:
            pass

    def closeBrowser(self):
        self.browser.close()

    def loadFollowers(self):
        items = self.browser.find_elements(
            By.CSS_SELECTOR, ".d-table.table-fixed")
        for i in items:
            self.followers.append(i.find_element(
                By.CSS_SELECTOR, ".Link--secondary").text)


github = Github(username=username, password=password)
github.signIn()
github.getFollowers()
github.closeBrowser()
print("Takipçi Sayısı : ", len(github.followers))
print(github.followers)
