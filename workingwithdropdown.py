from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
from selenium.webdriver.support.select import Select

class workingwithdropdown():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        time.sleep(5)

nr = workingwithdropdown()
nr.test()