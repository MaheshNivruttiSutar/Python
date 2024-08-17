from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

print(driver.title)  #Title of the page

print(driver.current_url)    #Returns the URl of the page

#print(driver.page_source)  #HTML code for the page

driver.close()  #Close the Browser