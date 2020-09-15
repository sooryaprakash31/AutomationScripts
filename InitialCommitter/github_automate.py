from selenium import webdriver
from time import sleep
import sys
import os

folderName = str(sys.argv[1])
username = str(sys.argv[2])
password = str(sys.argv[3])

class github:
     def __init__(self):
          self.driver = webdriver.Firefox()
          self.driver.get("https://github.com/login/")
          sleep(2)
          self.driver.find_element_by_name('login').send_keys(username)
          self.driver.find_element_by_name('password').send_keys(password)
          sleep(2)
          self.driver.find_element_by_name('commit').click()
          sleep(3)
          self.driver.get("https://github.com/new")
          sleep(3)
          self.driver.find_element_by_name('repository[name]').send_keys(folderName)
          sleep(1)
          self.driver.find_element_by_id('repository_visibility_private').click()
          sleep(2)
          self.driver.find_element_by_xpath("//button[contains(text(),'Create repository')]").click()
          sleep(3)
          self.driver.quit()

github()