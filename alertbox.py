from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

class alertbox():

    def trigger(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        entertext = driver.find_element(By.XPATH, "//input[@id='name']").send_keys("ebak")
        time.sleep(20)

        clickalert = driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
        time.sleep(20)


nr = alertbox()
nr.trigger()