# 3 Ways:
''' 1) Scroll down the page by pixel:
driver.execute_script("window.scrollBy(0,500)",""

2) Scroll down the page till element found:
driver.execute_script("arguments[0].scrollIntoView();",Element)

3) Scroll to end of the page:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
'''
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()  #Maximize window size

# 1) Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,8000)","")

# 2.Scroll down the page till element found:India Flag
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#flag=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[113]/td[2]')
#driver.execute_script("arguments[0].scrollIntoView();",flag)

# 3. Scroll to end of the page:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")