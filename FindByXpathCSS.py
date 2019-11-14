
from selenium import webdriver
from selenium.webdriver.common.by import By

import os

class FindByXPathCSS():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        url = "https://letskodeit.teachable.com/p/practice"
        driver.get(url)

        #elementByLinkText = driver.find_element_by_link_text('Login')
        elementByName = driver.find_elements(By.ID, "name")


        if elementByName is not None:
            print("Found the element by link text!")
        else:
            print("Wala")

        


rc = FindByXPathCSS()
rc.test()