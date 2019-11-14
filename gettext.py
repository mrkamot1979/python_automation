from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

class gettext():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elemBtnOpenTab = driver.find_element_by_xpath("//a[@id='opentab']")
        getTextElemBtnOpenTab = elemBtnOpenTab.text

        print("The text of the element is " + getTextElemBtnOpenTab)


nr = gettext()
nr.test()