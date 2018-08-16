import unittest
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
# chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome()
driver.get("http://taliwang:3000/")

# switch window 1 

# window_before = driver.window_handles[0]
# print(window_before)
# driver.find_element_by_xpath('id("root")/div[@class="App"]/div[@class="Login"]/div[@class="ui center aligned middle aligned grid Login-grid"]/div[@class="column Login-column"]/div[@class="Login-box"]/button[@class="ui google plus large button"]/i[@class="google icon"]').click()
# window_after = driver.window_handles[1]
# driver.switch_to_window(window_after)
# print(window_after)
# time.sleep(3)
# driver.find_element_by_id("identifierId").send_keys("helmon.pirie@shopee.com")
# driver.find_element_by_id("identifierNext").click()
# driver.find_element_by_name("password").send_keys("jewelljerrome")
# driver.find_element_by_id("passwordNext").click()
# time.sleep(3)

# switch window 2
driver.find_element_by_xpath('id("root")/div[@class="App"]/div[@class="Login"]/div[@class="ui center aligned middle aligned grid Login-grid"]/div[@class="column Login-column"]/div[@class="Login-box"]/button[@class="ui google plus large button"]/i[@class="google icon"]').click()
driver.switch_to_window(driver.window_handles[-1])
title=driver.title
time.sleep(2)
driver.find_element_by_id("identifierId").send_keys("helmon.pirie@shopee.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(1)
driver.find_element_by_name("password").send_keys("jewelljerrome")
driver.find_element_by_id("passwordNext").click()
# driver.find_element_by_id("totpPin")
time.sleep(10)
driver.find_element_by_id("totpNext").click()
# driver.switch_to_window(driver.window_handles[1])
# title=driver.title
time.sleep(10)
driver.find_element_by_class_name("dropdown icon")
time.sleep(2)


# driver.switch_to_window(driver.window_handles[-1])
# title=driver.title

# driver.find_element_by_class_name("identifier").send_keys("helmon.pirie@shopee.com")
# driver.find_element_by_id("identifierNext").click()
# driver.find_element_by_name("password").send_keys("jewelljerrome")
# driver.find_element_by_id("passwordNext").click()