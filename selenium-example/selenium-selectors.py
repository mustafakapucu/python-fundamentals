from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.options import ElementScrollBehavior

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)

driver.maximize_window()
# elem = driver.find_element(By.NAME, 'q')
elem = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')

elem.send_keys("python")
time.sleep(2)
elem.send_keys(Keys.ENTER)
time.sleep(2)


result = driver.find_elements(By.CSS_SELECTOR, ".repo-list-item a")

for element in result:
    print(element.text)



driver.close()
