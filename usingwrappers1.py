from selenium import webdriver
from utilities.handywrappers import handywrappers
from selenium.webdriver.common.by import By
import time, os




class UsingWrappers1():

    def test(self):

        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.implicitly_wait(10)

        hw = handywrappers(driver)

        driver.get(baseURL)

        elementResult = hw.elementPresenceCheck("name", By.ID)
        print(str(elementResult))


        """
        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()
        time.sleep(2)
        """

nr = UsingWrappers1()
nr.test()

