#Waits - Implicit wait:It is time Based
#      - Explicit wait:It is Conditional Based

#Implicit Wait:
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")  #Opening URL takes some time

driver.maximize_window()
time.sleep(4)
driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()
