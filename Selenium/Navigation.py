from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)  #FR

driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)  #tt

driver.back()
time.sleep(5)
print(driver.title)  #FR

driver.forward()
time.sleep(5)
print(driver.title) #tt