#Agenda:
#Basic WebDriver Commands
#Capture title of the page
#Closing and Quitting browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Chrome
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_4.0.0\IEDriverServer.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

#print(driver.title) #Return the title of the page
#print(driver.current_url) #Return URL of the page
#driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

#time.sleep(5)

#driver.close() #Currently focussed browser

#driver.quit() #Closing all the browsers