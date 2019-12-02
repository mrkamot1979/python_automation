from selenium import webdriver
import time, os
from selenium.webdriver.support.select import Select
from utilities.handywrappers import handrywrappers



class UsingWrappers1():

    def test(self):

        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)


        hw = HandyWrappers(driver)

        driver.implicitly_wait(10)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

ff = UsingWrappers1()
ff.test()

