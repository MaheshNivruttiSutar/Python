from selenium import webdriver

fp=webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain.application/pdf")  #Mine Type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C:\Downloadedfiles")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled",True)

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.30.0-win64/geckodriver.exe",firefox_profile=fp)

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