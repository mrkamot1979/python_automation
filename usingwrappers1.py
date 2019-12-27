from selenium import webdriver
from utilities.handywrappers import handywrappers
from selenium.webdriver.common.by import By
import time, os




class UsingWrappers1():

    def test(self):

        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        #baseURL = "https://learn.letskodeit.com/p/practice"
        #baseURL = "https://globalexpress.rakuten.co.jp/?lang=en"
        baseURL = "https://global.rakuten.com/en/"
        driver.maximize_window()
        driver.implicitly_wait(10)

        hw = handywrappers(driver)

        driver.get(baseURL)



        """
        elementResult = hw.elementPresenceCheck(, By.ID)
        print(str(elementResult))
        
        """


        textField1 = hw.getElement("//div[@id='member']//a[@href='https://grp01.id.rakuten.co.jp/rms/nid/login?xbp=1&service_id=s266&lang=en&return_url=%2Fen%2F']", "xpath")
        textField1.click()
        time.wait(5)
        #textField1.click()
        #textField1.send_keys("Test")
        #time.sleep(2)

        #textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        #textField2.clear()
        #time.sleep(2)
        



nr = UsingWrappers1()
nr.test()


