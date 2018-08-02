# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Python_call_comment(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Python_call_comment(self):
        success = True
        wd = self.wd
        wd.get("http://192.168.130.245:8080/GPLine/GPLineGray.html")
        wd.find_element_by_id("loginField-input").click()
        wd.find_element_by_id("loginField-input").clear()
        wd.find_element_by_id("loginField-input").send_keys("super")
        wd.find_element_by_id("passField-input").click()
        wd.find_element_by_id("passField-input").clear()
        wd.find_element_by_id("passField-input").send_keys("1")
        wd.find_element_by_css_selector("td.com-sencha-gxt-theme-base-client-frame-TableFrame-TableFrameStyle-top").click()
        wd.find_element_by_xpath("//div[@class='top-area']/div[1]/div[2]/div[1]/div/div[1]/div/div[1]").click()
        wd.find_element_by_css_selector("div.com-sencha-gxt-theme-base-client-field-DateCellDefaultAppearance-DateCellStyle-trigger").click()
        wd.find_element_by_link_text("31").click()
        wd.find_element_by_xpath("//div[@id='x-auto-85']/div/table/tbody/tr/td[2]/div").click()
        wd.find_element_by_link_text("31").click()
        wd.find_element_by_xpath("//div[@class='com-sencha-gxt-theme-gray-client-tabs-GrayTabPanelAppearance-GrayTabPanelStyle-tab']/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div/div[11]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/img").click()
        wd.find_element_by_css_selector("div.com-sencha-gxt-theme-base-client-grid-CheckBoxColumnDefaultAppearance-CheckBoxColumnStyle-rowChecker").click()
        wd.find_element_by_id("x-auto-92-input").click()
        wd.find_element_by_id("x-auto-92-input").clear()
        wd.find_element_by_id("x-auto-92-input").send_keys("комеентарий")
        wd.find_element_by_xpath("//div[@class='com-sencha-gxt-theme-gray-client-tabs-GrayTabPanelAppearance-GrayTabPanelStyle-tab']/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/table/tbody/tr/td/table/tbody/tr/td[3]/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/div").click()
        wd.find_element_by_css_selector("div.com-sencha-gxt-core-client-dom-Mask-MaskDefaultAppearance-MaskStyle-mask").click()
        wd.find_element_by_xpath("//div[@class='com-sencha-gxt-theme-base-client-container-HBoxLayoutDefaultAppearance-HBoxLayoutStyle-container']/div/img").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
