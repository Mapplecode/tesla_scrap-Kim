from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

def clickIt(driver,element):
    action = ActionChains(driver)

    # click the item
    action.move_to_element(element)
    action.click(on_element=element)

    # perform the operation
    action.perform()

def hoverIt(driver,element):
    action = ActionChains(driver)

    # click the item
    action.move_to_element(element)

    # perform the operation
    action.perform()

opts = Options()
agent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
opts.add_argument(agent)
driver = webdriver.Chrome(chrome_options=opts,executable_path='chromedriver.exe')
driver.get("https://www.tesla.com/inventory/used/ms?arrangeby=plh&zip=95113")
driver.maximize_window()
time.sleep(2)
total_sections = driver.find_elements(By.TAG_NAME,'article')
print(len(total_sections))

for main_article in total_sections:
    print(main_article.text)
    loc_main = main_article.location_once_scrolled_into_view
    hoverIt(driver,main_article)
    time.sleep(.5)
    btns = main_article.find_elements(By.TAG_NAME,'button')
    for btn in btns:
        loc = btn.location_once_scrolled_into_view
        print(btn.text)
        if btn.text == 'VIEW DETAILS':
            clickIt(driver,btn)
        print(len(driver.window_handles))

time.sleep(5)
driver.quit()