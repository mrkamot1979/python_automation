from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class interacting_with_elements():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        bmwBtn = driver.find_element(By.ID, "bmwradio")
        bmwBtn.click()

        bmwChk = driver.find_element(By.ID, "bmwcheck")
        bmwChk.click()

        benzChk = driver.find_element(By.XPATH,"//div[@class='right-align']//input[@id='benzcheck']")
        benzChk.click()


        time.sleep(10)

        print("BMW radio button is clicked? " + str(bmwBtn.is_selected()))
        print("Benz check button is checked? " + str(benzChk.is_selected()))
        print("BMW check button is checked?" + str(bmwChk.is_selected()))


nrebak = interacting_with_elements()
nrebak.test()