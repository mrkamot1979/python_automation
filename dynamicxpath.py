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

        #open browser and maximize
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        #initiate wrappers, locate Login link and click
        hw = handywrappers(driver)
        btnLogin = hw.getElement("//a[@class='navbar-link fedora-navbar-link']", "xpath")
        btnLogin.click()
        time.sleep(10)

        #locate the useremail/pwd, enter details then click login button
        inputEmail = hw.getElement("user_email")
        inputEmail.send_keys("test@email.com")
        inputPWD = hw.getElement("//input[@id='user_password']", "xpath")
        inputPWD.send_keys("abcabc")
        time.sleep(5)
        btnLoginForm = hw.getElement("//input[@name='commit']", "xpath")
        btnLoginForm.click()
        driver.implicitly_wait(5)

        #find the course via xpath

        # Select Course
        _course = "//div[@class='course-listing-title' and contains(text(),'{0}')]"
        _courseLocator = _course.format("Complete Step By Step Java For Testers")

        #print(str(_courseLocator))
        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        driver.implicitly_wait(5)



nr = dynamicxpath()
nr.test()