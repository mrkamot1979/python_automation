from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class ListOfElements():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("There are " + str(length1))
            #print(elementListByClassName[0])
        else:
            print("No such class name")


nrtest = ListOfElements()
nrtest.test()