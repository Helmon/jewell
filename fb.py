import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FBLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    #purpose : positive test insert 5 character    
    def test_login_kumparan_facebook_5_char(self):
        self.driver.get("https://kumparan.com/")
        driver = self.driver
        driver.find_element_by_id("onesignal-popover-cancel-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".btn-link[href='/login']").click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-fb").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        driver.find_element_by_id("email").send_keys("tlast7478@gmail.com")
        driver.find_element_by_name("pass").send_keys("lastlast")
        driver.find_element_by_id("u_0_0").click()
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        time.sleep(5)
        driver.find_element_by_css_selector(".panel-body.card-content .btn-block:nth-child(2)").click()
        time.sleep(5)
        for x in range(5):
            driver.find_element_by_xpath("//textarea[@placeholder='Tulis Komentarmu']").send_keys("a")
        time.sleep(3)
        driver.find_element_by_css_selector(".pull-right .btn-primary").click()
        driver.close()

    #purpose : negative test insert zero char    
    def test_login_kumparan_facebook_zero_char(self):
        self.driver.get("https://kumparan.com/")
        driver = self.driver
        driver.find_element_by_id("onesignal-popover-cancel-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".btn-link[href='/login']").click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-fb").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        driver.find_element_by_id("email").send_keys("tlast7478@gmail.com")
        driver.find_element_by_name("pass").send_keys("lastlast")
        driver.find_element_by_id("u_0_0").click()
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        time.sleep(5)
        driver.find_element_by_css_selector(".panel-body.card-content .btn-block:nth-child(2)").click()
        time.sleep(5)
        driver.find_element_by_xpath("//textarea[@placeholder='Tulis Komentarmu']").send_keys("")
        time.sleep(3)
        driver.find_element_by_css_selector(".pull-right .btn-primary").click()
        driver.close()

    #purpose : negative test insert special char    
    def test_login_kumparan_facebook_special_char(self):
        self.driver.get("https://kumparan.com/")
        driver = self.driver
        driver.find_element_by_id("onesignal-popover-cancel-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".btn-link[href='/login']").click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-fb").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        driver.find_element_by_id("email").send_keys("tlast7478@gmail.com")
        driver.find_element_by_name("pass").send_keys("lastlast")
        driver.find_element_by_id("u_0_0").click()
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        time.sleep(5)
        driver.find_element_by_css_selector(".panel-body.card-content .btn-block:nth-child(2)").click()
        time.sleep(5)
        driver.find_element_by_xpath("//textarea[@placeholder='Tulis Komentarmu']").send_keys("!@#")
        time.sleep(3)
        driver.find_element_by_css_selector(".pull-right .btn-primary").click()
        driver.close()    

if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F://report'))