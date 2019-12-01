from selenium.webdriver.common.by import By

class handrywrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatortype):
        locatortype = locatortype.lower()

        if locatortype = "id":
            return By.ID
        elif locatortype = "xpath"
            return By.XPATH


