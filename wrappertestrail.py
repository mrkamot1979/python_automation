from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handywrappers import handywrappers
import time, os

class wrappertestrail():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://rakuten.testrail.com "
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        hw = handywrappers(driver)

        username = hw.getElement("name")
        username.send_keys("rogelio.roldan@rakuten.com")
        time.sleep(10)
        pword = hw.getElement("password")
        pword.send_keys("ebak")
        time.sleep(10)

thet = wrappertestrail()
thet.test()