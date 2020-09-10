from selenium import webdriver
from time import sleep
import sys
import os

class BirthdayBot():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        sleep(10)
        self.username=input("Enter Contact Name: ")
        self.wishText=input("Enter Wish Text: ")
        self.wishText = self.getWishText()
        self.sendWish(self.wishText)

    def getWishText(self):
        wish = "Hello"
        return wish

    def sendWish(self,wishText):
        try:
            contact = self.driver.find_element_by_xpath('//span[@title ="{}"]'.format(self.username))
        except Exception as e:
            print(e)
        contact.click()

#Soorya 🔥

BirthdayBot()