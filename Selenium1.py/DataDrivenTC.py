import XLUtils

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.maximize_window()

path="C:\Drivers\DataDriven.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

    if driver.title=="Find a Flight: Mercury Tours:":
        print("test is passed")
        XLUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test failed")
        XLUtils.writeData(path,"Sheet1", r, 3, "test failed")

    driver.find_element_by_link_text("Home").click()
