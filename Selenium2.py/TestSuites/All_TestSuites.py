import unittest
from Package1.TC_loginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentText
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#Get all tests from LoginTest,SignUpTest,and PaymentReturnTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentText)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Creating test suites:
sanityTestSuite=unittest.TestSuite([tc1,tc2])     #Sanity test suits
functionalTestSuite=unittest.TestSuite([tc3,tc4])  #functional test suits

unittest.TextTestRunner().run(functionalTestSuite)