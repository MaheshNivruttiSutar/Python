from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("file:///C:/SeleniumPractice/sample.html")

rows=len(driver.find_element_by_xpath("/html/body/table/tbody/tr")) #count number of rows
cols=len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th"))  #count number of column

print(rows)
print(cols)

print("Product"+"     "+"Article"+"    "+"Price")
for i in range(2, rows+1):
    for c in range(1, cols+1):
        value=driver.find_element_by_xpath("/ html / body / table / tbody / tr[3] / td[2]")
        print(value,end='    ')  #Product 1    0001   10