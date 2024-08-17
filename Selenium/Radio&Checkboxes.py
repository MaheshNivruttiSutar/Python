#Radio button is selectied or not
#click

from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

#Working with the Radio Button
#Male:
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_displayed()   #false/True(Male)
print(status)

#driver.find_element_by_id("RESULT_RadioButton-7_0").click()  #Select radio button
#driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click()  #Select radio button

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()   #false/True
print(status)
#Female:
ststus=driver.find_element_by_id("RESULT_RadioButton-7_1").is_enabled()
print(status)

status=driver.find_element_by_id("RESULT_RadioButton-7_1").is_displayed()
print(status)

driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").click()

#Working with check boxes
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()  #Monday
#driver.find_element_by_id("RESULT_CheckBox-8_1").click()

#driver.find_element_by_id("RESULT_CheckBox-8_0").click()   #Sunday
driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[1]/td').click()  #Select radio button

#driver.find_element_by_id("RESULT_CheckBox-8_6").click()   #Saturday
driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[7]/td/label').click()  #Select radio button

status=driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)

status=driver.find_element_by_id("RESULT_CheckBox-8_6").is_selected()
print(status)
