from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#chromeOptions=Options()
#chromeOptions.add_experimental_option()

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#Download text File:
driver.find_element_by_id('textbox').send_keys('My Name is Mahesh. I am from Kolhapur.')
driver.find_element_by_id('createTxt').click()  #Generate file button
#driver.find_element_by_id('link-to-download').click()  #Download link

#Download pdf File:
driver.find_element_by_id('pdfbox').send_keys('My Name is Mahesh. I am from Kolhapur.')
driver.find_element_by_id('createPdf').click()
#driver.find_element_by_id('pdf-link-to-download').click()

#driver.close()