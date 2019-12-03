from selenium.webdriver.common.by import By


class handywrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorype == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Sorry the locator " + locatorType + " is not recognized")
            return False

    def getElement(self, locatorName, locatorType = "id"):
        element = None #element variable holder initialied as "none"
        try:

            locatorType = locatorType.lower()
            byType = self.getByType(locatorType) #get locatorType by using the getByType function
            element = self.driver.find_element(byType, locatorName)
            print("Element found")
        except:
            print("Not found1")
        return element











