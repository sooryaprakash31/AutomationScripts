from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from pathlib import Path

class BirthdayBot():
    def __init__(self):        
        self.username=input("Contact Name: ")
        print("Wish Text: ")
        self.lines = []
        while True:
            line = input()
            if line:
                self.lines.append(line)
            else:
                break
        self.date=input("Sending Date (yyyy-mm-dd): ")
        profile = webdriver.FirefoxProfile('/home/soorya/.mozilla/firefox/1gc0tunv.default')
        self.driver = webdriver.Firefox(profile)
        self.driver.get("https://web.whatsapp.com/")
        sleep(20)
        self.sendWish()

    def sendWish(self):
        try:
            contact = self.driver.find_element_by_xpath('//span[@title ="{}"]'.format(self.username))
        except Exception as e:
            print(e)
        contact.click()
        sleep(2)
        textBoxPath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
        for line in self.lines:
            self.driver.find_elements_by_xpath(textBoxPath)[0].send_keys(line)
            self.driver.find_elements_by_xpath(textBoxPath)[0].send_keys(Keys.SHIFT+Keys.ENTER)
        sleep(5)
        while True:
            currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.time = self.date + " 00:00:00"
            if currentTime==self.time:
                break
            sleep(1)
        sendButtonPath='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button'
        self.driver.find_elements_by_xpath(sendButtonPath)[0].click()
        
BirthdayBot()
