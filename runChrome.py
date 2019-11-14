
from selenium import webdriver
import os

class runChrome():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        url = "https://letskodeit.teachable.com/p/practice"
        driver.get(url)

        elementByID = driver.find_element_by_id("name")
        elementByTableID = driver.find_element_by_id("product")

        #elementbyName = driver.find_element_by_name("eenter-name")


        if elementByID is not None:
            print("We found an element by that ID!")
        else:
            print("Sorry element not found")

        if elementByTableID is not None:
            print("Found Table ID")

        


rc = runChrome()
rc.test()