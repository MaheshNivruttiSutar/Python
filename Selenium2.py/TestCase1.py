#PYTHON UNITTEST FRAMEWORK:
'''
-In automation testing. Organizing your code is very important and client except
us to write automation script according to the manual test cases.
-We can get good reporting structure if we can exactly map our automation code with
manual test cases.
-In Python we can use UnitTest testing framework to organize our automation code and
to extract reportc.
-To use the methods present in the UnitTest framework. We have to extend the TestCase class
present in the Unittest module.
'''



import unittest
class Test(unittest.TestCase):
    def test_firstTest(self):
        print("This is my first unit test case")

if __name__ == "__main__":
    unittest.main()