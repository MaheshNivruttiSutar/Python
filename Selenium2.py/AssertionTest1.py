#Assertion:
'''
 -Assertion is nothing but the check point or you can say it as verification  for the test case
 to evaluate some itemon the execution.
 -If we do not provide any assertion inside a test case then there is no way to know whether a
 test case is failed or not.
 -Assertion helps in report generation.based on the assertions the test execution report
 will be generated.
 - Ther are few assertion which will accept all the values and few assertions will accept
 only numeric values.
'''
#AssertEqual & AssertNotEqual
'''
AssertEqual:assertWqual compare the first parameter with the second parameter, if both matches the unittest
will continue with the remaining executionbut the both the values are different then unit test fails the testcase.

AssertNotEqual:
assertNotEqual method compares the given two parameters, if both parameter are not same then unittest
passes the test case but if both parameter are same then unittest fails the test case. 
'''

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage=driver.title
        #assertEqual
        #self.assertEqual("Google",titleOfWebPage,"webpages titles are not same")
        self.assertNotEqual("Google123",titleOfWebPage)

if __name__=="__main__":
    unittest.main()

