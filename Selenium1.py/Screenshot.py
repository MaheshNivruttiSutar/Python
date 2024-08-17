#Take Screenshot:WebDriver offers API's to take screenshot of a web page.
#                - save_screenshot('filename')
#                - get_screenshot_as_file('filename')

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.save_screenshot("C:\Screenshot\homepage.png")

#driver.get_screenshot_as_file("C:\Screenshot\homepage.png1")
#driver.get_screenshot_as_file("C:\Screenshot\homepage.jpg")