#creating Test Cases and Test suites in python unittest framework
#Executing test suites

import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is login by facebook test")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("This is login by twitter test")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()