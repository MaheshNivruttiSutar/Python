#Conditional commands:
# - is_displayed()
# - is_enabled()
# - is_selected()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

user_ele=driver.find_element_by_name("userName")

print(user_ele.is_displayed())  #Returns true/false based of element status
print(user_ele.is_enabled())   #Return true/False

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())  #return true/false based of element status
print(pwd_ele.is_enabled()) #return true/false

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("submit").click()
time.sleep(5)
driver.find_element_by_name("Flights").click()
driver.find_element_by_name("Flights").click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button",roundtrip_radio.is_selected())  #print status of radio button round trip

onetrip_radio=driver.find_element_by_css_selector("input[value=oneway]")
print("status of oneway radio button",onetrip_radio.is_selected())
