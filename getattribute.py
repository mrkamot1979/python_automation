from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

class getattribute():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("alertbtn")
        result = element.get_attribute("type")

        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()
        """
        element = driver.find_element_by_id("opentab")
        getAttributeElement = element.get_attribute("type")

        print("The attribute is " + str(getAttributeElement))

        """

nr = getattribute()
nr.test()