import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.tesla.com/inventory/used/ms?arrangeby=plh&zip=95113")
driver.maximize_window()
time.sleep(5.5)
previous_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == previous_height:
        break
    previous_height = new_height
article = driver.find_elements(By.TAG_NAME,'article')
for bt in article:
    print(bt.text,"===================")
    

   





