from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from pathlib import Path

class BirthdayBot():
    def __init__(self):        
        self.username=input("Enter Contact Name: ")
        print("Enter Wish Text: ")
        profile = webdriver.FirefoxProfile('/home/soorya/.mozilla/firefox/1gc0tunv.default')
        self.driver = webdriver.Firefox(profile)
        self.driver.get("https://web.whatsapp.com/")
        sleep(20)
        self.sendWish()

    def getWishText(self):
        wish = ''' 
        Lorem ipsum
        '''
        return wish

    def sendWish(self):
        try:
            contact = self.driver.find_element_by_xpath('//span[@title ="{}"]'.format(self.username))
        except Exception as e:
            print(e)
        contact.click()
        sleep(1)
        
        self.driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')[0].send_keys("Your are the winner!!!"+ Keys.SHIFT + Keys.ENTER +"Contact 12345 for assistance")
        sleep(10)
        self.driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')[0].click()
        
BirthdayBot()
