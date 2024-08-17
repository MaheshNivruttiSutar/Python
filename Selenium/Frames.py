#Working with Frames:
#                  - switch_to.frame(name)
#                  - switch_to.frame(id)

from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?deprecated-list.html")

driver.maximize_window()

driver.switch_to.frame("Packages")  #First Frame
#driver.find_elements_by_link_text("org.openqa.selenium").click()
driver.find_element_by_xpath("/html/body/main/ul/li[1]/a").click()
time.sleep(3)

#driver.switch_to.default_content() #For jumping second frame want to move main page

#driver.switch_to.frame("Interfaces")  #SecondFrame
#driver.find_element_by_link_text("WebDriver").click()
#time.sleep(3)

#driver.switch_to.default_content()
#time.sleep(3)
'''
driver.switch_to.frame("classFrame")  #ThirdFrame
driver.find_element_by_xpath("/html/body/div[1]/ui/li[5]").click()
'''
