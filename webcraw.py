import unittest
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")

chrome_driver = 'C:\\Python35\\selenium\\chromedriver.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.tokopedia.com/ramadan/pemenang/")

test2 = driver.find_elements_by_xpath("//meta[@property]")
test = driver.find_elements_by_xpath("//img[@src]")
#print(test.get_attribute("property"))
for i in range(len(test)):
    img = test[i].get_attribute("src") 
    if "ecs7.tokopedia.net" in img :
        print("images posted from " + img)
    elif "ecs7.tokopedia.net" not in img :
        print("images posted from " + img)    
    elif " " in img :
        print("all images not posted from any server !")
print ('======================= END ECS CHECK ===================================')

print('\n')
hit = len(test2)
if hit == 0:
    print("\033[31m"+"OG not Detected!!!")      
for i in range(hit):
    meta = test2[i]
    content = meta.get_attribute("content")
    content = content.encode("ascii","ignore")
    content = content.decode("utf-8")
    prop = meta.get_attribute("property")
    if "og:" in prop:
        print("og detected " + prop)
        print("content = " + content)
    else :
        print("\033[31m"+"OG Blank!!! ")

driver.quit()