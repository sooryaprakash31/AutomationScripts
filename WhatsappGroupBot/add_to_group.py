from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from configparser import ConfigParser
import csv

config = ConfigParser()
config.read('config.ini')

firefox_profile_path = config.get('FIREFOX', 'PROFILE_PATH')
name = config.get('NAME','GROUP_NAME')

class AddToGroup:
    
    numbers = []
    errorNumbers = []

    def __init__(self):
        profile = webdriver.FirefoxProfile(firefox_profile_path)
        self.driver = webdriver.Firefox(profile)
        sleep(2)
        self.login()
        self.getContactList()
        self.AddContacts()

    def AddContacts(self):
        self.driver.find_element_by_css_selector(".m7liR > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").click()
        sleep(2)
        self.driver.find_element_by_css_selector("div.eJ0yJ:nth-child(2) > div:nth-child(2)").click()
        print(self.numbers)
        for i in self.numbers:
            sleep(3)
            self.driver.find_element_by_css_selector("._9a59P > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > label:nth-child(4) > div:nth-child(1) > div:nth-child(2)").send_keys(i)
            sleep(2)
            try:
                self.driver.find_element_by_xpath(f'//span[@title ={i}]').click()
                sleep(2)    
            except Exception as e:
                print(e)
                self.errorNumbers.append(i)
            self.driver.find_element_by_css_selector(".MfAhJ").click()
            sleep(3)
        self.driver.find_element_by_css_selector("._3y5oW > span:nth-child(1)").click()
        sleep(2)
        self.driver.find_element_by_css_selector("div.S7_rT:nth-child(2)").click()
        sleep(5)
        self.driver.close()
        for i in self.errorNumbers:
            print(i)

    def getContactList(self):
        with open("data.csv","r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if len(row['number'])==10:
                    self.numbers.append(row['number'])
                else:
                    self.errorNumbers.append(row['number'])
    def login(self):
        self.driver.get("https://web.whatsapp.com/")
        sleep(20)
        group = self.driver.find_element_by_xpath(f'//span[@title="{name}"]')
        group.click()
        sleep(3)

AddToGroup()