#Working with Alerts:
#                  - switch_to_alert().accept()
#                  - switch_to_alert().dismiss()

from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

#driver.switch_to_alert().accept() #Closes alert window using OK button

#driver.switch_to_alert().dismisss()  #closes alert by using cancel button
driver.find_element_by_name('Cancel').click()

