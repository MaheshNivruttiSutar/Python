#Handling Cookies:
'''
-Cookies is piece of information from website and saved by your web browser.
-Cookies are way of remembering users and their interaction with the site by storing information in the
cookie file as key value pairs.
-It stores the login information like user name/email and password.
-HTTP cookie is also known as a web cookies, a browser cookie or internet cookie.

Operations on Cookies:
-Capture All Cookies from browser
-Count number of cookies
-Read Cookie pairs
-Adding new cookies
-Deleting pecific cookie by using name of cookie
-Deleting all the cookies
'''

#Demo Cookies:
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

#Capture all cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))  #Print number of cookies have been created
print(cookies)  #Print all the cookie pairs

#Adding new cookies to the browser:
cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies)) #Print number of cookies after adding new cookies
print(cookies)  #Print all the cookie pairs

#Delecting cookie:
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies)) #Print Number of cookies after dekecting the new cookies

#Deleting All the cookies:
driver.delete_all_cookies()  #Delete all cookies
cookies=driver.get_cookies() #Capture all the cookies after delecting
print(len(cookies))