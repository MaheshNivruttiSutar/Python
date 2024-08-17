#How to find how many input boxws present in web page
#How to provide value into text box
#How to get the status

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#How to find how many inputboxes present in web page

inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))   # 8

status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print(status)    #tr

status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("Displayed or not:",status)  #true/false

status=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("Enabled or not:", status)

#How to provide value into text box

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("pavan")

driver.find_element(By.ID,'RESULT_TextField-2').send_keys("kumar")

driver.find_element_by_id("RESULT_TextField-3").send_keys("333333333")

driver.find_element_by_id("RESULT_TextField-4").send_keys("India")

driver.find_element_by_id("RESULT_TextField-5").send_keys("Kolhapur")

driver.find_element_by_id("RESULT_TextField-6").send_keys("xyz@gmail.com")