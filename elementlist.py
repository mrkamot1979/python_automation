import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By

class elementList():

    def getElementList(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        #find element list and count them
        carElementList = driver.find_elements(By.XPATH, "//input[contains(@id, 'radio') and contains(@name,'car')]")
        size = len(carElementList)
        print("The element list length is " + str(size))

        for radioButton in carElementList:
            print(radioButton)

        """
        isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

        
        
        #select the first element
        selectBMWradio = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
        selectBMWradio.click()
        time.sleep(10)

        """



nr = elementList()
nr.getElementList()