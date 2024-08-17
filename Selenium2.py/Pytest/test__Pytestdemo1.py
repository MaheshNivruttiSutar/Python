#How to Work with pytest fixture:
'''
The purpose of test fixture is to provide a fixed baseline upon which tests can
reliably and repeatedly execute.

@pytest_fixture()
Executes specific method before every test method.

@pytest.yield_fixture()
Execute specific method before & After every test method
'''


import pytest

@pytest.fixture()
def setup():
    print("Once before every Method")

def testmethod1(setup):
    print("This is test method1")

def testmethod2(setup):
    print("This is test method2")