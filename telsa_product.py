from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

def clickIt(driver,element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.click(on_element=element)
    action.perform()

opts = Options()


agent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
opts.add_argument(agent)

driver = webdriver.Chrome(chrome_options=opts,executable_path='chromedriver.exe')
driver.get("https://www.tesla.com/inventory/used/ms?arrangeby=plh&zip=95113")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

total_sections = driver.find_elements(By.TAG_NAME,'article')
for main_article in total_sections:
    loc_main = main_article.location_once_scrolled_into_view
    print(main_article.text)
    time.sleep(.5)
    btns = main_article.find_elements(By.TAG_NAME,'button')
    for btn in btns:
        loc = btn.location_once_scrolled_into_view
        print(btn.text)
      
        if btn.text == 'VIEW DETAILS':
            clickIt(driver,btn)

    new_tab = webdriver.Chrome(chrome_options=opts,executable_path='chromedriver.exe')
    new_tab.get("https://www.tesla.com/ms/order/5YJSA1E68MF447661?postal=95113&coord=37.3326639,-121.8918364&titleStatus=used&redirect=no#overview")
    time.sleep(2)

    total_div = new_tab.find_elements(By.CLASS_NAME,'tds-list')
    for show in total_div:
        print(show.text,"==================================")
      
time.sleep(2)
