# Mouse Actions:
#               - Mouse Hover
#               - Double Click
#               - Right Click
#               - Drag and Drop


from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys("Admin")
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
usermgnt=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users=driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element("usermgnt").move_to_element(users).click()
