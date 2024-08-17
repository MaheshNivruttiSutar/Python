#How many link present
#Capture links
#Click on the link

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,"a")

print("Number of links present:",len(links))  #Print how many links present in a page

for link in links:
    print(link.text)

#clicking on the link
driver.find_element(By.LINK_TEXT,"REGISTER").click()

#driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
