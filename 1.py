from argparse import Action
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options




opts = Options()
agent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
opts.add_argument(agent)
driver = webdriver.Chrome(chrome_options=opts,executable_path='chromedriver.exe')

driver.get("https://www.tesla.com/inventory/used/ms?arrangeby=plh&zip=95113")
# driver.maximize_window()
driver.set_window_size(625, 11003)
time.sleep(5.5)

def clickIt(driver,element):
    action = ActionChains(driver)

    # click the item
    action.move_to_element(element)
    action.click(on_element=element)

    # perform the operation
    action.perform()


def hoverIt(driver,element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.perform()




action = ActionChains(driver)



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


    section_get = bt.find_elements(By.XPATH,"//*[@id='iso-container']/div/div[1]/main/div/article[1]/section[4]")
    for show_section in section_get:
  

        get_div = show_section.find_elements(By.XPATH,"//*[@id='iso-container']/div/div[1]/main/div/article[1]/section[4]/div[1]")
        for show_div in get_div:
        

            get_button_class = show_div.find_elements(By.XPATH,"//*[@id='iso-container']/div/div[1]/main/div/article[1]/section[4]/div[1]")
            for show_button_class in get_button_class:
          


                show_all_btn =show_button_class.find_elements(By.XPATH,"//*[@id='iso-container']/div/div[1]/main/div/article[1]/section[4]/div[1]/button[2]")
                for show_bt in show_all_btn:
                    # hoverIt(driver,bt)
                    print(show_bt.text,"==================================")


                    action.move_to_element(bt).move_to_element(show_section).move_to_element(show_div).move_to_element(show_button_class).move_to_element(show_bt).click().perform()
                  
       




   
  





    









