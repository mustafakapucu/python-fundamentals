from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://github.com/"

driver.get(url=url)
time.sleep(3)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")
print("title:", driver.title)
time.sleep(2)

url = "https://github.com/mustafakapucu"
driver.get(url=url)
time.sleep(3)

if "mustafakapucu" in driver.title:
    driver.save_screenshot("github.com-mustafakapucu.png")
driver.back()
time.sleep(2)

driver.close()
