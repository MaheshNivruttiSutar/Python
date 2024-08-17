#Explicit Wait:It is Conditional Based
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("http://www.expedia.com/")

#driver.find_element_by_id("location-field-destination-dialog-trigger").click()
#driver.find_element_by_xpath('//*[@id="wizardMainRegionV2"]/div/ul/li[2]/a/span').click()

#driver.find_element(By.ID,"tab-flight-tab-hp".click()  #Flight Button

#driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")   #ORIGIN

time.sleep(2) #From Python

#driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC") #Destination

#driver.find_element(By.ID,"flight-departing-hp-flight").clear()
#driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("12/10/2018")

#driver.find_element(By.ID,"flight-returning-hp-flight").clear()
#driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("15/10/2018")

#driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

#Explicit Wait
wait=WebDriverWait(driver,10)
#element=wait.until(EC.element_to_be_clickable(By.XPATH,"//*[@id='stopFilter_stops-0']")

#element.click()

#time.sleep(3)

#driver.quit()