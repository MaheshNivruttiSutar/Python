#assertIn & assertNotIn:
'''
assertIn:method verifies whether the first element is present in the send element. if first element is present
in second element then test is passed otherwise test is failed.

assertNotn: method verifies whether the first element is not present in the second element or not,if first
element is present then test will be failed otherwise test is passed.

These two methods will be helpful when you want to verify presence of a value in a list,tuple,set and dictionary.
'''




import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        list=("python","selenium","java")
        #self.assertIn("python",list)  #Passed
        self.assertIn("ruby",list)  #Failed

        #self.assertNotIn("python",list) #failed
        #self.assertNotIn("ruby", list)

if __name__ == "__main__":
    unittest.main()