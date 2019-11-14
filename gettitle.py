from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class gettitle():

    def test(self):
        driverLocation = "/Users/rogelio.roldan/Documents/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        #baseURL = "https://letskodeit.teachable.com/p/practice"
        baseURL = "https://global.rakuten.com/en"
        driver.get(baseURL)



        pagetitle = driver.title
        print("The title of the page is " + pagetitle)

nr_gettitle = gettitle()
nr_gettitle.test()