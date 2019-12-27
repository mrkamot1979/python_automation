from selenium import webdriver
from utilities.handywrappers import handywrappers
from selenium.webdriver.common.by import By
import time, os

class dynamicxpath():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://letskodeit.teachable.com/"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)


        hw = handywrappers(driver)
        btnLogin = hw.getElement("//a[@class='navbar-link fedora-navbar-link']", "xpath")
        btnLogin.click()
        time.sleep(10)



# //div[@class='course-listing-title']


nr = dynamicxpath()
nr.test()