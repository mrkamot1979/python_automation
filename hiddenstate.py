from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

class hiddenstate():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(5)

        """
        #find the element
        elementInputLine = driver.find_element_by_id("displayed-text")
        enterElementInputLine = elementInputLine.send_keys("ebak")

        if elementInputLine.is_displayed():
            print("The element is displayed")
            time.sleep(5)
            elementHideButton = driver.find_element_by_id("hide-textbox").click()
            time.sleep(5)
            showElementHide = driver.find_element_by_id("show-textbox").click()
            time.sleep(5)

        
        """

    def expedia(self):
         driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
         os.environ["webdriver.chrome.driver"] = driverLocation
         driver = webdriver.Chrome(driverLocation)
         expedbaseURL = "https://www.expedia.com"

         driver.maximize_window()
         driver.get(expedbaseURL)
         driver.implicitly_wait(10)

         findFlightButton = driver.find_element(By.XPATH,"//button[@id='tab-flight-tab-hp']")
         clickFlightButton = findFlightButton.click()
         time.sleep(2)

         clickDropdown = driver.find_element(By.XPATH, "//div[@id='traveler-selector-hp-flight']//button[@class='trigger-utility menu-trigger btn-utility btn-secondary dropdown-toggle theme-standard pin-left menu-arrow gcw-component gcw-traveler-amount-select gcw-component-initialized']").click()
         time.sleep(5)





nr = hiddenstate()
nr.expedia()