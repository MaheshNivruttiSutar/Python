#Relational comparison:
'''
asssertGreater : verifies whether first values if greater than second value or not.
assertGreaterEqual: verifies whether first parameter is greater or equal to the second parameter.
assertLess: verifies whether first parameter is lesser than second parameter or not.
assetLessEqual: verifies whether firstparameter is lesser or equal to the second parameter.
'''

#assertGreater:

import unittest

class Test(unittest.TestCase):
    def testName(self):
        #self.assertLessEqual (100,100)
        #self.assertLess(10,100)

        #self.assertGreater(100,10)
        self.assertGreaterEqual(100, 100)
