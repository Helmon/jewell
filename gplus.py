import unittest
# import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GplusLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    #purpose : positive test insert 5 character    
    def test_login_kumparan_glus_5_char(self):
        self.driver.get("https://kumparan.com/")
        driver = self.driver
        driver.find_element_by_id("onesignal-popover-cancel-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".btn-link[href='/login']").click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-gplus").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        driver.find_element_by_id("identifierId").send_keys("tlast7478@gmail.com")
        driver.find_element_by_id("identifierNext").click()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("lastlast")
        driver.find_element_by_id("passwordNext").click()
        driver.switch_to_window(driver.window_handles[-2])
        title=driver.title
        time.sleep(5)
        driver.find_element_by_css_selector(".panel-body.card-content .btn-block:nth-child(2)").click()
        time.sleep(5)
        for x in range(5):
            driver.find_element_by_xpath("//textarea[@placeholder='Tulis Komentarmu']").send_keys("a")
        time.sleep(3)
        driver.find_element_by_css_selector(".pull-right .btn-primary").click()
        driver.close()

    #purpose : negative test insert zero character
    def test_login_kumparan_zero_char(self):
        self.driver.get("https://kumparan.com/")
        driver = self.driver
        driver.find_element_by_id("onesignal-popover-cancel-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".btn-link[href='/login']").click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-gplus").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        driver.find_element_by_id("identifierId").send_keys("tlast7478@gmail.com")
        driver.find_element_by_id("identifierNext").click()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("lastlast")
        driver.find_element_by_id("passwordNext").click()
        driver.switch_to_window(driver.window_handles[-2])
        title=driver.title
        time.sleep(3)
        time.sleep(5)
        driver.find_element_by_css_selector(".panel-body.card-content .btn-block:nth-child(2)").click()
        time.sleep(5)
        driver.find_element_by_xpath("//textarea[@placeholder='Tulis Komentarmu']").send_keys(" ")
        driver.find_element_by_css_selector(".pull-right .btn-primary").click()
        driver.close()

    #purpose : negative test insert special character
    def test_login_kumparan_special_char(self):
        self.driver.get("https://kumparan.com/")
        driver = self.driver
        driver.find_element_by_id("onesignal-popover-cancel-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".btn-link[href='/login']").click()
        time.sleep(3)
        driver.find_element_by_class_name("btn-gplus").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        title=driver.title
        driver.find_element_by_id("identifierId").send_keys("tlast7478@gmail.com")
        driver.find_element_by_id("identifierNext").click()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("lastlast")
        driver.find_element_by_id("passwordNext").click()
        driver.switch_to_window(driver.window_handles[-2])
        title=driver.title
        time.sleep(5)
        driver.find_element_by_css_selector(".panel-body.card-content .btn-block:nth-child(2)").click()
        time.sleep(5)
        driver.find_element_by_xpath("//textarea[@placeholder='Tulis Komentarmu']").send_keys("!@")
        time.sleep(3)
        driver.find_element_by_css_selector(".pull-right .btn-primary").click()
        driver.close()

# if __name__ == "__main__":
#         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F://report'))